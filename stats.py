def word_counter(file): # function takes a string as input and returns the number of words
    word_count = len(file.split())
    return word_count


def character_counter(file): # function takes a string as input and returns thea dictionary containing each unique character and how many times they appeared
    character_count = {}
    char_list = list(file.lower())
    for char in char_list:
        if char in character_count:
                character_count[char] += 1
        else:
                character_count[char] = 1
    return character_count


def char_count_list(chars_dict): #function takes a dictionary as input and returns a list of dictionaries sorted depending on the "num" key value from highest to lowest
    char_dict_list = []
    for char_key, char_value in chars_dict.items():
        char_kv_pair = {"char":char_key, "num":char_value}
        if char_kv_pair["char"].isalpha() is False:
            continue
        char_dict_list.append(char_kv_pair)
    char_dict_list.sort(reverse=True, key=char_sort)
    return char_dict_list

def char_sort(char_dict): # helper function is called in the char_count_list function's sort method to specify which key to sort by, returns the "num" key
    return char_dict["num"]
    


