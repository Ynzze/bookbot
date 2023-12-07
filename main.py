def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_dict = count_unique_characters(text)
    print_report(book_path, num_words, character_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_unique_characters(text):
    unique_characters = {}
    for character in text:
        character = character.lower()
        if character not in unique_characters:
            unique_characters[character] = 1
        else:
            unique_characters[character] += 1
    return unique_characters

def print_report(book_path, words_found, input_dict):
    report_list = list(input_dict.items())
    report_list.sort()
    final_list = []

    for key, value in report_list:
        if key.isalpha() :
            final_list.append((key, value))

    print(f"--- Begin report of {book_path} ---")
    print(f"{words_found} words found in the document")
    
    for key, value in final_list :
        print(f"The '{key}' was found {value} times")

    print("--- End report ---")


main()