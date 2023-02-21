
import re
import vigenere_cipher as vc

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


# Function for breaking the caesar cipher
def break_caesar(text_encoded: str):
    """
    Function for breaking English Caesar cipher encrypted text. Returns the shift value.
    """
    closeness = []
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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


# Formatting the text for use
txt = "The game is also accompanied by free patches, which may adjust existing mechanics or add new ones in the same theme as the expansions. The first major patch arrived on May 24, shortly after the game's release, featuring numerous improvements to the AI, as well as an additional playable race.[14] The 2.0 patch (Cherryh), released in February 2018, revamps a significant amount of game mechanics, even for players who have not purchased the corresponding Apocalypse DLC. The 2.1 (Niven) update, released alongside the Distant Stars DLC in May, revamped the base game play loop and added more quality-of-life features. The 2.2 (Le Guin) update was released in December, along with the Megacorp DLC, and revamped how planets are organized. The 3.0 (Dick) update was released in April 2021, coinciding with the release of the Nemesis DLC.[15] Minor releases have continued through 2022 with 3.5 being released September 2022."
txt_f = "".join(re.findall(r"[a-zA-Z]+", txt)).upper()

# Creating the helper object
key = "AMOGUS"
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
vc_ho = vc.VigenereCipher(key, abc)

# Encoding the text
txt_f_en = vc_ho.encode(txt_f)

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
    
    

# Now starting the key finding operation
# Only encoded text and key length are known
encodedtext = txt_f_en
keylen = len(key)

# Divide text into sub-strings by key letters
txt_f_en_subdiv = ["" for _ in range(keylen)]
for i, c in enumerate(encodedtext):
    txt_f_en_subdiv[i % keylen] += c
    
# Now process each sub-string the same way as breaking caesar cipher and save shift values as key characters
txt_key = "".join([abc[break_caesar(substr)] for substr in txt_f_en_subdiv])

# Print the key
print(txt_key)
        