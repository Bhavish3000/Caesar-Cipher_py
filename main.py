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

def secret(text, shift_amount, direction):
    """_Takes string as an input and do either encode or decode and gives the result_

    Args:
        text (_string_)
        shift_amount (_int_)
        direction (_string_)
    """
    output_text= ""
    if direction == "Decode":
        shift_amount = -shift_amount
    for letter in text:
        if letter in ALPHABET:
            shifted = ALPHABET.index(letter) + shift_amount
            shifted %= len(ALPHABET)
            output_text += ALPHABET[shifted]
        else:
            output_text += letter
    print(f"{direction}d message: {output_text}")

EXIT= False
while not EXIT:
    original_text= input("Enter the text: ").upper()
    shifts= int(input("No.of shifts: "))
    encode_decode= input("Encode (or) Decode: ")
    
    secret(text=original_text, shift_amount=shifts, direction=encode_decode)
    CONTINUE= input("Do want to CONTINUE (yes or no): ")

    if CONTINUE == "no":
        EXIT= True
