from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

def check_text(text):
 while (len(text) % 16) != 0 :
 text += " "
 return text

key = get_random_bytes(16)
key = str(key)
key_list = key.split('\\')
key_str = ""

for element in key_list:
 key_str += element

key = key_str[2:18]


message = input("Enter the message you want to send: ")
output_message = check_text(message)

des = DES3.new(key , DES3.MODE_ECB)
encrypted_text = des.encrypt(output_message)


decrypted_text = des.decrypt(encrypted_text)

