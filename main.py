import lexems
from pars import *
import polish


if __name__ == '__main__':
    file = open("test.txt")
    text = file.read()
    file.close()
    tokens = lexems.lex(text)
    for token in tokens:
        print(token.element,token.type)

    flag = if_right(tokens)

    if flag:
        print('true')
        polish.polish(tokens)
