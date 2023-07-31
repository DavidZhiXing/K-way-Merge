import random

def generate_phone_numbers(file_path, num_lines):
    with open(file_path, 'w') as file:
        for _ in range(num_lines):
            phone_number = ''.join(random.choices('0123456789', k=8))
            file.write(phone_number + '\n')

generate_phone_numbers('phone_numbers.txt', num_lines=10000000)