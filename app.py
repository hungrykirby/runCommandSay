import win32com.client as wincl
import glob
import os
import random
import threading
import sys
from time import sleep

import modify
import comuWOsc
import setup

from msvcrt import getch

fetch_type = "r"
#print(speak.AlertBoundary)

len_scripts = 0
origin_processing_file_pathes = []
lines = []

is_train = False
is_train = input("if you want to train:input 't'")
is_keyboard = input("if you want to keyboard debug:input 'k'")

def speak_scripts_w_osc():
    #speak_line = -1
    lines = setup.read_files(is_train)
    client = comuWOsc.setup_osc(lines)
    comuWOsc.receive_osc(lines, is_train)

def speak_scripts():
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Rate = -3
    speak.Priority = 1 #0, 1, 2
    speak_line = -1
    lines = setup.read_files(is_train)

    while True:
        input_word = input("""
コマンドを選んでください
r->同じ行を繰り返して読む
u->次の行を読み上げる
d->前の行を読み上げる
>""")
        #if len(input_word) > 1:
        #    input_word = input_word[0]
        if len(input_word) > 0 and input_word[0] == "u":
            speak.Skip("SENTENCE", 1)
            #speak.Pause()
            if speak_line < len(lines) - 1:
                speak_line += 1

                if is_train == "t":
                    print(lines[speak_line])
                speak.Speak(modify.modify(lines[speak_line]), 3)
        elif len(input_word) > 0 and input_word[0] == "d":
            speak.Skip("SENTENCE", 1)
            if speak_line > 1:
                speak_line -= 1

                if is_train == "t":
                    print(lines[speak_line])

                speak.Speak(modify.modify(lines[speak_line]), 3)
        elif len(input_word) > 0 and input_word[0] == "r":
            speak.Skip("SENTENCE", 1)
            if 0 <= speak_line and speak_line < len(lines) - 1:

                if is_train == "t":
                    print(lines[speak_line])

                speak.Speak(modify.modify(lines[speak_line]), 3)

        elif  input_word == "w":
            speak.Pause()
            speak.Skip("SENTENCE", 1)
            speak.Resume()
            if speak_line < len(lines) - 2:
                speak_line += 1

                words = lines[speak_line].split(" ")
                for w in words:
                    speak.Speak(modify.modify(w), 1)
                    print(w)

        elif input_word == "s":
            sys.exit()

        elif input_word == "a":
            speak.Rate += 1
        elif input_word == "m":
            speak.Rate -= 1

        elif input_word in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            speak.Rate = int(input_word) - 6
        else:
            print(input_word)
        #print(speak.Rate)

if __name__ == '__main__':
    if is_keyboard == "k":
        speak_scripts()
    else:
        speak_scripts_w_osc()
