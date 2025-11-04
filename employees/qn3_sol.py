sentence = input("enter the sentence: ")
words_list = sentence.split()
words_tuple = tuple(word.upper() for word in words_list)

with open("sentence_data.txt", "w") as file:
    file.write("list of words:")
    file.write(str(words_list))
    file.write("tuple of words:")
    file.write(str(words_tuple))

print("Data saved successfully")

print("Reading file:")
with open("sentence_data.txt", "r") as file:
    content = file.read()
    print(content)
