# '''Create a fibonacci sequence of the value of 200, multiply by the 5th number, and divide by 2'''

# # Function to generate a Fibonacci sequence up to a given value
# def generate_fibonacci(n):
#     fibonacci_sequence = [0, 1]
#     while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
#         next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
#         fibonacci_sequence.append(next_number)
#     return fibonacci_sequence

# # Calculate the Fibonacci sequence up to 200
# value_limit = 200
# fibonacci_sequence = generate_fibonacci(value_limit)

# # Multiply the 5th number by 3 (0-based index)
# fifth_number = fibonacci_sequence[4]
# result = (fifth_number * 3) / 2

# print("Fibonacci Sequence:", fibonacci_sequence)
# print("5th number (0-based index):", fifth_number)
# print("Result:", result)

# def fibonacci_sequence(n):
#     sequence = [0, 1]
#     for i in range(2, n):
#         next_number = sequence[i - 1] + sequence[i - 2]
#         sequence.append(next_number)
#     return sequence
    
# # print(f'{fibonacci_sequence(200)} \n')

# fib_sequence = fibonacci_sequence(5)
# last_value = fib_sequence[-1]
# result = (last_value *5 )/2

# print(f'Fibonacci sequence: {fib_sequence}')
# print(f'Last valueb* 5/2 = {result}')

name = 'hello'
