# pyPassgen
This script is used to generate passwords of arbitrary length with varied character sets. The reason for this short script is that most often password managers would require a user to log into their vault to generate a password for new service or user, but that is sometimes not wanted as there might not be any other reason for the login.

## How to use the script
using the script is easy, as you only need to have python3.6+ installed.

To clone the repo, run `git clone https://github.com/Thoogs/pyPassgen.git`

For the most basic use case where we only want a password with ASCII characters and numbers, we can just run

`python3 passgen.py --verbose <length of password>`

if we want to use nordic characters in the generated password, we can simply include the argument `--scandics` with desired country code.
As an example, the following line will generate a password with ASCII characters, numbers, and norwegian/danish characters with total length of 26 characters.

`python3 passgen.py --verbose --scandics NODK 26`

if you want to add punctuation characters to the password, you would add the `--punctuation` argument.

Should you desire to save your passwords to a file for later use, the script uses the `-o`or `--output` arguments.
***the files will be utf-8 encoded.***
`python3 passgen.py --verbose --output passwords.txt 10`

## Notes on security
Personally I do not recommend creating passwords shorter then 8 characters, as modern hardware can crack such short passwords quite quickly. You should in all cases where possible use 2 factor authentication on top of a unique password, preferably with varying usernames between services. Another valuable piece of technology is some kind of password manager, be it software or physical notebook.

## Disclaimer
This script is not and will not replace your own password manager, it simply will generate them. It also falls onto the user to securely store their passwords, as the script will output or save them in plain text.
