__author__ = 'Valeria'

symbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def to_base_10(number, old_base):
    error = False
    result = 0
    figures = []
    number = str(number)
    number.lower()
    for k in number:
        i = symbol.index(k)
        if i >= old_base:
            error = True
        figures.append(i)
    for k in range(len(figures)):
        result += (figures[k]) * old_base**(len(figures)-k-1)
    result = str(result)
    if error:
        raise Exception('Not valid number')
    else:
        return result

def from_base_10(number, new_base):
    values = []
    try:
        number = int(number)
    except:
        raise Exception('Not valid number')
    while number > 0:
        remainder = number % new_base
        values.append(remainder)
        number = number/new_base
    result = ''
    for i in range(len(values)):
        result += symbol[values[len(values)-1-i]]
    return result

def cast(number, old_base, new_base):
    if old_base != 10:
        number = to_base_10(number, old_base)
    if new_base != 10:
        number = from_base_10(number, new_base)
    return number


class Converter:
    def __init__(self, old_base, new_base):
        self.old_base = old_base
        self.new_base = new_base
    def convert(self, number):
        result = cast(number, self.old_base, self.new_base)
        return result