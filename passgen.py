import os
import string
import secrets

SCANDIC_CHARACTERS_FI_SE = "öäåÖÄÅ"
SCANDIC_CHARACTERS_DK_NO = "øæÆØåÅ"

def save_password_to_file(password, password_file="./passwords.txt"):
    """
    Writes the generated password into the given file
    Defaults to writing to passwords.txt in current dir
    """
    try:
        with open(password_file, "a", encoding="utf-8") as f:
            f.write(password)
    except Exception as e:
        print(e)
        return -1

def print_passwords_from_file(password_file="./passwords.txt"):
    """
    Reads given file line by line and prints the passwords on separate lines.
    Defaults to passwords.txt in current dir
    """
    try:
        with open(password_file, "r", encoding="utf-8") as f:
            for line in f:
                print(line)
    except Exception as e:
            print(e)
            return -1

def generate_valid_characters(scandics_fi_se=True, scandics_dk_no=False, symbols=True) -> str:
    """
    Generates the possible characters used in the password generation
    """

    valid_characters = ""
    valid_characters += string.ascii_letters + string.digits
    if symbols:
        valid_characters += string.punctuation
    if scandics_fi_se:
        valid_characters += SCANDIC_CHARACTERS_FI_SE
    if scandics_dk_no:
        valid_characters += SCANDIC_CHARACTERS_DK_NO
    return valid_characters

def generate_password(characters: str, length: int) -> str:
    """
    Takes in the list off approved characters and the length of the password
    before generating a new password of desired length
    """
    password = "".join(secrets.choice(characters) for i in range(length))
    return password
    

if __name__ == "__main__":
    characters = generate_valid_characters()
    print(generate_password(characters, length=10))
