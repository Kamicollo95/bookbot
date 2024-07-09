def get_text(path):
    with open(path) as f:
        return f.read()
    

def get_word_count(text):
    words = text.split()
    return len(words)


def character_count(text):
    character_count = {}
    for character in text.lower():
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count

def sort_on(d):
    return d["Freq"]

def sort_characters_to_letters(dict):
    sorted_letters = []
    for entry in dict:
        sorted_letters.append({"Letter": entry, "Freq": dict[entry]})
    sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters 

def main(book):
    book_path = f"books/{book}.txt"
    text = get_text(book_path)
    num_words = get_word_count(text)
    num_letters = character_count(text)
    sorted_letters = sort_characters_to_letters(num_letters)
    print(f"{num_words} words found in the document.")
    for letter in sorted_letters:
        if letter["Letter"].isalpha():
            print(f"The '{letter['Letter']}' character was found {letter['Freq']} times.")

main("frankenstein")