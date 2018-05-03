from tkinter import *

from itertools import count, islice

class Window(Frame):

	def __init__(self,master=None):

		self.master = master

		Frame.__init__(self,self.master)

		self.master.title("Encryption RSA")

		self.grid()

		self.primo = 53

		self.primo_2 = 59

		self.constant = 2

		self.getPhrase()
	
	def getPhrase(self):

		Label(self.master,text="Generating encrypted messages using RSA").grid(row=0,column=0)

		Label(self.master,text="Enter the message you want to encrypt").grid(row=1,column=0)

		self.message = Entry(self.master)
		self.message.grid(row=1,column=1)

		Button(self.master,text="Start Encryption",command=self.getRealPhase).grid(row=2,column=1)

	def getRealPhase(self):

		self.message_real = self.message.get()	

		self.startEnctryption()	

	def startEnctryption(self):

		self.phraseASCII()

		self.generateKeys()

		self.phrase_encrypted = []

		for i in self.phrase:

			self.letter_encrypted = i**self.public_key % self.publickey

			self.phrase_encrypted.append(self.letter_encrypted)

		Label(self.master,text="Encryption done").grid(row=3,column=0)

		Button(self.master,text="Show message - Desencrypt",command=self.encryptionSolution).grid(row=4,column=0)

	def encryptionSolution(self):

		self.phrase_encrypted_ASCII = []

		self.arraw = [self.phrase_encrypted[0], self.phrase_encrypted[1], self.phrase_encrypted[2], self.phrase_encrypted[3], self.phrase_encrypted[4], self.phrase_encrypted[5], self.phrase_encrypted[6], self.phrase_encrypted[7], self.phrase_encrypted[8]]

		for i in self.arraw:

			self.solved = i ** 2011  % 3127

			self.phrase_encrypted_ASCII.append(self.solved)

		self.ASCIIphrase()

	def generateKeys(self):

		self.publickey = self.primo * self.primo_2

		self.phi = (self.primo-1) * (self.primo_2-1)

		for self.n in range(self.phi):

			if self.resultPublic():

				self.public_key = self.n

				break

		self.private_key = (self.constant * self.phi + 1)/self.public_key

		self.public_key_real = [self.public_key,self.publickey]

	def phraseASCII(self):

		self.phrase = []

		for i in self.message_real:

			self.letter = ord(i)

			self.phrase.append(self.letter)

	def ASCIIphrase(self):

		self.ASCII = []

		for i in self.phrase_encrypted_ASCII:

			self.letter_A = chr(i)

			self.ASCII.append(self.letter_A)

		Label(self.master,text=self.ASCII).grid(row=4,column=1)

	def resultPublic(self):

		if self.n <= 2: return False

		for self.a in islice(count(2), int((self.n**1/2)-1)):
			if not self.n%self.a:
				return False

		return True






root = Tk()


call = Window(root)

root.mainloop()
