import string
import re
book = open("../book.txt", "r")


# Funtion: identify Roman numbers from words
# Input: String
# Output: String or Empty
def roman_to_int(roman, values={'M': 1000, 'D': 500, 'C': 100, 'L': 50,
                                'X': 10, 'V': 5, 'I': 1}, one = 0):
    word = roman
    """Convert from Roman numerals to an integer."""
    for char in word:
        if not char in values:
            return roman # case when word rather than number

    if (word == "I" and one >3):
        return roman.lower()
    else:
        one = one + 1
    return "" #return emty if Roman Number

# Funtion: clear string from punctuation
# Input: String
# Output: String
def remove_punctuation(word):
    puncList = [".",";",":","!","--","[","]",
                "?","/","\\",",","#",
                "&",")","(","\""] #list of possible punctuations

    #some specific cases to remove punctuation
    if (word[0] == "'" or word[-1] == "'" or word[-2:] == "' " ):
        word = word.replace("'", "")
    for punc in puncList:
        word=word.replace(punc,'')
    return word

#Create dictionary
d = dict()

# split book by lines
for line in book:
    # Remove the leading spaces and newline character
    line = line.strip()

    #exclude empty line from calculation
    if len(line) > 0:
        #split line into words by space among words
        words = line.split(" ")

        #process each word separately
        for word in words:
            # use function remove_punctuation to clear text
            word = remove_punctuation(word)
            # use function roman_to_Int do exclude roman numbers
            word = roman_to_int(word)
            # make lower case
            word = word.lower()
            # case if word is not empty to process futher
            if word !="":
                #adding each word into dictonary and count how often is reapeted each
                if word in d:
                    # Increment count of word by 1
                    d[word] = d[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    d[word] = 1

# end of loop for

#sorting and displaying the result
all_words = 0 #count all unic words
letter = 0 # use for display Dictionary letter on top
counter = 0 # count number of words per each letter from Latin alphabet
alphabet = {"a":"A","b":"B","c":"C","d":"D","e":"E",
            "f":"F","g":"G","h":"H","i":"I","j":"J",
            "k":"K","l":"L","m":"M","n":"N","o":"O","q":"Q",
            "p":"P","r":"R","s":"S","t":"T","u":"U",
            "v":"V","w":"W","x":"X","y":"Y","z":"Z"} # Latin Alpfabet object

#sorting words by alphabet
for key in sorted(d.keys()):
    all_words = all_words + 1 #increment number of words
    time = "time" #use word 'time' in a singular case
    tobe = "was" #use word 'to be' in a singular case
    if letter == 0: #case when no any letter was assigned yet
        letter = alphabet["a"] # assign first letter from alphabet
        print("----------------------")
        print (letter)
        print("----------------------")
        counter = counter + 1 # start count each word per fisrt letter
        if d[key] > 1: #condition when word has repeated multiple times then one
            time="times" #use plural
            tobe = "were" #use plural
        print(counter,")",key, " - ", tobe, " used ", d[key], time)

    elif key[0] != letter.lower(): # case when next letter from Alphabet is starting
        print(key)
        counter = 0 # counter is brought to zero for new incremental
        letter = alphabet[key[0]] #assigning a new letter
        print("----------------------")
        print (letter)
        print("----------------------")
        counter = counter + 1
        if d[key] > 1:
            time="times"
            tobe = "were"
        print(counter,")",key, " - ", tobe, " used ", d[key], time)

    else: # case when there are more than one word per each Letter in a loop
        counter = counter + 1
        if d[key] > 1:
            time="times"
            tobe = "were"
        else:
             time="time"
             tobe = "was"

        print(counter,")",key, " - ", tobe, " used ", d[key], time)


print("----------------------------------------")
print(all_words, " - all words in total")
print("----------------------------------------")
