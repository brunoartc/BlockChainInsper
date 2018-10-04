var CryptoJS = require("crypto-js");
var express = require("express");
var bodyParser = require('body-parser');
var request = require('request');

var app = express();
app.use(bodyParser.json());


paresNodes = []

class Block {
    constructor(index, previousHash, timestamp, data, hash) {
        this.index = index;
        this.previousHash = previousHash.toString();
        this.timestamp = timestamp;
        this.data = data;
        this.hash = hash.toString();
    }
}



var getGenesisBlock = () => {
    return new Block(0, "0", 1538628779, "Top Top mt Top, o primeiro bloco", "https://brartc.com");
};

var blockchain = [getGenesisBlock()];

function generateNextBlock(blockData){
    var BlocoAnterior = blockchain[blockchain.length - 1];
    var nextIndex = BlocoAnterior.index + 1;
    var nextTimestamp = new Date().getTime() / 1000;
    var nextHash = calculateHash(nextIndex, BlocoAnterior.hash, nextTimestamp, blockData);
    return new Block(nextIndex, BlocoAnterior.hash, nextTimestamp, blockData, nextHash);
};


function calculateHashForBlock(block){
    return calculateHash(block.index, block.previousHash, block.timestamp, block.data);
};

function calculateHash(index, previousHash, timestamp, data){
    return CryptoJS.SHA256(index + previousHash + timestamp + data).toString();
};

function addBlock(BlocoNovo){
    if (ValidoBlocoNovo(BlocoNovo, blockchain[blockchain.length - 1])) {
        blockchain.push(BlocoNovo);
    }
};

var ValidoBlocoNovo = (BlocoNovo, BlocoAnterior) => {
    if (BlocoAnterior.index + 1 !== BlocoNovo.index) {
        console.log('invalid index');
        return false;
    } else if (BlocoAnterior.hash !== BlocoNovo.previousHash) {
        console.log('invalid previoushash');
        return false;
    } else if (calculateHashForBlock(BlocoNovo) !== BlocoNovo.hash) {
        console.log(typeof (BlocoNovo.hash) + ' ' + typeof calculateHashForBlock(BlocoNovo));
        console.log('invalid hash: ' + calculateHashForBlock(BlocoNovo) + ' ' + BlocoNovo.hash);
        return false;
    }
    return true;
};


var handleBlockchainResponse = (message) => {
    if (typeof(message)==typeof(" ")) {
      var receivedBlocks = JSON.parse(message.data).sort((b1, b2) => (b1.index - b2.index));
    } else {
      var receivedBlocks = message.data.sort((b1, b2) => (b1.index - b2.index));
    }
    var latestBlockReceived = receivedBlocks[receivedBlocks.length - 1];
    var latestBlockHeld = blockchain[blockchain.length - 1];
    if (latestBlockReceived.index > latestBlockHeld.index) {
        console.log('blockchain possibly behind. We got: ' + latestBlockHeld.index + ' Peer got: ' + latestBlockReceived.index);
        if (latestBlockHeld.hash === latestBlockReceived.previousHash) {
            blockchain.push(latestBlockReceived);
            sendAll({'flag': 2,'data': JSON.stringify([blockchain[blockchain.length - 1]])});
        } else if (receivedBlocks.length === 1) {
            console.log("Precisamos atualizar os blocos");
            sendAll({'flag': 1});
        } else {
            console.log("Nossa blockchain esta errada sobreescrevendo");
            refazerCadeita(receivedBlocks);
        }
    } else {
        console.log('o Bloco recebido nao faze parte da blockchain');
    }
};

function refazerCadeita(BlocoNovos) {
    if (ValidoChain(BlocoNovos) && BlocoNovos.length > blockchain.length) {
        console.log('Received blockchain is valid. Replacing current blockchain with received blockchain');
        blockchain = BlocoNovos;
        sendAll({'flag': 2,'data': JSON.stringify([blockchain[blockchain.length - 1]])});
    } else {
        console.log('Received blockchain invalid');
    }
};

var ValidoChain = (blockchainToValidate) => {
    if (JSON.stringify(blockchainToValidate[0]) !== JSON.stringify(getGenesisBlock())) {
        return false;
    }
    var tempBlocks = [blockchainToValidate[0]];
    for (var i = 1; i < blockchainToValidate.length; i++) {
        if (ValidoBlocoNovo(blockchainToValidate[i], tempBlocks[i - 1])) {
            tempBlocks.push(blockchainToValidate[i]);
        } else {
            return false;
        }
    }
    return true;
};


function sendAll(msg) {
  for (i in paresNodes){
    request.post({
  	headers: {'content-type' : 'application/x-www-form-urlencoded'},
  	url:     i + "/qqAcontece",
  	body:    msg
		}, function(error, response, body){
  		console.log(body);
		});
  }

}
app.get('/Blocos', (req, res) => res.send(JSON.stringify(blockchain)));
app.post('/MinerarBloco', (req, res) => {
    var BlocoNovo = generateNextBlock(req.body.data);
    addBlock(BlocoNovo);
    sendAll({'flag': 2,'data': JSON.stringify([blockchain[blockchain.length - 1]])});
    console.log('block added: ' + JSON.stringify(BlocoNovo));
    res.send();
});
app.post('/qqAcontece', (req, res) => {
  var ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
  var message = req.body
  console.log('Received message' + JSON.stringify(message));
  switch (message.type) {
    case 0:
      res.send({'flag': 2,'data': JSON.stringify([blockchain[blockchain.length - 1]])});
      request.post({
    	headers: {'content-type' : 'application/x-www-form-urlencoded'},
    	url:     ip + ":" + 3001 + "/qqAcontece",
    	body:    {'flag': 2,'data': JSON.stringify([blockchain[blockchain.length - 1]])}
  		}, function(error, response, body){
    		console.log(body);
  		});
      break;
    case 1:
      res.send({'flag': 2, 'data': JSON.stringify(blockchain)});
      request.post({
    	headers: {'content-type' : 'application/x-www-form-urlencoded'},
    	url:     ip + ":" + 3001 + "/qqAcontece",
    	body:    {'flag': 2, 'data': JSON.stringify(blockchain)}
  		}, function(error, response, body){
    		console.log(body);
  		});
      break;
    case 2:
      res.send("acabou o bate-papo");
      handleBlockchainResponse(message);
      break;
  }
});
app.get('/ParesLista', (req, res) => {
    res.send(paresNodes.toString());
});
app.post('/addPar', (req, res) => {
    paresNodes.push(req.body.peer); //adiciona o ip de um node ao blockchain
    res.send();
});
app.get('/ultimoBloco', (req, res) => {
    res.send({'flag': 2,'data': JSON.stringify([blockchain[blockchain.length - 1]])}); //pega o ultimo bloco
});

app.get('/todosOsBlocosPls', (req, res) => {
    res.send({'flag': 2, 'data': JSON.stringify(blockchain)}); //pega o ultimo bloco
});

port = process.env.HTTP_PORT || 3001

app.listen(port, () => console.log('Server started: ' + port));
