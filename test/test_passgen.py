import passgen
import string
from constants import (
        SCANDIC_SE_FI,
        SCANDIC_NO_DK
        )


def test_generate_valid_characters_scandics():
    kwargs = {"scandics": "SEFI"}
    charset = passgen.generate_valid_characters(**kwargs)
    assert SCANDIC_SE_FI in charset


def test_generate_valid_characters_no_scandics():
    charset = passgen.generate_valid_characters()
    assert SCANDIC_NO_DK not in charset


def test_generate_valid_characters_punctuation():
    kwargs = {"punctuation": True}
    charset = passgen.generate_valid_characters(**kwargs)
    assert string.punctuation in charset


def test_generate_valid_characters_no_punctuation():
    kwargs = {"punctuation": False}
    charset = passgen.generate_valid_characters(**kwargs)
    assert string.punctuation not in charset


def test_generate_password_length():
    charset = passgen.generate_valid_characters()
    assert len(passgen.generate_password(charset, 9)) == 9


def test_generate_password_scandics():
    kwargs = {"scandics": "NODK"}
    charset = passgen.generate_valid_characters(**kwargs)
    passwd = passgen.generate_password(charset, 15)
    found = False
    # Check if any scandic character is in the generated password
    # we should change the function to always include these if requested
    for character in SCANDIC_NO_DK:
        if character in passwd:
            found = character in passwd
            break
        else:
            continue
    assert found
