chosen_word = "raise"
tf = "20120"
first = False
words = ""

def not_same_letter(word):
    char = [char for char in word]
    return len(char) == len(set(char))

if first:
    with open("words.txt", "r") as f:
        words = f.read().splitlines()
else:
    with open("bruh.txt", "r") as f:
        words = f.read().splitlines()
    for word in words:
        if not_same_letter(word):
            chosen_word = word
            break

letters = [
    {
        "char": None, 
        "correct_letter": None,
        "correct_index": None, 
        "index": 0
    }, 
    {
        "char": None, 
        "correct_letter": None,
        "correct_index": None, 
        "index": 1
    }, 
    {
        "char": None, 
        "correct_letter": None,
        "correct_index": None, 
        "index": 2
    },
    {
        "char": None, 
        "correct_letter": None,
        "correct_index": None, 
        "index": 3
    },
    {
        "char": None, 
        "correct_letter": None,
        "correct_index": None, 
        "index": 4
    },
]
char = [char for char in chosen_word]
for i in range(len(char)):
    letters[i]["char"] = char[i]

n = [n for n in tf]
for i in range(len(n)):
    if n[i] == "0":
        letters[i]["correct_letter"] = False
    elif n[i] == "1":
        letters[i]["correct_letter"] = True
        letters[i]["correct_index"] = False
    elif n[i] == "2":
        letters[i]["correct_letter"] = True
        letters[i]["correct_index"] = True

lst = []
for word in words:
    lst.append(word)

for word in words:
    for letter in letters:
        if letter["correct_letter"]:
            if letter["char"] not in word:
                lst.remove(word)
                break

            if letter["correct_index"]:
                if letter["char"] not in word[letter["index"]]:
                    lst.remove(word)
                    break
            else:
                if letter["char"] in word[letter["index"]]:
                    lst.remove(word)
                    break
        else:
            if letter["char"] in word:
                lst.remove(word)
                break

textfile = open("bruh.txt", "w")
for element in lst:
    textfile.write(element + "\n")
textfile.close()

if len(lst) < 20:
    print("Word List:")
    print(lst)
    for word in lst:
        if not_same_letter(word):
            print("New Chosen Word: " + word)
            break
else:
    for word in lst:
        if not_same_letter(word):
            print("New Chosen Word: " + word)
            break