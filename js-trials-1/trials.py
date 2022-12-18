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
    camel_case = []

    for word in string.split('_'):
        camel_case.append(f'{word[0].upper()}{word[1:]}')

    return ''.join(camel_case)

def longest_word_length(words):
    longest = len(words[0])
    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest


def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)

    return ''.join(result)


def has_balanced_parens(string):
    parens = 0
    for char in string: 
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
            if parens < 0: 
                return False
    return parens == 0

def compress(string):
    compressed = []
    curr_char = ''
    char_count = 0
    
    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0

        char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)
