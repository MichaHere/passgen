from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from colorama import Fore, Style
from enum import Enum
import random
import string

class CharacterTypes(Enum):
    Lowercase = 1
    Uppercase = 2
    Number = 3
    Special = 4

def generate_password(password_length, character_types):
    characters = {
        CharacterTypes.Lowercase: string.ascii_lowercase,
        CharacterTypes.Uppercase: string.ascii_uppercase,
        CharacterTypes.Number: string.digits,
        CharacterTypes.Special: string.punctuation,
    }

    chosen_characters = ""

    for character_type in character_types:
        chosen_characters += characters[character_type]
    
    generated_password = ""

    for i in range(0, password_length):
        random_index = random.randint(0, len(chosen_characters)-1)
        generated_password += chosen_characters[random_index]
    
    return generated_password

def prompt_length():
    try:
        return int(input("How Many Characters Do You Want Your Password To Be?\n~> "))
    except ValueError:
        print(f"{Fore.RED}ERROR: {Style.RESET_ALL}Please provide a valid number. ")
        prompt_length()
        return

def prompt_character_types():
    question_options = [Separator()] + [ 
        Choice(option, name=f"{option.name} Characters", enabled=True) for option in list(CharacterTypes) 
    ] + [Separator()]
    
    question = inquirer.checkbox(
        message="Select Character Types:",
        choices=question_options,
        cycle=False,
        transformer=lambda result: "%s Type%s Selected"
        % (len(result), "s" if len(result) > 1 else ""),
    )

    return question.execute()

def print_result(password):
    print(
f"""
{Fore.YELLOW}\
:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:
{Style.RESET_ALL}
Generated Password:
{password}
{Fore.YELLOW}
:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:\
{Style.RESET_ALL}\
"""
    )

def main():
    password_length = prompt_length()
    character_types = prompt_character_types()
    password = generate_password(password_length, character_types)
    print_result(password)

if (__name__ == "__main__"):
    main()
