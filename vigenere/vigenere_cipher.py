
class VigenereCipher(object):
    """
    Vigenere cipher helper
    """
    def __init__(self, key: str, alphabet: str):
        """
        Create an helper object for encoding and decoding the Vigenere cipher
        """
        self.key = key 
        self.abc = alphabet
    
    def encode(self, text: str):
        """
        Encode the given text
        """
        
        result = ""
        for i, ch in enumerate(text):
            
            if ch not in self.abc: 
                result += ch
            else:
                char_index = self.abc.find(ch)
                key_index = self.abc.find(self.key[i % len(self.key)])
                char_index = (char_index + key_index) % len(self.abc)
                result += self.abc[char_index]
        return result
    
    def decode(self, text: str):
        """
        Decode the given text
        """
        
        result = ""
        for i, ch in enumerate(text):
            
            if ch not in self.abc: 
                result += ch
            else:
                char_index = self.abc.find(ch)
                key_index = self.abc.find(self.key[i % len(self.key)])
                char_index = (char_index - key_index) % len(self.abc)
                result += self.abc[char_index]
        return result

