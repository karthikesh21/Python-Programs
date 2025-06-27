def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

# Input
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Output
if is_anagram(s1, s2):
    print("Anagram")
else:
    print("Not an Anagram")
