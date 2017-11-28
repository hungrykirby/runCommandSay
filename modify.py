def modify(line):
    if line == "\n" or line == " " or line == " ":
        line = "no word"
    if len(line) > 2 and line[0:2] == "//":
        line = "this line is comment"

    change_words = {
        ";": "semicolon",
        ":": "colon",
        "-": "minus",
        ",": "comma",
        ".": "period",
        #"(": "left parenthesis",
        "(": " ",
        #")": "right parenthesis",
        ")": " ",
        #"{": "left Brace",
        "{": " ",
        #"}": "right Brace",
        "}": " ",
        "<": "less than",
        ">": "greater than"
    }
    for k in change_words:
        line = line.replace(k, "   " + change_words[k] + "   ")
    return line
