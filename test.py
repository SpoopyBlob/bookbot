import sys

with open("books/mobydick.txt","r") as f:
    sys.stdin = f
    user_input = f.readline()
    print(f"You entered: {user_input}")