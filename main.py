import sys
from stats import word_counter, character_counter, char_count_list

if (len(sys.argv) < 2 or len(sys.argv) > 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_input = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(book_input)} total words")
    print("--------- Character Count -------")
    #print(char_count_list(character_counter(selected_book)))
    for char_dict in char_count_list(character_counter(book_input)):
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")
    


def get_book_text(file): # function takes a path to a .txt file as input and returns the contents of the file as a string a string
    with open(file) as f:
        file_contents = f.read()
        return file_contents

main()