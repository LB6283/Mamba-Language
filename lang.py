def out(*args, **kwargs):
    for arg in args:
        if args.index(arg) < len(args) - 1:
            print(arg, end=kwargs.get('spaceing', ''))
        elif args.index(arg) == len(args) - 1 and kwargs.get('endspace') == False:
            print(arg, end=kwargs.get('end_spaceing', ''))
        else:
            print(arg, end=kwargs.get('spaceing', ''))
    print(kwargs.get('end', '\n'))


def accept(*args, **kwargs):
    for arg in args:
        if args.index(arg) < len(args) - 1:
            print(arg, end=kwargs.get('spaceing', ''))
        elif args.index(arg) == len(args) - 1 and kwargs.get('endspace') == False:
            print(arg, end=kwargs.get('end_spaceing', ''))
        else:
            print(arg, end=kwargs.get('spaceing', ''))
    print(end=kwargs.get('cursor_position', ''))
    y = input()
    return y
    
def length(x):
    return len(x)

def final_index(x):
    return (len(x) - 1)
def last_item(x):
    item = x[final_index(x)]
    return item
def n_to_last(x, n):
    item = x[final_index(x) - n]

# Test

fruits = ['apple', 'banana', 'pineapple', 'orange', 'blueberry']
print(n_to_last(fruits, 6))