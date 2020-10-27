"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
 
    # function outputAllItems(items) {
    #   for (const item of items) {
    #     console.log(item);
    #   }
    # }
    for item in items:
        print(item)
        
def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num%2 == 0:
            even_nums.append(num)

    return even_nums

    # TODO: replace this line with your code


def get_odd_indices(items):

    result = []

    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])
    return result
    
def print_as_numbered_list(items):
#     function printAsNumberedList(items) {
#   let i = 1;

#   for (const item of items) {
#     console.log(`${i}. ${item}`);

#     i += 1;
#   }
# }
    i = 1
    for item in items:
        print (f'{i}. {item}')
        i +=1


def get_range(start, stop):
#     function getRange(start, stop) {
#   const nums = [];

#   for (let num = start; num < stop; num += 1) {
#     nums.push(num);
#   }
# }
# def get_range(start, stop):
    nums = []

    for num in range(start, stop):
        nums.append(num)

    return nums



def censor_vowels(word):
#     function censorVowels(word) {
#   const chars = [];

#   for (const letter of word) {
#     if ('aeiou'.includes(letter)) {
#       chars.push('*');
#     }
#     chars.push(letter);
#   }

#   return chars.join('');
# }
    chars=[]
    vowels = ['a' , 'e', 'i', 'o', 'u']
    for letter in word:
        if letter in vowels:
            chars.append('*')
        else:
            chars.append(letter)
    return ' '.join(chars)
            



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
