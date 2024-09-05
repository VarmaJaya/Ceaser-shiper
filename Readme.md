Caesar Cipher Program
This Python program implements the Caesar Cipher for encoding and decoding messages by shifting letters of the alphabet. It allows users to encrypt and decrypt text with a specified shift value. The program handles edge cases, such as shift values greater than the number of letters in the alphabet, by using the modulus operator.

Features:
Encrypt or Decrypt: Users can choose to either encode (encrypt) or decode (decrypt) a message.
Customizable Shift: Users can input any shift number, and the program will automatically adjust for shift values larger than 26.
Special Characters: Non-alphabet characters (such as spaces or punctuation) are preserved in the message without encryption.
User-Friendly Interface: The program continuously prompts users if they would like to restart the cipher for another message, making it convenient to use multiple times.
Logo Display: The program imports and displays a logo from the art.py file when it starts.
How to Run:
Clone the repository and ensure art.py is present for logo display.
Run the program, and follow the prompts to encode or decode your message.
Example:
Input: encode, message: "hello", shift: 5
Output: "mjqqt"
