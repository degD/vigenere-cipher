import re

def caesar_encode(text: str, shift: int) -> str:
    """
    Encode uppercase-letter-only text with the Caesar cipher
    """
    result = ""
    for ch in text:
        result += chr((ord(ch) - 65 + shift) % 26 + 65)
    return result

def caesar_decode(text: str, shift: int) -> str:
    """
    Decode uppercase-letter-only text with the Caesar cipher
    """
    result = ""
    for ch in text:
        result += chr((ord(ch) - 65 - shift) % 26 + 65)
    return result

if __name__ == "__main__":
    
    text = "Create an helper object for encoding and decoding the Vigenere cipher"
    text = "".join(re.findall(r"[a-zA-Z]+", text)).upper()
    text = 'SUOMSKUSDJBEPOIJOFQS'
    
    print(caesar_decode(text, 1))
    