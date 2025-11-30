import string

def count_words(str):
    return str.split()

def count_chars(str):
    lower_str=str.lower()
    letter_counts = {letter: 0 for letter in string.ascii_lowercase}
    for s in lower_str:
        if s in letter_counts:
            letter_counts[s]+=1
    return letter_counts
    

def sort_on(d):
    return d["num"]

def letter_sort(counts):
    # Build a list of {"char": x, "num": y} dicts
    list_of_dicts = []
    for char, num in counts.items():
        list_of_dicts.append({"char": char, "num": num})
    
    # Sort by the "num" key, descending
    list_of_dicts.sort(reverse=True, key=sort_on)
    
    return list_of_dicts
