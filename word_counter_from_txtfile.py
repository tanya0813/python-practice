word=input("Enter the word: ")

with open("Text_file.txt") as f:
    content=f.read().lower()

#To count the occurence of the word
count = content.split().count(word.lower()) #Splits the text into a list of words.
                                            #.count() to find how many times the input word appears.
if(f'{word} in {content}'):
    print (f'The occurence of {word} in text file is: {count}')