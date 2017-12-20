import msvcrt
import time

DEFAULT_TIMEOUT = 30.0

class TimeoutOccurred(RuntimeError):
    pass

def win_print(line=None, end='\r\n'):
    if line is not None:
        for c in line:
            msvcrt.putwch(c)

    for c in end:
        msvcrt.putwch(c)

def win_clean_up_line(length):
    win_print('\r' + ' '*length, end='\r')

def win_input_with_timeout(prompt='', timeout=DEFAULT_TIMEOUT):
    end = time.monotonic() + timeout
    win_print(prompt, end='')

    line = ''
    while time.monotonic() < end:
        if msvcrt.kbhit():
            c =  msvcrt.getwch()

            if c.isalnum():
                line += c
            elif c == '\r' or c == '\n':
                win_print()
                return line
            elif c == '\b':
                line = line[:-1]
            elif c == '\x1a':
                win_print(r'^Z')
                raise EOFError

            win_clean_up_line(len(prompt) + len(line) + 1)
            win_print(prompt + line, end='')

        time.sleep(0.005)

    win_print()
    raise TimeoutError
