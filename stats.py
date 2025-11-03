def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    dict = {}
    for c in text:
        c = c.lower()
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    return dict

def get_sorted_dict(dict):
    list = []
    for key in dict:
        new_dict = {"char": key, "num": dict[key]}
        list.append(new_dict)

    list.sort(key=helper)
    return list

def helper(dict):
    return dict["num"]
