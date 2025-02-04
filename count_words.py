def count_words(string):
    # Split the string by spaces and filter out empty strings
    words = string.split()
    return len(words)

string = input("Enter a string: ")

word_count = count_words(string)
print("Number of words in the string:", word_count)
