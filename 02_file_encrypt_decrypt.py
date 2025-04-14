# Demo - File Based
# 	Demostrates file encryption/decryption
from mc_core import *
import filecmp
tPriv = privateKeyH84()
tPub = publicKeyH84(tPriv.makeGPrime())

try:
    while (not(filecmp.cmp("caesar_letter.txt", "caesar_letter.txt.ctxt.decoded", shallow = False))):
     print ("Encrypting...")
     tPub.encryptFile("caesar_letter.txt")
     print ("Decrypting...")
     tPriv.decryptFile("caesar_letter.txt.ctxt")

except FileNotFoundError or IOError:
    print ("Encrypting...")
    tPub.encryptFile("caesar_letter.txt")
    print ("Decrypting...")
    tPriv.decryptFile("caesar_letter.txt.ctxt")

finally:
     while (not(filecmp.cmp("caesar_letter.txt", "caesar_letter.txt.ctxt.decoded", shallow = False))):
      print ("Encrypting...")
      tPub.encryptFile("caesar_letter.txt")
      print ("Decrypting...")
      tPriv.decryptFile("caesar_letter.txt.ctxt")
