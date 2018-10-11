const express = require('express');
const bodyParser = require('body-parser');
const app = express();
var fs = require('fs');
const NodeRSA = require('node-rsa');
var SHA256 = require("crypto-js/sha256");
const key = new NodeRSA({b: 1024});
const publicKey = key.exportKey('public');
const privateKey = key.exportKey('private');
var request = require('request');

const urlencodedParser = bodyParser.urlencoded({ extended: false })

app.set('view engine', 'ejs');


app.use(urlencodedParser);


var message = []

app.get('/', function(req, res) {
});

app.post('/', function(req, res) {
	var total = req.body
	message.push({ "receiver": total.receiver, "sender": total.sender, "message_enc": message_encrypt, "message": total.message, "public": publicKey });
});

app.get('/publickey', function(req, res) {
	res.send(publicKey)
});

app.get('/encryptmessage', function(req, res) {
	var total = req.body;
	res.render('forms', {qs: req.query});
});

app.post('/encryptmessage', function(req, res){
	var total = req.body;
	var message_int = total.message
	console.log(req.body)
	var message_encrypt = key.encryptPrivate(message_int);
	request.post({
	  	headers: {'content-type' : 'application/x-www-form-urlencoded'},
	  	url: "http://localhost:8001/", 
	  	form: { receiver: total.receiver, sender: total.sender, message_enc: message_encrypt, message: total.message, public: publicKey }
	})	
	res.render('forms', {total:req.body})
});


app.get('/readmessage', function(req, res) {
	request.get({
		headers: {'content-type' : 'application/x-www-form-urlencoded'},
		url: "https://6e7aee2d-7082-4464-83f0-ca2c55680f3a.mock.pstmn.io/publickey",
	}).pipe(key.importKey({resp}, 'components-public'); key.decryptPublic(message[0].message_encrypt) 

});




class Blocks{
	constructor(index, timestamp, previousHash, data, Hash) {
		this.index = index
		this.previousIndex.toString();
		this.Hash = Hash.toString()
		this.nonce = 0
		this.data = data //message["message"] + message["message_enc"] + message["publickey"]
		this.timestamp
	}

	calculateHash(){
		encrypted = SHA256(this.data + this.index + this.nonce + this.timestamp) //data: message["receiver"] + message["sender"] + message["message_enc"] + message["message"] + message["public"]
		return encrypted
	}

	mineBlock(difficulty){
		while (this.hash.substring(0, difficulty) !== Array(difficulty + 1).join("0")){
			this.nonce++
			this.hash = this.calculateHash()
		}
	}
}



class Blockchain{
    constructor() {
        this.chain = [this.createGenesisBlock()];
        this.difficulty = difficulty;
    }

    createGenesisBlock(){

		return new Blocks(0, "08/10/2018", "0", "bloco", "HASH");
    }



    getLatestBlock() {
        return this.chain[this.chain.length - 1];
    }


    addBlock(data) {
    	var blockchain = []
        const index = this.index
        const previousHash = this.getLatestBlock().hash
        const block = new Blocks(0, "08/10/2018", "0", "bloco", "00000000000000000000000")
        this.index++
        blockchain.push(block) //blockchain array
    }

}



nodes = []


app.get('/nodes', function(req, res){
	data = req.body
	nodes.push(data.url_node)
	for (var i of nodes) {
		var one_node
		one_node = i
	}
	request.post({
		headers: {'content-type' : 'application/x-www-form-urlencoded'},
	  	url: one_node, 
	  	body: blockchain[blockchain.length - 1]
	})
})




app.get('/publishBlockchain', function(req, res){
	res.send(blockchain.length, blockchain)
})



app.get('/getBlockchainRequest' function(req, res){

})

//pushblock - checar nodes na lista




 //app.set('port', process.env.PORT || 8001);
var port = process.env.PORT || 8001

 app.listen(port, function() {
	console.log("App running");
});