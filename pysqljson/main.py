from pysqljson import Parser

parser = Parser.Parser()
parser.parse('{"&&": 2}', ['c', 'e'])

def print_hi(name):
    print('Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
