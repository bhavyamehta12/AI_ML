def process_numbers(numbers):
    # Filter OUT numbers that are multiples of 5 (keep where x % 5 != 0)
    filtered_numbers = list(filter(lambda x: x % 5 != 0, numbers))
    
    # Filter even and odd numbers from the remaining set
    even_numbers = list(filter(lambda x: x % 2 == 0, filtered_numbers))
    odd_numbers = list(filter(lambda x: x % 2 != 0, filtered_numbers))
    
    # Return dictionary with exact required keys: "even" and "odd"
    dic = {"even": len(even_numbers), "odd": len(odd_numbers)}
    return dic

numbers = [2, 3, 5, 1, 3, 10, 80]
res = process_numbers(numbers)
print(res)