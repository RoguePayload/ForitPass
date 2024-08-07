import random
import string
import time
import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to generate a password
def generate_password(length, use_symbols, use_numbers, complexity):
    base_characters = string.ascii_letters
    characters = base_characters
    
    if use_symbols:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits

    # Adjust complexity
    password = ''
    for _ in range(length):
        if complexity >= 8:
            # Very complex: mix letters, numbers, symbols heavily
            characters = ''.join(random.sample(characters, len(characters)))
        elif complexity >= 5:
            # Moderate complexity: mix letters with occasional numbers and symbols
            characters = ''.join(random.sample(base_characters + string.digits, len(base_characters) + len(string.digits)))
        else:
            # Less complex: mostly letters, some numbers
            characters = ''.join(random.sample(base_characters, len(base_characters)))

        password += random.choice(characters)

    return password

# Main menu
def main_menu():
    clear_screen()
    print("\033[34mFortiPass\033[0m")
    print("\033[33mThe Ultimate Password Generator\033[0m")
    print("\033[32mDeveloped by Rogue Payload\033[0m")
    print("1. Generate Password")
    print("2. Exit")
    print("\033[36mEnter your choice: \033[0m", end='')

# Password generator menu
def password_generator_menu():
    time.sleep(2)
    clear_screen()
    print("\033[31mLoading Password Generator Configurations...\033[0m")
    time.sleep(2)
    clear_screen()
    print("\033[34mFortiPass\033[0m")
    print("\033[33mThe Ultimate Password Generator\033[0m")
    print("\033[32mPassword Generator\033[0m")
    
    # Getting user input
    print("\033[32mPlease Select the Length of Password [5-99]: \033[0m", end='')
    length = int(input("\033[36m"))
    
    print("\033[32mUse Symbols? [Y/N]: \033[0m", end='')
    use_symbols = input("\033[36m").strip().upper() == 'Y'
    
    print("\033[32mUse Number? [Y/N]: \033[0m", end='')
    use_numbers = input("\033[36m").strip().upper() == 'Y'
    
    print("\033[32mComplexity? [1-10]: \033[0m", end='')
    complexity = int(input("\033[36m"))
    
    password = generate_password(length, use_symbols, use_numbers, complexity)
    print(f"\033[36mGenerated Password: {password}\033[0m")

def main():
    while True:
        main_menu()
        choice = input("\033[36m").strip()

        if choice == '1':
            password_generator_menu()
            input("\033[36mPress Enter to return to main menu...\033[0m")
        elif choice == '2':
            print("\033[31mShutting Down Systems...\033[0m")
            time.sleep(2)
            clear_screen()
            break
        else:
            print("\033[31mInvalid choice. Please try again.\033[0m")
            time.sleep(2)

if __name__ == "__main__":
    main()
