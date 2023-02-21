
import re

# Average letter occurances percentages
avg_data = {
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

def count_letters(text: str) -> dict:
    """
    Calculate letter occurance percentages in the given text and return the results"
    """
       
    # Format the text into an operatable form by removing whitespaces and punction, and turning all characters into uppercase
    text = "".join(re.findall(r"[a-zA-Z]+", text)).upper()

    # Create an alphabet dict
    abc_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc_dict = {l: 0 for l in abc_str}

    # Letter amounts
    for c in text: 
        abc_dict[c] += 1
        
    # Letter amounts by total letters, so percentages
    total_num_letters = sum(abc_dict.values())
    for l, n in abc_dict.items():
        abc_dict[l] = round(n / total_num_letters * 100, 2)

    # Return the results
    return abc_dict

