import itertools
import time
import os
import platform
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    """Clear the terminal screen."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def generate_and_display_wordlist(characters, min_length, max_length):
    wordlist = []
    start_time = time.time()
    print(Fore.CYAN + "\nGenerating words...\n")

    for length in range(min_length, max_length + 1):
        for word in itertools.product(characters, repeat=length):
            word_str = ''.join(word)
            print(Fore.YELLOW + word_str)
            wordlist.append(word_str)

    end_time = time.time()
    generation_time = end_time - start_time

    print(Fore.GREEN + f"\nNumber of words generated: {len(wordlist)}")
    print(Fore.GREEN + f"Time taken to generate wordlist: {generation_time:.2f} seconds")

    return wordlist

def save_wordlist(wordlist, filename):
    try:
        with open(filename, "w") as f:
            for word in wordlist:
                f.write(word + '\n')

        file_size = os.path.getsize(filename)
        print(Fore.MAGENTA + f"Wordlist saved to {filename} with size {file_size / 1024:.2f} KB")
    except Exception as e:
        print(Fore.RED + f"Error saving wordlist: {e}")

def display_welcome_banner():
    """Display the welcome banner with ASCII art."""
    cat_art = r"""
  /\_/\  
 ( o.o ) 
 > ^ <  
"""
    banner_text = "Welcome to the Wordlist Generator!"
    
    print(Fore.BLUE + Style.BRIGHT + "=" * 50)
    print(Fore.MAGENTA + Style.BRIGHT + cat_art)
    print(Fore.CYAN + Style.BRIGHT + banner_text)
    print(Fore.BLUE + Style.BRIGHT + "=" * 50)

def main():
    try:
        clear_screen()
        display_welcome_banner()

        characters = input(Fore.CYAN + "Enter the characters to use: ")
        if not characters:
            raise ValueError("Character set cannot be empty.")

        min_length = int(input(Fore.CYAN + "Enter the minimum length of the words: "))
        max_length = int(input(Fore.CYAN + "Enter the maximum length of the words: "))
        if min_length > max_length or min_length <= 0:
            raise ValueError("Invalid length range specified.")

        wordlist = generate_and_display_wordlist(characters, min_length, max_length)

        save_choice = input(Fore.CYAN + "Do you want to save the wordlist to a file? (Y/n): ").strip().lower()
        save_to_file = (save_choice == 'y' or save_choice == '')

        if save_to_file:
            filename = input(Fore.CYAN + "Enter the filename (with .txt extension): ").strip()
            save_wordlist(wordlist, filename)
    except ValueError as ve:
        print(Fore.RED + f"Input error: {ve}")
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

