import math
# m vai ser a mensagem em ASCII

# e é chave que o toranja passsou (141837)
e = 1411837
# n é a multiplicação das chaves (153721)
n = 153721
# c é a mensagem encriptada

# % corresponde ao mod

# d é a chave privada 

message = "Ja sou um hacker" #input("Enter message to encrypt: ")

def encode(msg):
	m = "999"
	for ch in msg:
		m = m + "{:0>3d}".format(ord(ch))
		mi = int(m)
	return mi

def decode(m):
	s=str(m)
	msg = ""
	for i in range(2,1+int(len(s)/3)):
		msg = msg + chr(int(s[(3*i-3):(3*i)]))
	return msg

def encrypt(m,e,n):
	c = (m** e) % n
	return c

def decrypt(c,d,n):
	m = (c ** d) % n
	return m

#print(message)
#m=encode(message)
#print(m)
#c=encrypt(m,e,n)
#print(c)
#m2=decrypt(c,d,n)
#dm=decode(m)
#print(dm)