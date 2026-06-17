def main():
    word = input("Input: ") #we ask the user to input a word and we store it in the variable "word"
    print("output: ", end="") #we print this line just to give format to the next output
    delete_vocals(word) #we call the function "delete_vocals" taking the word as an argument


def delete_vocals(word):
    vocals = "aeiouAEIOU" #we create a string with all the vocals, both lowercase and uppercase
    for w in word: #as a list, we will iterate for each letter of the string "word" and we will store each letter in the variable "w"
        if w in vocals: #if the value of w is in the string "vocals" we will print an empty string, so it will be like if we are deleting the vocal
            print("", end="")#as we said, we print an empty str and we use end="" to avoid that the next print statement goes to the next line, 
        else:
            print(w, end="")#if w is not on the string vocals we print the value of w and we use end="" to avoid "n/" in the output

main()