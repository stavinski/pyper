# Pyper

Performs enumeration of named pipes over SMB, I know metasploit as an auxillary module for doing this however some exams (hint, hint!) don't allow use of this framework :)

## Usage

```bash
usage: pyper.py [-h] [-w WORDLIST] [-u USERNAME] [-p PASSWORD] target

positional arguments:
  target                IP address of target

optional arguments:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        wordlist file to use for pipe names
  -u USERNAME, --username USERNAME
                        username to use for authentication, defaults to NULL
  -p PASSWORD, --password PASSWORD
                        password to use for authentication, defaults to NULL
```

## Credits

Uses code from the following repo https://github.com/worawit/MS17-010

## Dependencies

* pysmb
* impacket
