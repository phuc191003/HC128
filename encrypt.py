import hc128
import codecs
import binascii
import time
start = time.time()
key = "0ABF78739497938948CB483EF7900C98098BDF"
IV  = "8570EBD0678676956A7897C667678D786B7676"

print ("Initializing HC-128 cipher state")
print ("Key = ",key)
print ("IV = ",IV)

hc128.init(key, IV)

print ("\nHC-128 Cipher state initialized")

'''file_name = input("\nEnter file to encrypt: ")'''
file_name = 'PCB.jpg'
print ("\nGenerating keystream, 4 bytes at a time")
k = hc128.keygen()
print ("Keystream generated: ", k)
with open (file_name, 'rb') as f:
  plain_text = f.read()
k = k.encode()
print(k)
cipher_text = b""
for i in range(0,len(plain_text)):
  cipher_text += bytes([plain_text[i] ^ k[i % 8]])

with open ("encrypt.txt", "wb") as f:
  f.write(cipher_text)
print ("Finished Encoded!")
end = time.time()
print("Excecution time: ", (end - start)* 10**3,"ms")
