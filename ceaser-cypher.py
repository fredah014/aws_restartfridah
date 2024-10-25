# define a function called getDoubleAlphabet that takes a string argument and concatenates, or combines, the given string with itself


def getDoubleAlphabet(alphabet):

    doubleAlphabet =alphabet + alphabet

    return doubleAlphabet


# test the function with a string argument


print(getDoubleAlphabet("hello")) # should return "hellohello"


print(getDoubleAlphabet("123")) # should return "123123"


print(getDoubleAlphabet("")) # should return ""


#GETTING  a cipher key

def getCipherKey():

    shiftAmount = input("please ente a key(whole number  from 1-25):")

    return shiftAmount
def getMessage():
    return input("Please enter the message to encrypt: ")
 # testing the function with a shift key

 # should return a whole number between 1 and 25

 # encrypting a string using a cipher key


 #Encrypt message

#Take three arguments: the message, the cipherKey, and the alphabet.


#Initialize variables.


#Use a for loop to traverse each letter in the message.


#For a specific letter, find the position.


#For a specific letter, determine the new position given the cipher key.


#If current letter is in the alphabet, append the new letter to the encrypted message.


#If current letter is not in the alphabet, append the current letter.


#Return the encrypted message after exhausting all the letters in the message.


def encryptMessage(message,cipherKey,alphabet):

    encryptedMessage = ""

    uppercaseMessage = ""

    uppercaseMessage = message.upper()

    for currentCharacter in uppercaseMessage:

        position = alphabet.find(currentCharacter)

        newPosition = position + int(cipherKey)

        if currentCharacter in alphabet:

            encryptedMessage = encryptedMessage + alphabet[newPosition]

        else:

                encryptedMessage = encryptedMessage + currentCharacter


    return encryptedMessage


    # testing the function with a message, cipher key, and alphabet

    print(encryptMessage("TRY ME!", "5", "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")) # should return "KHOOR, ZRUOG!"
def runCaesarCipherProgram():
    print(f'Alphabet: {"ABCDEFGHIJKLMNOPQRSTUVWXYZ"}')

    myAlphabet2 = getDoubleAlphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    print(f'Alphabet2: {myAlphabet2}')

    myMessage = getMessage()
    print(F'Message: {myMessage}')

    myCipherKey = getCipherKey()

    print(myCipherKey)

    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)

    print(f'Encrypted Message: {myEncryptedMessage}')

    myDecryptedMessage =DecryptedMessage(myEncryptedMessage, myCipherKey, myAlphabet2)

    print(f'MyDecypted Message: {myDecryptedMessage}')

runCaesarCipherProgram()































