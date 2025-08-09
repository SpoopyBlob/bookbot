def get_num_words(string):
    word_count = string.split()
    return len(word_count)
    
def get_num_times(string):
    character_dict = {}
    for char in string:
        char = char.lower() 
        if character_dict.get(char) == None:
            character_dict[char] = 1
        else:
            character_dict[char] += 1

    return character_dict

def sort_on(items):
    return items["num"]


def sort_dict(dict_count):
    list_dict = []
    for key in dict_count:
        list_dict.append({"char": key, "num": int(dict_count[key])})
    
    list_dict.sort(reverse=True, key=sort_on)

    return list_dict
    