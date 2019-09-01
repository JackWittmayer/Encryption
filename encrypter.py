import webbrowser, bs4, requests, randomdotorg
# randomdotorg doesn't work in python 3. It does work in python 2.7.

def Offset(letter, amount):
    if letter.isalpha():
        newASCII = ord(letter.lower()) + amount
        while newASCII > 122:
            newASCII = 96 + (newASCII - 122)
        while newASCII < 97:
            newASCII = 123 - (97 - newASCII)
        return chr(newASCII)
    else:
        return letter

def Caesar(message, code):
    newMessage = ""
    for letter in message:
        letter = Offset(letter, code)
        newMessage += letter
    return newMessage

def DeCaesar(message, code):
    origMessage = ""
    for letter in message:
        letter = Offset(letter, -code)
        origMessage += letter
    return origMessage

def OneTimePadEncrypt(message, key):
    encrypted = ""
    i = 0
    for letter in message:
        encrypted += Offset(letter, key[i])
        i += 1
    return encrypted

def OneTimePadDecrypt(message, key):
    decrypted = ""
    i = 0
    for letter in message:
        decrypted += Offset(letter, -key[i])
        i += 1
    return decrypted


code = -863520
message = "The krabby patty secret formula is nothing."
encryptedMessage = (Caesar(message, code))
decryptedMessage = DeCaesar(encryptedMessage, code)
print ("Caesar Cypher: ")
print ("Original Message: " + message)
print ("Encrypted Message: " + encryptedMessage)
print ("Decrypted Message: " + decryptedMessage)

r = randomdotorg.RandomDotOrg('encrypter.py')
key = r.randrange(97, 122, 1, len(message))
# print ("\n" "Key: ")
# print (key)  # Don't show this to anyone!
encryptedMessage = OneTimePadEncrypt(message, key)
decryptedMessage = OneTimePadDecrypt(encryptedMessage, key)

print ("\n" + "One Time Pad: ")
print ("Original Message: " + message)
print ("Encrypted Message: " + encryptedMessage)
print ("Decrypted Message: " + decryptedMessage)

key = []  # Get rid of the key once it's used.
