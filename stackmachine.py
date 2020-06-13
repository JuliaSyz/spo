import operator
import lexems

LISTS = {}
VALUE={}
def stackmachine(string):
    pos=0
    pos_start=0
    pos_finish=0
    stack = []
    tags=[]
    for st in string:
        tags.append(st.type)
    while pos<len(string):
        print()
        print('victionary_start', VALUE)
        print(string[pos].element,string[pos].type)
        if string[pos].type=="R":
            stack+=arif_calc(string[pos_start+1:pos])
            if string[pos_start].type == 'ID_LIST':
                el=string[pos_start].element


                LISTS[el[0]][int(el[1][1])]=lexems.lex(stack[-1].element)[0]
                print('LIST',LISTS)
            else: VALUE.update({string[pos_start].element:stack[-1].element})

        elif (string[pos].type == 'ID' or string[pos].type=='ID_LIST' ) and (string[pos+1].type=='ADD' or string[pos+1].type=='REMOVE'):
            el=string[pos].element
            pos+=1
            if int(string[pos].element[-1])<len(LISTS[el]):
                if string[pos].type=='ADD':
                    if len(string[pos].element)-1==2:
                        new_list = lexems.lex(string[pos].element[1])[0]
                        LISTS[el].insert(int(string[pos].element[-1]),new_list)
                    elif len(string[pos].element)-1==1:
                        new_list=lexems.lex(string[pos].element[1])[0]
                        LISTS[el].append(new_list)
                elif string[pos].type == 'REMOVE':

                    LISTS[el].pop(int(string[pos].element[-1]))
                else:
                    print('error')
                    break
        elif (string[pos].type=='ID' or string[pos].type == 'ID_LIST') and string[pos+2].type=='R' and string[pos+1].type=='DIGIT':
            #print(string[pos])
            if string[pos].type == 'ID_LIST':
                el=string[pos].element


                LISTS[el[0]][int(el[1][1])]=string[pos+1]
                print('LIST',LISTS)
            else: VALUE.update({string[pos].element:string[pos+1].element})
            pos+=2
            print('victionary',VALUE)

        elif string[pos].type=='ID' and string[pos+2].type=='R' and string[pos+1].type=='LIST':
            linkList=[]
            for el in string[pos+1].element:

                linkList.append(el)
            print('linkList',linkList)
            LISTS.update({string[pos].element:linkList})
            pos+=2
            print('list',LISTS)
        elif (string[pos].type=='ID' or string[pos].type == 'ID_LIST') and (string[pos-1].type == 'SPLIT' or string[pos-1].type == 'FLAG'):
            pos_start=pos
            print('elif2')
        elif string[pos].type=='FLAG' and string[pos].element!=-1:

            if string[pos-1].type=='SPLIT':

                pos+=string[pos].element-1
                pos_start=pos
                if pos>len(string):
                    break
            elif string[pos-1].type=='LOG' or string[pos-1].type=='COMPAR':
                #print(string[pos].element,string[pos].type,int(log_calc(string[pos_start:pos])[0].element)==0)
                if int(log_calc(string[pos_start:pos])[0].element)==0:
                    pos+=string[pos].element-1
            elif string[pos].type=='FLAG' and string[pos].element<-1:
                pos += string[pos].element-1
        pos+=1
        for s in stack:
            print(s.element, s.type, end=', ')
        #print(string[pos].element,string[pos].type)

    for s in stack:
        print(s.element, s.type, end=', ')

    print("stack")
    print()
    keys=VALUE.keys()

    for el in keys:
        print(el,' = ',VALUE[el])
    print()
    keys = LISTS.keys()
    for el in keys:
        print(el, ' = ',end='')
        for element_list in LISTS[el]:

            print(element_list.element,end=', ')








def arif_calc(string):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    pos=0
    stack=[]
    print("apif")
    for s in string:
        print(s.element, s.type, end=', ')
    print()
    for token in string:
        #print(1,token,stack)

        if token.type == 'ARIF':

            op2, op1 = stack.pop(), stack.pop()
            print(op1.element,op2.element)
            if op1.type=='ID':
                op1=(lexems.lex(VALUE[str(op1.element)])[0])
            elif op1.type=='ID_LIST':
                el = op1.element

                op1=(lexems.lex(LISTS[el[0]][int(el[1][1])].element)[0])

            if op2.type=='ID':
                #print("              ",op2)
                op2=(lexems.lex(VALUE[str(op2.element)])[0])
            elif op2.type == 'ID_LIST':
                el = op2.element
                print("  ", LISTS[el[0]][int(el[1][1])].element)
                op2 = (lexems.lex(LISTS[el[0]][int(el[1][1])].element)[0])

            print(op1.element, op2.element, token.element)
            op = str(OPERATORS[token.element](int(op1.element),int(op2.element)))
            print("op",op,lexems.lex(op)[0].type)
            stack.append(lexems.lex(op)[0])

        else:
            stack.append(token)
            print('stack')
            for s in stack:
                print(s.element, s.type, end=', ')
            print()
    return stack

def log_calc(string):
    OPERATORS = {'and': operator.and_, 'or': operator.or_, 'not': operator.not_,'>=': operator.ge, '>': operator.gt, '<': operator.lt,'<=':operator.le, '==':operator.eq, '!=':operator.ne}
    pos = 0
    stack=[]
    print("log_arif")
    for token in string:
        # print(1,token,stack)

        if token.type == 'LOG' or token.type == 'COMPAR':

            op2, op1 = stack.pop(), stack.pop()
            print(op1.element, op2.element)
            if op1.type == 'ID':
                op1 = (lexems.lex(VALUE[str(op1.element)])[0])
            elif op1.type == 'ID_LIST':
                el = op1.element

                op1 = (lexems.lex(LISTS[el[0]][int(el[1][1])].element)[0])

            if op2.type == 'ID':
                # print("              ",op2)
                op2 = (lexems.lex(VALUE[str(op2.element)])[0])
            elif op2.type == 'ID_LIST':
                el = op2.element
                print("  ", LISTS[el[0]][int(el[1][1])].element)
                op2 = (lexems.lex(LISTS[el[0]][int(el[1][1])].element)[0])

            print(op1.element, op2.element, token.element)
            op = str(int(OPERATORS[token.element](int(op1.element), int(op2.element))))
            print("op", op, lexems.lex(op)[0].type)
            stack.append(lexems.lex(op)[0])

        else:
            stack.append(token)
            print('stack')
            for s in stack:
                print(s.element, s.type, end=', ')
            print()
    return stack
