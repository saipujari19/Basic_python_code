#Saiprasad Pujari
"""program that asks the user to enter a string and should display the length of string,
capitalize all the vowels and display the modified string and
convert the string into list of words and display the length of the list."""
def main():
    user_input = input("enter a string: ")
    print("length of the string:", len(user_input))#display the length of string.
    def capitalize_vowels(string):
        vowels = "aeiou"
        modified_string = ""
        for char in string:
            if char in vowels:
                modified_string += char.upper()
            else:
                modified_string += char
        return modified_string
    modified_string = capitalize_vowels(user_input)#capitalize all the vowels and display the modified string.
    print("modified string with capitalized vowels:", modified_string)
    words_list = user_input.split()#convert the string into list of words and display the length of the list.
    print("length of list of words:", len(words_list))


if __name__ == "__main__":
    main()







