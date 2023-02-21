
# This file is only for debugs and tests. Currently obsolete file

import os
import re

"""
Average letter occurances. Might be useful
{'A': 8.85,
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
 'Z': 0.15}
 """


def count_letters(example_filename: str) -> dict:
    """
    Calculate letter occurance percentages in the given example file and return the results"
    """
    
    # Read the "example_filename" into variable "text"
    with open(f"./example texts/{example_filename}", encoding="utf-8") as f:
        text = f.read()
    
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

    # Sort the letter percentages using a new list from greater to smaller and print the results, for debug
    # abc_data_sorted = sorted(abc_dict.items(), key=lambda x: x[1], reverse=True)
    # for l, p in abc_data_sorted:
    #     print(f"{l}: {p}%")

    # Return the results
    return abc_dict


if __name__ == "__main__":
    
    results = []
    
    # Read each file and calculate letter occurances in the examples dir
    for f in os.listdir("./example texts"):
        results.append(count_letters(f))
    
    # Calculate the averages from the results
    abc_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    averages_dict = {l: 0 for l in abc_str}
    for res_dict in results:
        for l, p in res_dict.items():
            averages_dict[l] += p
    res_count = len(results)
    for l in averages_dict:
        averages_dict[l] = round(averages_dict[l] / res_count, 2)
        
    # Print the average occurances of letters, sorted up
    avg_data_sorted = sorted(averages_dict.items(), key=lambda x: x[1], reverse=True)
    for l, p in avg_data_sorted:
        print(f"{l}: {p}%")
