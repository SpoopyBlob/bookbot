import time
import sys
from stats import character_occurrence
from stats import word_count

def organise_sys_arguments():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    return [sys.argv[n] for n in range(1, len(sys.argv))]

def store_file_metadata(list_of_paths):
    file_metadata = {}
    for path in list_of_paths:
        filename = retrieve_filename_from_path(path)
        try:
            file_metadata[filename] = {"filename": filename, "path": path, "contents": get_file_content(path)}
            print(f"{filename} found")
        except FileNotFoundError:
            print(f"{filename} could not be found")
        time.sleep(1)


    if len(file_metadata) == 0:
        print("ERROR: file not found!")
        sys.exit(1)

    return file_metadata 

def get_file_content(filepath):
    with open(filepath) as file:
        return file.read()
    
def retrieve_filename_from_path(path):
    split_path = path.split("/")
    return split_path[-1]


def load_book(book_content):
    word_split = book_content.split()
    
    pages = []
    page_counter = 1
    page = f"Page {page_counter}\n\n"
    

    for word in word_split:
        page += f"{word} "
        
        if len(page) > 2000:
            page += "\n\nn - next_page, p - previous_page, e - exit, f - first_page, l - last_page"
            pages.append(page)
            page_counter += 1
            page = f"Page {page_counter}\n\n"
    
    return pages


