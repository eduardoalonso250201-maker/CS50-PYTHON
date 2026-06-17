'''Emojize
In this example we install emoji library (pip install emoji)
and use it to convert text to emojis. For example, if the user inputs "I :heart: Python", the output will be "I ❤️ Python". The emoji library uses a specific syntax for emojis, where you can use colons to denote an emoji name. The 'alias' language option allows us to use common emoji names as aliases.'''

import emoji

def main():
    request = input("Input: ")
    print(f"Output: {emoji_f(request)}") #we print with format and call the function emoji_f  

def emoji_f(g): #This function recieves the input wich contain the text and the emoji name
    return emoji.emojize(g, language='alias') #we return the string with the emoji converted thanks to the function emojize, 
#check the arguments, language='alias' allows us read not only the emoju name with "_", but also the common name without "_"


main()


