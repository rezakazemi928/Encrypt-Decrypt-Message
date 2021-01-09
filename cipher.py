import random

alphabet = 'arzhino0123456789/'
letter_to_index = dict(zip(alphabet , range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)) , alphabet))

preson = {
    'name': 'zhino',
    'bro1_name': 'zhiar',
    'bro2_name': 'arzhin',
    'birthday': '78/5/13',
    'bro1_birth': '86/9/14',
    'bro2_birth': '92/11/30',
}

def generate_key(num):
    key = ''
    for num in range(num):
        key += random.choice('arzhino0123456789/') 
    
    return key

def encrypt(message , key):
    encrypt_message = ''
    split_message = [message[i : i + len(key)] for i in range(0 , len(message) , len(key))]
    
    for each_element in split_message:
        i = 0;
        
        for letter in each_element:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            encrypt_message += index_to_letter[number]
            i += 1
            
    return encrypt_message

def decrypt(cipher_message , key):
    split_message = [cipher_message[i : i + len(key)] for i in range(0 , len(cipher_message) , len(key))]
    decrypt_message = ''
    
    for each_element in split_message:
        i = 0;
        
        for letter in each_element:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            decrypt_message += index_to_letter[number]
            i += 1
    return decrypt_message


plain_text = preson['name'] + preson['bro1_name'] + preson['bro2_name'] + preson['birthday'] + preson['bro1_birth'] + preson['bro2_birth']
key = generate_key(4)
encrypt_message = encrypt(plain_text , key)
decrypt_message = decrypt(encrypt_message , key)

print(f"key: {key} , encript_message: {encrypt_message} , decripted_message:{decrypt_message}")