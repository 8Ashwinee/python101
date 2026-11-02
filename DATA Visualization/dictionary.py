from PyDictionary import PyDictionary

dictionary = PyDictionary()


def check_meaning(word):         # if user want to check meaning of word
    return dictionary.meaning(word)

def get_antonym(word):         # if user want to check antonym of word
    return dictionary.antonym(word)

def get_synonym(word):         # if user want to check synonym of word
    return dictionary.synonym(word)

def translate(word,language):     # if user want to translate word into other language
    return dictionary.translate(word,language)



def menu():
    print('''
----------------------------------------------
Enter 1 to check meaning of word
Enter 2 to get antonyms of word
Enter 3 to get synonyms of word
Enter 4 to translate word to other language
Enter 0 to the close dictionary
''')

    choice = int(input("Enter your choice: "))

    return choice


while(True):
    word = input("\nEnter a word: ")
    user_choice = menu()
    match user_choice:
        case 0:
            print("Dictionary is closed")
            exit(0)
        case 1:
            meaning = check_meaning(word)
            print(meaning)
        case 2:
            antonym = get_antonym(word)
            print(antonym)
        case 3:
            synonym = get_synonym(word)
            print(synonym)
        case 4:
            print('''Enter a language code in which you want to translate word
Like for URDU language code is ur
For ARABIC language code is ar
For HINDI language code is hi
''')

            lang_choice = input("Enter your choice: ")
            trans = translate(word, lang_choice)
            print(trans)
        case _:
            print("Invalid choice!")


