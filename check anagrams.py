x = input("First word: ")
y = input("Second word: ")

def split(word):
    return list(word)

list_x = split(x)
list_y = split(y)

if len(list_x) is not len(list_y):
    print(f'{x} and {y} are not arnagrams.')
    exit()

if set(list_x) == set(list_y):
    print(f'{x} and {y} are anagrams.')
    
