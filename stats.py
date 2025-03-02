def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    words_list = file_contents.split()
    num_words = len(words_list)
    return num_words

def get_char_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    words_list = file_contents.split()
    char_dict = {}
    for word in words_list:
        for char in word:
            char = char.lower()
            char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def sort_on(dict):
    return dict["count"]


def sort_dict(dict):
    dict_list = []   
    for char, count in dict.items():
        single_dict = {"character": char,"count": count}
        dict_list.append(single_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list




