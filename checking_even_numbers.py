def check_even_list(num_list):
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# Calling the function
print(check_even_list([2, 5, 6, 3]))

