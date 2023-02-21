
import re
import letters as le
import caesar_cipher as cs


_letters = {
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


def format_text(text: str) -> str:
    """
    Format an English text to letter-only-uppercase form
    """
    return "".join(re.findall(r"[a-zA-Z]+", text)).upper()


def lettercloseness(avg_data: dict, shift_data: dict) -> float:
    """
    Returns a numerical representasion of how close the shifted letter data to letter' averages. 
    """
    res = 0
    for l, p in shift_data.items():
        avg_p = avg_data[l]
        res += abs(avg_p - p) / avg_p
    return res


def break_caesar(encrypted_text: str) -> tuple:
    """
    Enter an encoded uppercase-letters-only text. Function returns the shift value and decrypted version
    of the text.
    """
    
    # Shift until letter ocurrance is closest to averages
    l = []
    for s in range(26):
        text_decrypted = cs.caesar_decode(encrypted_text, s)
        l.append(lettercloseness(_letters, le.count_letters(text_decrypted)))
    shiftval = l.index(min(l))
    
    # Return the shift value and the decrypted text
    return shiftval, cs.caesar_decode(encrypted_text, shiftval)

