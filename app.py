import win32com.client as wincl
import glob
import os
import random
import threading
import sys

import modify

speak = wincl.Dispatch("SAPI.SpVoice")
speak.Rate = 1
#fetch_type = input("all(a), random(r), a file(filename)")
fetch_type = "r"

len_scripts = 0
origin_processing_file_pathes = []
lines = []

go_up = {
    "up":False,
    "down":False,
    "speak_line":-1
}

def read_files():
    all_origin_processing_file_pathes = glob.glob('data/change/Blink/*.ino')

    if fetch_type == "r":
        n_ran = random.randint(0,len(all_origin_processing_file_pathes))
        if n_ran == len(all_origin_processing_file_pathes):
            n_ran = 0
        origin_processing_file_pathes = [all_origin_processing_file_pathes[n_ran]]

    for p in origin_processing_file_pathes:
        f = open(p)
        lines = f.readlines()
        f.close()

    return lines

def speak_scripts():
    lines = read_files()

    while True:
        input_word = input(">")
        if input_word == "u":
            go_up["up"] = True
            if go_up["speak_line"] < len(lines) - 1:
                go_up["speak_line"] += 1
                speak.Speak(modify.modify(lines[go_up["speak_line"]]))
        elif input_word == "d":
            go_up["down"] = True
            if go_up["speak_line"] > 1:
                go_up["speak_line"] -= 1
                speak.Speak(modify.modify(lines[go_up["speak_line"]]))
        elif input_word in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            speak.Rate = int(input_word)

if __name__ == '__main__':
    speak_scripts()
