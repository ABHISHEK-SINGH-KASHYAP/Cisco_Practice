numbers = input('Enter numbers separated by space: ')
numbers_list = [int(num) for num in numbers.split()]
max_val = max(numbers_list)
min_val = min(numbers_list)
'''
max_value = numbers_list[0]
min_value = numbers_list[0]

for num in numbers_list:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
'''

with open('minmax_data.txt', 'w') as output_file:
    output_file.write(f'Numbers list: {numbers_list}')
    output_file.write(f'Maximum: {max_val}\n')
    output_file.write(f'Minimum: {min_val}\n')

print("Data saved successfully")

with open('minmax_data.txt', 'r') as input_file:
    content = input_file.read()
    print(content)
