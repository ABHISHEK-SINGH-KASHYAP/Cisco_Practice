integer_list = input('Integers list (separated by space):')
print(integer_list)
nums = integer_list.split() #' '
print(nums, type(nums))

with open('qn02_data.txt', 'w') as output_file:
    output_file.write(f'list:{nums}\n')

with open('qn02_data.txt', 'r') as input_file:
    file_nums_list_line = input_file.readline()
    print(file_nums_list_line)
    def find_sum(first, second, *others):
        '''
        find_sum takes arguments and returns sum of the two or many positiona arguments numbers
        '''
        add_result = first + second
        for num in others:
            add_result += num

        return add_result
    def find_average(first, second, *others):
        '''
        find_average takes arguments and returns average of the two or many positiona arguments numbers
        '''
        total_numbers = 2 + len(others)
        sum_result = find_sum(first, second, *others)
        average_result = sum_result / total_numbers
        return average_result

addd_result = find_sum(int(nums[0]), int(nums[1]), *(int(num) for num in nums[2:]))
avg_result = find_average(int(nums[0]), int(nums[1]), *(int(num) for num in nums[2:]))
    
with open('numbers_data.txt','w') as output_file:
    output_file.write(f'Sum: {addd_result}\n')
    output_file.write(f'Average: {avg_result}\n')

with open('numbers_data.txt','r') as input_file:
    file_sum_line = input_file.readline()
    file_average_line = input_file.readline()
    print(file_sum_line)
    print(file_average_line)

# --- IGNORE ---
'''
num_spe_by_space = input('Numbers separated by space:')
num_str_list = num_spe_by_space.split()
nums = []

for num_str in num_str_list:
    num = int(num_str)
    nums.append(num)
print(nums, type(nums))

result = 0
for num in nums:
    result += num

avg = result / len(nums)

with open('numbers_data.txt', 'w') as output_file:
    output_file.write(f'numbers list: {nums}\n')
    output_file.write(f'sum: {result}\n')
    output_file.write(f'average: {avg}\n')
    '''

'''
# beginning 
num_sep_by_space = input('Numbers (Space separated):') # '10 20 30'
num_str_list = num_sep_by_space.split() #['10', '20', '30']
nums = []
for num_str in num_str_list:
    num = int(num_str)
    nums.append(num)
print(nums) # [10, 20, 30]

total = 0
for num in nums:
    total += num 
# end beginning 
'''
'''
# easy
nums = [int(num_str) for num_str in input('Numbers (Space separated):').split()]
total = sum(nums)
# end easy 

avg = total / len(nums) # 60 / 3 = 20

print(f'sum:{total}')
print(f'average:{avg}')

print('To/From file...')

with open('numbers_data.txt', 'w') as out_file:
    out_file.write(f'numbers list: {nums}\n')
    out_file.write(f'sum: {total}\n')
    out_file.write(f'average: {avg}\n')

with open('numbers_data.txt', 'r') as in_file:
    line1 = in_file.readline()
    line2 = in_file.readline()
    line3 = in_file.readline()
    print(line1, end='')
    print(line2, end='')
    print(line3, end='')
'''