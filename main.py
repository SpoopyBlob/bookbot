from utility import organise_sys_arguments
from utility import store_file_metadata
from utility import load_book
from stats import word_count
from stats import stats_pipeline

import os
import time
import sys

def main ():
    print("Welcome to BOOKBOT... loading files")
    filepaths = organise_sys_arguments()
    file_metadata = store_file_metadata(filepaths)
    user_control(file_metadata)
    
def user_control(file_metadata):
    main_msg = main_page_string(file_metadata)
    while True:
        os.system("clear")
        print(main_msg)

        user_input = input("")

        if user_input.lower() == "e":
            sys.exit()

        elif user_input in file_metadata:
            open_book(file_metadata[user_input])

        else:
            msg = (
                "=================================\n"
                " The filename you entered didn't\n"
                "     match, please try again!"
                )
            print(msg)
            time.sleep(2)

def open_book(file_meta):
    msg = open_book_string(file_meta["filename"])
    while True:
        os.system("clear")
        print(msg)
        user_input = input()

        if user_input == "e":
            return
        elif user_input == "s":
            os.system("clear")
            if not "stats" in file_meta:
                stats_string(file_meta)
            print(file_meta["stats"])
            i = input()
        elif user_input == "r":
            book = load_book(file_meta["contents"])
            read_book(book)
        else: 
            print("Invalid input, please try again!")
            time.sleep(2)

def read_book(book):
    index = 0
    while True:
        os.system("clear")
        print(book[index])
        print("\n\nn - next_page, p - previous_page, e - exit, f - first_page, l - last_page")
        user_input = input()

        if user_input == "e":
            return
        elif user_input =="f":
            index = 0
        elif user_input == "l":
            index = len(book) - 1
        elif user_input == "n":
            if index + 1 <= len(book) - 1:
                index += 1
            else:
                print("Can't go forward, last page...")
                time.sleep(1)
        elif user_input == "p":
            if index == 0:
                print("Can't go back, first page...")
                time.sleep(1)
            else:
                index -= 1
        else:
            print("Invalid input, please try again")
            time.sleep(1)

def main_page_string(file_metadata):
    header = (
        "============ BOOKBOT ============\n"
        "       Books found include:      \n"   
        )
    filenames = ""
    for key in file_metadata:
        filenames += f"{key}\n"

    rest = (
        "=================================\n"
        " Write the name of the book you\n"
        "       would like to select\n" 
        "   or type e to exit the program"   
        )

    return header + filenames + rest

def open_book_string(filename):
    msg = (
        "============ BOOKBOT ============\n"
        f"You have selected {filename}\n"
        "  r - read, s - stats, e - exit\n"
        ) 
    return msg

def stats_string(file_meta):

    header = (
    "============ BOOKBOT ============"
    f"\nAnalyzing book found at {file_meta["path"]}"
    "\n----------- Word Count ----------"
    f"\nFound {word_count(file_meta["contents"])} total words"
    "\n--------- Character Count -------")

    character_counts = "\n"
    for item in stats_pipeline(file_meta["contents"]):
        if item["char"].isalpha():
            character_counts += f'{item["char"]}: {item["num"]}\n'

    end = (
        "============= END ===============\n"
        "   type any character to return"
           )

    file_meta["stats"] = header + character_counts + end

main()

