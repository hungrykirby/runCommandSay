def modify(line):
    if line == "\n":
        line = "no word"

    change_words = {
        ";": "semicolon",
        ":": "colon",
        "(": "kakko left parenthesis",
        ")": "kakko right parenthesis",
        "{": "dai kakko left Brace",
        "}": "dai kakko right Brace",
        "<": "under",
        ">": "over"
    }
    for k in change_words:
        #print(k)
        line = line.replace(k, change_words[k])
        #print(k, change_words[k])
    return line
