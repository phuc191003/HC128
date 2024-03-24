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

'''file_name = input("\nEnter file to decrypt: ")'''
file_name = "encrypt.txt"
print ("\nGenerating keystream, 4 bytes at a time")
k = hc128.keygen()
print ("Keystream generated: ", k)
with open (file_name, 'rb') as f:
  cipher_text = f.read()
k = k.encode()
print(k)
plain_text = b""
for i in range(0,len(cipher_text)):
    plain_text += bytes([cipher_text[i] ^ k[i%8]])
with open ("pcb_decrypt.jpg", "wb") as f:
  f.write(plain_text)
print ("Finished Decode! ")
end = time.time()
print("Exceution time: ", (end - start)* 10**3,"ms")