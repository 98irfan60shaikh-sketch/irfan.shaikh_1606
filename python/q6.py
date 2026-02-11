ch = input("Enter a character: ")

if ch.isdigit():
    print("It's a digit")
elif ch.lower() in "aeiou":
    print("It's a vowel")
elif ch.isalpha():
    print("It's a consonant")
else:
    print("It's a special symbol")