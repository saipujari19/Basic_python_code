#saiprasad Pujari
"""a function that accepts two text strings of equal length and returns the Hamming distance between them;
that is the number of corresponding characters or symbols that differ in the two strings"""
def hamming_distance(str1, str2):
    # calculating and returning the hamming distance between two strings.
    if len(str1) != len(str2):
        return None
    return sum(1 for i, ch in enumerate(str1) if ch != str2[i])
def main():
    # Prompt the user to enter two strings
    string1 = input("enter the first string: ")#input from the user
    string2 = input("enter the second string: ")#input from the user
# calculating the hamming distance
    distance = hamming_distance(string1, string2)
    if distance is None:
        print("error: Strings are not of equal length.")
    else:
        print(f"the hamming distance between the strings is: {distance}")
if __name__ == "__main__":
    main()


