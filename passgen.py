"""Password generator

This script allows users to generate passwords of varying lengths using
standard ascii characters as well as common symbols and scandic characters.
"""

import string
import secrets
import argparse


def save_password_to_file(password_to_write: str, password_file: str = None):
    """
    Writes the generated password into the given file
    Defaults to writing to passwords.txt in current dir

    Parameters
    ----------
    password_to_write : str
        A string containing the password to be written to file.
    password_file : str
        A string containing the filepath and filename for output file.
    """
    # If no output file is selected, default to passwords.txt in current dir
    # TODO: Add OS detection to handle windows filepaths
    if password_file is None:
        password_file = "./passwords.txt"
    try:
        with open(password_file, "a", encoding="utf-8") as f:
            f.write(password_to_write)
    except Exception as e:
        # If we for some reason cannot write, print the error to terminal
        print(e)


def generate_valid_characters(**kwargs) -> str:
    """
    Generates the possible characters used in the password generation

    Returns
    -------
    valid_characters
        a string of characters that can be used for the password generation.
    """

    # We assume that ascii characters and numbers are always valid.
    valid_characters = string.ascii_letters + string.digits
    # Define the scandic character sets
    scandic_characters_fi_se = "öäåÖÄÅ"
    scandic_characters_dk_no = "øæåÆØÅ"

    if "punctuation" in kwargs and kwargs["punctuation"] is True:
        valid_characters += string.punctuation
    if "scandics" in kwargs:
        if kwargs["scandics"] == "NODK":
            valid_characters += scandic_characters_dk_no
        elif kwargs["scandics"] == "SEFI":
            valid_characters += scandic_characters_fi_se
    return valid_characters


def generate_password(passwd_characters: str, length: int) -> str:
    """
    Takes in the list off approved characters and the length of the password
    before generating a new password of desired length

    Parameters
    ----------
    passwd_characters : str
        String of characters that contain all allowed characters
    length : int
        Integer that defines the length of the generated password

    Returns
    -------
    generated_password
        A random generated string used as a password
    """
    if length <= 8:
        print(
            "Passwords of 8 characters or less are discouraged, as they can be cracked relatively quickly."
        )
    generated_password = "".join(
        secrets.choice(passwd_characters) for i in range(length)
    )
    return generated_password


if __name__ == "__main__":
    # Handle the arguments
    parser = argparse.ArgumentParser(
        description="Generate passwords for new services or user password recoveries."
    )
    parser.add_argument(
        "length",
        metavar="N",
        type=int,
        help="Desired length for the password. Recommended to be over 8",
    )
    parser.add_argument(
        "-o", "--output", type=str, help="Defines the output file for passwords"
    )
    parser.add_argument(
        "--scandics",
        type=str,
        choices=["NODK", "SEFI"],
        help="Define which nordic character set to use.",
    )
    parser.add_argument(
        "--punctuation",
        action="store_true",
        default=False,
        help="Enables punctuation characters for passwords.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Print password onto the terminal.",
    )
    args = parser.parse_args()

    # Start password generation
    characters = generate_valid_characters(
        scandics=args.scandics, punctuation=args.punctuation
    )
    password = generate_password(characters, length=args.length)

    # Handle output in file and terminal
    if args.output:
        save_password_to_file(password, password_file=args.output)
    if args.verbose is True:
        print(password)
