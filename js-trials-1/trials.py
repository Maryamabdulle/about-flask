"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)
    pass 

def get_all_evens(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens

def get_odd_indices(items):
    odd_idx = []
    for i in range(len(items)):
        if items % 2 != 0:
            odd_idx.append(items[i])
    return odd_idx



def print_as_numbered_list(items):

    i = 1

    for item in items:
        print(f'{i}.{item}')
        i += 1


def get_range(start, stop):
     
    nums= []
    for num in range (start, stop):
        nums.append(num)
    return nums

def censor_vowels(word):
    pass  # TODO: replace this line with your code
    chars= []
    for char in word:
        if char in "aeiou":
            chars.append("*")
        else:
            chars.append(char)
    return " ".join(chars)
    
    

def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
