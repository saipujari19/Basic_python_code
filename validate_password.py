#Saiprasad Pujari
"""program prompts for a password & checks with the certain criteria for security, prompts again if it does not meet """
def validate_password(password):
    if len(password) < 8: #checking if the entered password is eight character long or not
        return False
    has_uppercase = False #initializing flags to check for uppercase lowercase and digit
    has_lowercase = False
    has_digit = False
    for char in password:
        if char.isupper(): #checking if the character is upper
            has_uppercase = True
        elif char.islower(): #checking if the character is lower
            has_lowercase = True
        elif char.isdigit(): #checking if the character is digit
            has_digit = True
    return all([has_uppercase, has_lowercase, has_digit]) #returning all
def main():
    while True:
# prompting the user for a password
        user_password = input("enter a password: ")
# validating the password
        if validate_password(user_password):
            print("password is valid.")
            break
        else:
            print("invalid password, try again")
if __name__ == "__main__":
    main()