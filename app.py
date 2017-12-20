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
import TimeoutInput as toi

from msvcrt import getch

from datetime import datetime

fetch_type = "r"
#print(speak.AlertBoundary)

event = threading.Event()

len_scripts = 0
origin_processing_file_pathes = []
lines = []

is_start_reading = False

input_word2 = ""
cut_loop = False

is_train = False
is_train = input("if you want to train:input 't'")
is_keyboard = input("if you want to keyboard debug:input 'k'")
username = "no_name"
#if is_train and is_keyboard:
username = input("input username : ")
num = input("input num : ")
f = open(username + str(num) + 'test.txt','a')
f.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f'") + '\n')
print(datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f'"))
f.close()


def speak_scripts_w_osc():
    #speak_line = -1
    lines = setup.read_files(is_train, username, num)
    client = comuWOsc.setup_osc(lines)
    comuWOsc.receive_osc(lines, is_train)

def input_loop():
    global input_word2
    global cut_loop
    count = 0
    while True:
        count += 1
        if count > 100:
            print("count over")
            count = 0
            break
        """input_word_loop = input("thread input >")
        print("in loop:", input_word_loop)
        if input_word_loop in ["r", "u", "d", "w"]:
            input_word2 = input_word_loop
            break"""
        try:
            #input_word2 = toi.win_input_with_timeout("loop:" + str(count), timeout=0.005)
            #cut_loop = input_word2 in ["r", "d", "u", "w"]
            cut_loop = toi.win_input_with_timeout("loop:" + str(count), timeout=0.05) == "s"
            print("loop break", cut_loop, input_word2)
            if cut_loop:
                cut_loop = False
                break
        except TimeoutError:
            pass
    #print("end loop")

def multi():
    print("start threading")
    th = threading.Thread(name="01", target=input_loop, args=())
    th.start()
    return th

def speak_scripts():
    global cut_loop
    global input_word2
    th = None

    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Rate = -3
    speak.Priority = 1 #0, 1, 2
    speak.SynchronousSpeakTimeout = 0
    speak_line = -1
    lines = setup.read_files(is_train, username, num)
    #speak.SpeakCompleteEvent = print_some()
    #print(speak.SpeakCompleteEvent)
    #print(speak.WaitForSingleObject(speak.SpeakCompleteEvent, -1))

    while True:
        #print("input_word2", input_word2 == "")
        if input_word2 == "":
            input_word = input("""
コマンドを選んでください
r->同じ行を繰り返して読む
u->次の行を読み上げる
d->前の行を読み上げる
>""")
        else:
            input_word = input_word2
            input_word2 = ""
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
            if speak_line > 0:
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
        elif len(input_word) > 0 and input_word[0] == "h":
            print(datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f'"))
            f = open(username + str(num) + 'test.txt','a')
            f.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + '\n')
            f.close()
        elif  input_word == "w":
            speak.Skip("SENTENCE", 1)
            if speak_line < len(lines) - 2:
                speak_line += 1

                words = modify.modify(lines[speak_line]).split(" ")
                #input_word2 = ""
                howmanytimes_speak = 0
                howmany_thread = 0
                for word in words:
                    #for cw in modify.change_words:
                    #    if word in cw:
                    #        ws = word.split(cw)
                    speak.Speak(word, 3)
                    while speak.WaitUntilDone(0) == False:
                        is_start_reading = True
                        if howmanytimes_speak == 0 and howmany_thread == 0:
                            th = multi()
                            howmany_thread += 1
                            cut_loop = False
                    else:
                        howmanytimes_speak += 1
                        print(word)
                        if howmanytimes_speak == len(words):
                            print("\007")
                            is_start_reading = False
                            cut_loop = True
                            #event.set()
                            #event.clear()
                            #th.join()

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
