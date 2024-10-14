# function to add two numbers
def add_numbers(a, b):
    result = a + b
    return result

# function to multiply two numbers
def multiply_numbers(a, b):
    result = a * b
    return result

# function to perform both operations: addition and multiplication
def calculate(a, b):
    sum_result = add_numbers(a, b)
    product_result = multiply_numbers(a, b)

    return {
        'sum' : sum_result,
        'product' : product_result
    } 

x = 5
y = 10

results = calculate(x, y)

print(f"The sum of {x} and {y} is: {results['sum']}")
print(f"The product of {x} and {y} is: {results['product']}")
