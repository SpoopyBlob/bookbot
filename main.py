from stats import get_num_words
from stats import get_num_times
from stats import sort_dict
import sys

def get_book_text(filepath):
    try:
        with open(filepath) as file:
            return file.read()
    except Exception as e:
        print(e)
        sys.exit(1)
    
def print_stats(sorted_dict, word_count, book_path):

    header = (
    "============ BOOKBOT ============"
    f"\nAnalyzing book found at {book_path}"
    "\n----------- Word Count ----------"
    f"\nFound {word_count} total words"
    "\n--------- Character Count -------")

    end = "============= END ==============="

    character_counts = "\n"
    for item in sorted_dict:
        if item["char"].isalpha():
            character_counts += f'{item["char"]}: {item["num"]}\n'

    print(header + character_counts + end)


def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    file_text = get_book_text(filepath)
    word_count = get_num_words(file_text)
    sorted_dict = sort_dict(get_num_times(file_text))
    print_stats(sorted_dict, word_count, filepath)

main()