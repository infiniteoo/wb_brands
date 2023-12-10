def add(x, y):
    return x + y

print(add(1, 2))

add = lambda x, y: x + y
print(add(1, 2))

def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

print(list(squared_numbers))

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda num: num * num, numbers)

print(list(squared_numbers))

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)

print(list(even_numbers))

numbers = [1,2,3,4,5,6]
even_numbers = filter(lambda num: num % 2 == 0, numbers)
print(list(even_numbers))

def get_second_element(item):
    return item[1]

pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=get_second_element)
print(sorted_pairs)

pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda item: item[0])

print(list(sorted_pairs))

def square(num):
    return num * num

numbers = [1,2,3,4,5]
squared_numbers = [square(num) for num in numbers]
print(squared_numbers)

numbers = [1, 2, 3, 4, 5]
squared_numbers = [(lambda num: num * num)(num) for num in numbers]
print(squared_numbers)


numbers = [1, 2, 3, 4, 5]
# Your code here to create a list `cubes` that contains the cubes of the numbers
cubed_numbers = [(lambda num: num * num * num)(num) for num in numbers]

print(cubed_numbers)


celsius = [0, 10, 20, 30, 40]
# Your code here to create a list `fahrenheit` using map and lambda

converted_temps = map(lambda num: (num * 9/5) + 32, numbers)
print(list(converted_temps))

words = ["apple", "it", "creek", "pond", "quiet"]
# Your code here to create a list `long_words` using filter and lambda
filtered_words = filter(lambda word: len(word) > 3, words)
print(list(filtered_words))

scores = [("Anna", 90), ("Bob", 85), ("Carl", 95)]
# Your code here to sort the list `scores` by scores
sorted_scores = sorted(scores, key=lambda score: score[1])
print(list(sorted_scores))


def create_adder():
    return lambda x,y: x+y

adder = create_adder()
result = adder(5,3)
print(result)

numbers = [1,2,3,4,5,6]
list_of_strings = [("even" if num % 2 == 0 else "odd") for num in numbers]
print(list(list_of_strings))

words = ["banana", "apple", "cherry"]
# Your code here to sort `words` by the last character
sorted_by_last_char = sorted(words, key=lambda word: word[-1] )
print(list(sorted_by_last_char))


numbers = [9, 10, 11, 12, 13, 14, 15]
# Your code here to create a list `filtered_numbers`
filtered_numbers = filter(lambda num: num > 10 and num % 2 != 0, numbers)
print(list(filtered_numbers))

from functools import reduce
numbers = [1, 2, 3, 4, 5]
# Your code here to find the product of numbers
result = reduce(lambda x,y: x*y,numbers)
print(result)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in matrix for item in sublist]
print(flattened)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [num * num for num in numbers if num % 2 == 0]
print(even_squares)


