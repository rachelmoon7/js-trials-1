"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    evenNums = []

    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)
    
    return evenNums


def get_odd_indices(items):
    result= []

    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])

    return result


def print_as_numbered_list(items):
    i = 0

    for item in items:
        i += 1
        print(f"{i}. {item}")


def get_range(start, stop):
    nums = []
    
    for i in range(start, stop):
        nums.append(i)
    
    return nums


def censor_vowels(word):
    chars = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    for char in word:
        if char in vowels:
            chars.append('*')
        else:
            chars.append(char)
    
    return "".join(chars)


def snake_to_camel(string):
    camel_case = []

    for word in string.split('_'):
        camel_case.append(f"{word[0].upper()}{word[1:]}")
    
    return "".join(camel_case)


def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if len(word) > longest:
            longest = len(word)
    
    return longest


def truncate(string):
    result = []
    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)

    return "".join(result)


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens += 1 
        elif char == ')':
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
    return "".join(compressed)


