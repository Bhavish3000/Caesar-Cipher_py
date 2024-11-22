"""_This module creaters the encoded value of Ceaser Cipher and decode the value to its original state_
"""

ALPHABET= [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z',' ',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        '!','"','#','$','%','&',"'",'(',')','*','+',
        ',', '-', '.', '/', ':',';','<','=','>','?',
        '@','[','\\',']', '^','_','`','{','|','}','~'
    ]
EXIT= False
while not EXIT:
    original_text= input("Enter the text: ").upper()
    shifts= int(input("No.of shifts: "))
    state= input("Enter (Encode or Decode): ")

    def encode(text, shift_amount):
        """_This function takes the text and shift_amount as inputs and
            encode in ceaser cipher algorithm_

        Args:
            text (_string_): _original text_
            shift_amount (_integer_): _number of shifts_
        """
        encoded_text= ""
        for letter in text:
            shifted = ALPHABET.index(letter) + shift_amount
            shifted %= len(ALPHABET)
            encoded_text += ALPHABET[shifted]
        print(f"Encoded message: {encoded_text}")

    def decode(text, shift_amount):
        """_This function takes the text and shift_amount as inputs and
            decode in ceaser cipher algorithm_

        Args:
            text (_string_): _original text_
            shift_amount (_integer_): _number of shifts_
        """
        output_text= ""
        for letter in text:
            shifted = ALPHABET.index(letter) - shift_amount
            shifted %= len(ALPHABET)
            output_text += ALPHABET[shifted]
        print(f"Decoded message: {output_text}")
    if state == "Encode":
        encode(text=original_text, shift_amount=shifts)
    elif state == "Decode":
        decode(text=original_text, shift_amount=shifts)
    CONTINUE= input("Do want to CONTINUE (yes or no): ")
    if CONTINUE == "no":
        EXIT= True
