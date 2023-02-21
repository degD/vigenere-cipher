
# Letter occurrance percentage in English text
letters_data = {
    'A': 8.85,
    'B': 1.73,
    'C': 3.66,
    'D': 3.56,
    'E': 11.94,
    'F': 1.81,
    'G': 1.92,
    'H': 4.12,
    'I': 7.19,
    'J': 0.16,
    'K': 0.89,
    'L': 3.97,
    'M': 2.44,
    'N': 7.05,
    'O': 7.25,
    'P': 2.74,
    'Q': 0.11,
    'R': 6.53,
    'S': 6.79,
    'T': 8.93,
    'U': 3.16,
    'V': 1.18,
    'W': 1.58,
    'X': 0.55,
    'Y': 1.73,
    'Z': 0.15
    }

# English alphabet
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Function for breaking the caesar cipher
def break_caesar(text_encoded: str):
    """
    Function for breaking English Caesar cipher encrypted text. Returns the shift value.
    """
    closeness = []
    for s in range(26):
        
        # Try shifting text with each possible shift value
        possible_text = "".join([abc[abc.index(c) - s] for c in text_encoded])
        
        # Count letters
        pos_letters_data = {c: 0 for c in abc}
        for c in possible_text:
            pos_letters_data[c] += 1

        # Calculate their percentages and then calculte how close they are to averages
        for l, n in pos_letters_data.items():
            perc = round(n / len(possible_text) * 100, 2)
            pos_letters_data[l] = abs(perc - letters_data[l]) / letters_data[l] * 100 
            
        # Add sum of those numbers to a list. Minimum of those numbers will determine the shift value
        closeness.append(sum(pos_letters_data.values()))
        
    # Find the shift value from the minimum
    return closeness.index(min(closeness))

def get_keyword(ciphertext: str, key_len: int) -> str:
    """
    Find the keyword for a string that is encoded with Vigenere cipher
    """
    
    # Divide text into sub-strings by key letters
    text_subdiv = ["" for _ in range(key_len)]
    for i, c in enumerate(ciphertext):
        text_subdiv[i % key_len] += c
        
    # Now process each sub-string the same way as breaking caesar cipher and save shift values as key characters
    key = "".join([abc[break_caesar(substr)] for substr in text_subdiv])
    
    return key
