def count_words(file_contents):
    num_words = 0
    words = file_contents.split()
    
    for i in range (0, len(words)):
        num_words += 1
    return num_words

def count_characters(file_contents):
    lower_book = file_contents.lower()
    characters = {}
    for character in lower_book:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

def get_sorted_character_list(characters):
    letters = []
    for key, value in characters.items():
        if key.isalpha() == True:
            letters.append({"char": key, "num": value})
    letters.sort(reverse=True, key=sort_on)
    return letters
    
def sort_on(letters):    
    return letters["num"]
    
