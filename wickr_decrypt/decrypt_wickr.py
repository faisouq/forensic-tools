import binascii
import scrypt
from Crypto.Cipher import AES

passwd = input("Fill in the plaintext Wickr Me password: ")

with open("sk.wic", "rb") as file:
    data = file.read()
    hexdata = binascii.hexlify(data)

with open("output.txt", "wb") as outputfile:
    outputfile.write(hexdata.upper())

with open("output.txt", "rb") as datafile:
    data = str(datafile.read())

KDF_salt = bytes.fromhex(data[4:36])
GCM_nonce = bytes.fromhex(data[38:62])
GCM_tag = data[62:94]
ciphertext = data[94:238]

key = scrypt.hash(passwd, KDF_salt, 131072, 8, 1, 32)

encryption = AES.new(key, AES.MODE_GCM, GCM_nonce)
cipher = encryption.encrypt(bytes.fromhex(ciphertext))

AES_GCM = cipher.hex()

db_password = AES_GCM[8:74]
print(f"The database password is: {db_password}. You can put this in SQLcipher to decrypt the database.")