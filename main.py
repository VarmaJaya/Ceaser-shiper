alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    



    





# My_code
'''
#TODO-3: Create a function called 'ceaser' that takes the 'text' and 'shift' as inputs., it combines the two functions both encript and decript

#def ceaser(dir, txt, shft):

def ceaser(start_text, shift_amount, chipher_direction):
    end_text = ""
    if chipher_direction == "decode":
            shift_amount*=-1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        end_text+=new_letter
    print(f"the {chipher_direction}d text is: {end_text}")

ceaser(start_text=text, shift_amount=shift, chipher_direction=direction)

again = input("Type 'yes' if you want to go again or Type 'no' if you want to quit: ")
go_again = True
while go_again:
     if again == "yes":
        ceaser(start_text=text, shift_amount=shift, chipher_direction=direction)
     else:
          go_again = False

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#def encrypt(dir, txt, shft):

def encrypt(plain_text, shift_amount):
    chipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        chipher_text +=new_letter
    print(f"the encoded text is: {chipher_text}")
'''
#TODO-2: Create a function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#def decrypt(dir, txt, shft):
'''
def decrypt(chipher_text, shift_amount):
    plain_text = ""
    for letter in chipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text +=new_letter
    print(f"the decoded text is: {plain_text}")
    

'''


'''
   Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(chipher_text=text, shift_amount=shift)
'''
