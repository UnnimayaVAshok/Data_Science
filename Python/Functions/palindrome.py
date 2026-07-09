def palindrome(text):
    new = ""
    new = text[::-1]
    print("Palindrome" if text == new else "Not palindrome")

palindrome("madam")