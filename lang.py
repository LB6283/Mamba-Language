def out(*args, **kwargs):
    for arg in args:
        if args.index(arg) < len(args) - 1:
            print(arg, end=kwargs.get('spaceing', ''))
        elif args.index(arg) == len(args) - 1 and kwargs.get('endspace') == False:
            print(arg, end=kwargs.get('end_spaceing', ''))
        else:
            print(arg, end=kwargs.get('spaceing', ''))
    print(end=kwargs.get('end', '\n'))


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
    counter = 0
    for y in x:
        counter += 1
    return counter

def final_index(x):
    return (length(x) - 1)
def last_item(x):
    item = x[final_index(x)]
    return item
def rev_index(x, n):
    item = x[final_index(x) - n]
    return item

def sum(*args):
    result = Num(0)
    for arg in args:
        result += arg
    return result

def diff(*args):
    result = 0
    for arg in args:
        result -= arg
    return result

def product(*args):
    result = 0
    for arg in args:
        result *= arg
    return result

def quot(*args):
    result = 0
    for arg in args:
        result /= arg
    return result






############################################################################################################################################
################################################################## CLASSES: ################################################################
############################################################################################################################################





class List:
    def __init__(self, listofvalues):
        self.listofvalues = listofvalues
    
    def make_list(self):
        return self.listofvalues;
    
    def length(self):
        return len(self.make_list())
    
    def values(self):
        items = self.listofvalues
        def recursive(x):
            entries = []
            for item in x:
                if isinstance(item, (str, bool, int, float)):
                    entries.append(item)
                elif isinstance(item, (dict, list, set, tuple)): 
                    entries.extend(recursive(item))
            return entries
        return recursive(items)
    
    def __str__(self):
        return f"List({self.make_list()})"


# DATA TYPES:


class String:
    def __init__(self, string):
        if not isinstance(string, str):
            raise ValueError (f"Could not interpret {type(string)} as <class 'String'>")
        else:
            self.string = string

    def __str__(self):
        return self.make_string()
    
    def make_string(self):
        return self.string


class Num:
    def __init__(self, num):
        if not isinstance(num, (int, float)):
            raise ValueError (f"Could not interpret {type(num)} as <class 'Num'>")
        else:    
            self.num = num
    
    def __str__(self):
        return f"{self.number()}"

    def __add__(self, other):
        return Num(self.number() + other.number())

    def number(self):
        return self.num

## Variable declaration in mamba:

class Var:
    def __init__(self):
        self.vars = {}
    def declare(self, name, value):
        self.vars[name] = value
    def fetch(self, index):
        return self.vars[index]


variables = Var()
