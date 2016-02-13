ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def Caesar_encrypt(plaintext:str,key:int) -> str:
    '''takes in a string containing a message and a key.
    returns an encrypted version of the message
    '''
    key = key % 26
    table = str.maketrans(ALPHABET,shifter(key))
    return plaintext.translate(table)
            
            
            
def Caesar_decrypt(ciphertext:str,key:int) -> str:
    '''takes in a string containing an encrypted message
    and a key. returns a decrypted version of the message
    '''
    key = -(key % 26)
    table = str.maketrans(ALPHABET,shifter(key))
    return ciphertext.translate(table)


def shifter(num:int) ->str:
    '''takes takes a number and produces a "rotated" alphabet with the
    specified number of characters taken off the front and added on to
    the end of the string
    '''
    result = ALPHABET[num:len(ALPHABET)] + ALPHABET[0:num]
    return result

assert(Caesar_encrypt("Hi there", 29) == "Kl wkhuh")
assert(Caesar_decrypt("Kl wkhuh", 3) == "Hi there")


