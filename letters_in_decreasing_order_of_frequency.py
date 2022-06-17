text = input("enter a string: ")


def make_dict(n):
    dict = {}
    for letter in n:
        dict[letter] = 1 + dict.get(letter, 0)
    return dict
def frequent_decreasing(text):
    letters = [letter.lower() for letter in text if letter.isalpha()]
    dict = make_dict(letters)
    result = []
    for key in dict:
        result.append((dict[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print (letter,"=",count)
frequent_decreasing(text)
