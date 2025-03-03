def word_counter(filename):
    word_list = filename.split()
    word_number = len(word_list)
    return word_number

def char_counter(filename):
    char_list = list(filename)
    unique_char_list = []
    for char in char_list:
        lower_char = char.lower()
        if lower_char not in unique_char_list:
            unique_char_list.append(lower_char)

    char_count = {}
    for char in char_list:
        lower_char = char.lower()
        if lower_char not in char_count:
            char_count[lower_char] = 1
        else:
            char_count[lower_char] += 1

    return char_count

def char_report(char_dict):
    #char_dict_list = []
    #for k, v in char_dict.items():
    #    char_dict_list.append({k:v})
    sorted_char_dict_list = dict(sorted(char_dict.items(), key = lambda item : item[1], reverse=True))
    for i in sorted_char_dict_list:
        if i.isalpha():
            print(f"{i}: {char_dict[i]}")


def sort_on(dict):
    return dict.values()
    





    #print(char_dict_list.sort())

    
    