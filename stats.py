def word_count(string):
    word_count = string.split()
    return len(word_count)

#helper function for sort_dict
def sort_on(items):
    return items["num"]

def sort_character_dict(character_dict):
    list_dict = []
    for key in character_dict:

        list_dict.append({"char": key, "num": int(character_dict[key])})
    
    list_dict.sort(reverse=True, key=sort_on)

    return list_dict

def character_occurrence(string):
    character_dict = {}
    for char in string:
        char = char.lower() 
        if character_dict.get(char) == None:
            character_dict[char] = 1
        else:
            character_dict[char] += 1

    return character_dict

def stats_pipeline(file_contents):
    character_dict = character_occurrence(file_contents)
    return sort_character_dict(character_dict)