names = input("Enter the names separated by spaces:")
names_list = sorted(names.split())
'''
names_list = names.split()

# Bubble Sort
for i in range(len(names_list)):
    for j in range(len(names_list) - i - 1):
        if names_list[j].lower() > names_list[j + 1].lower():
            names_list[j], names_list[j + 1] = names_list[j + 1], names_list[j]'''
names_tuple = tuple(names_list)

with open("names_data.txt", "w") as output_file:
    output_file.write("Sorted list of names:")
    output_file.write(str(names_list))
    output_file.write("Tuple of names:")
    output_file.write(str(names_tuple))

print("Data saved successfully")

print("Reading file:")
with open("names_data.txt", "r") as input_file:
    content = input_file.read()
    print(content)
