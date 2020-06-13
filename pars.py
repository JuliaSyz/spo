import lexems
LISTS=[]
VALUE=[]
def if_right(tokens):
    flag=False
    pos=0
    tags = []
    for token in tokens:
        tags.append(token.type)

    while pos < len(tokens):
        print('-------------------',pos)
        for i in range(pos, len(tokens)):
            print(tokens[i].element, end=' ')
        print()

        flag, pos = exp(tokens,pos,tags)
        if not flag:
            print('error')
            break
    return flag
def exp(tokens,pos,tags):
    print('-------------------exp', pos, tokens[pos].type,tokens[pos].element)
    for i in range(pos, len(tokens)):
        print(tokens[i].element, end=' ')
    print()
    flag='True'
    print(tokens[pos].type == 'ID' and (tokens[pos + 1].type == 'ADD' or tokens[pos + 1].type == 'REMOVE'))
    if (tokens[pos].type == 'ID' or tokens[pos].type == 'ID_LIST') and tokens[pos+1].type == 'R':

        pos+=2
        if tokens[pos].type == 'LIST':
            LISTS.append(tokens[pos-2].element)
            print("LISTS",LISTS)
            flag, tokens[pos] = list_exp(tokens[pos])
            pos+=2
        else:
            VALUE.append(tokens[pos-2].element)
            flag, pos = do_exp(tokens, pos, tags,'SPLIT')
    elif tokens[pos].type == 'ID' and tokens[pos + 1].type == 'INDEX':
        print(tokens[pos].element,tokens[pos].element == 'ID' in LISTS)
        if tokens[pos].element  in LISTS:

            id_list(tokens, pos, tags)
        print('!!!!',len(tokens[pos + 1].element),tokens[pos + 1].element)
        print('*******', tokens[pos].element,tokens[pos+1].element)
    elif tokens[pos].type == 'ID' and (tokens[pos + 1].type == 'ADD' or tokens[pos + 1].type == 'REMOVE'):

        pos+=1
        if tokens[pos-1].element in LISTS:
            print('!', tokens[pos-1].element, tokens[pos].element,LISTS)

            str=tokens[pos].element
            print(str)
            str = lexems.lex(str[tokens[pos].element.index('(')+1:tokens[pos].element.index(')')])
            tokens[pos].element=[tokens[pos].element[:tokens[pos].element.index('(')]]
            for st in str:
                tokens[pos].element.append(st.element)

            print(tokens[pos].element)
            pos+=2
            #print(tokens[pos].element)


        else:
            flag=False




    elif tokens[pos].type == 'H_OP':

        pos+=1
        if 'DO'in tags[pos:]:
            pos_finish = pos + tags[pos:].index('DO')


            if 'COMPAR' in tags[pos:pos_finish] or 'LOG' in tags[pos:pos_finish]:
                print('wwww', pos)
                flag, pos = do_exp(tokens, pos, tags,'DO')
                #pos+=1
                flag, pos = exp(tokens, pos, tags)

                if tokens[pos].type == 'ELSE':
                    pos += 1
                    if tokens[pos].type == 'DO':
                        pos += 1
                        flag, pos = exp(tokens, pos, tags)


                if tokens[pos].type == 'END':
                    pos += 1


    else: flag=False

    return flag,pos

def log_exp(tokens,pos,tags,end):
    print('-------------------log', pos)
    for i in range(pos, len(tokens)):
        print(tokens[i].element, end=' ')
    print()

    flag = True
    if end in tags[pos:]:
        if tags[pos:].count('OP') == tags[pos:].count('CP'):
            while tokens[pos].type != end:
                if (tokens[pos].type==tokens[pos+1].type) or ((tokens[pos].type=='ID' or tokens[pos].type == 'ID_LIST') and tokens[pos+1].type=='DIGIT') and ((tokens[pos+1].type=='ID' or tokens[pos+1].type == 'ID_LIST') and tokens[pos].type=='DIGIT'):
                    flag = False
                    break
                if tokens[pos].type == 'ID':
                    if tokens[pos].element not in VALUE:
                        flag = False
                if tokens[pos + 1].type == 'INDEX':
                    print('!!!!!')
                    if tokens[pos].element  in LISTS:id_list(tokens, pos, tags)
                pos += 1


        else:
            flag = False
    else:
        flag = False
    print(flag)
    return flag, pos
def arif_exp(tokens, pos, tags,end):
    print('-------------------arif', pos)
    for i in range(pos, len(tokens)):
        print(tokens[i].element,end=' ')
    print()
    flag=True
    if end in tags[pos:]:
        if tags[pos:].count('OP')==tags[pos:].count('CP'):

            while tokens[pos].type!=end:
                if tags[pos]!='OP' and tags[pos]!='CP':
                    if (tokens[pos].type==tokens[pos+1].type) or ((tokens[pos].type=='ID' or tokens[pos].type == 'ID_LIST') and tokens[pos+1].type=='DIGIT') and ((tokens[pos+1].type=='ID' or tokens[pos+1].type == 'ID_LIST') and tokens[pos].type=='DIGIT'):

                        print(3,tags[pos])
                        flag=False
                        break
                    if tokens[pos].type=='ID':
                        print(VALUE)
                        if tokens[pos].element not in VALUE:
                            print('!')
                            flag=False
                    if tokens[pos + 1].type == 'INDEX':
                        print('!!!!!')
                        if tokens[pos].element  in LISTS:id_list(tokens, pos, tags)
                pos+=1

        else:flag=False
    else:flag=False
    print(flag)
    return flag,pos

def do_exp(tokens, pos, tags,end):
    print('-------------------do', pos)
    for i in range(pos, len(tokens)):
        print(tokens[i].element, end=' ')
    print()

    if end in tags[pos:]:
        pos_finish = pos+tags[pos:].index(end)
        print(tags[pos:pos_finish],pos_finish)
        if ('COMPAR' in tags[pos:pos_finish] or 'LOG' in tags[pos:pos_finish]) and 'ARIF' not in tags[pos:pos_finish]:

            flag, pos = log_exp(tokens, pos, tags, end)
        elif 'ARIF' in tags[pos:pos_finish] and 'LOG' not in tags[pos:pos_finish]:
            flag, pos = arif_exp(tokens, pos, tags, end)
        elif (tags[pos]=='DIGIT' or tags[pos]=='ID' or tokens[pos].type == 'ID_LIST') and len(tags[pos:pos_finish])==1:
            if tokens[pos+1].type == 'INDEX':
                print('!!!!!')
                if tokens[pos].element in LISTS:id_list(tokens,pos,tags)
            flag=True
            pos+=1

        pos+=1
    else:flag=False
    print(flag)
    return flag, pos
def id_list(tokens,pos,tags):
    print('id_list')
    tokens[pos].element = [tokens[pos].element, tokens[pos + 1].element]

    tokens[pos].type = 'ID_LIST'
    tokens.pop(pos + 1)
    tags.pop(pos + 1)

def list_exp(token):
    flag=True
    str=token.element
    str=lexems.lex(str[1:len(str)-1])
    token.element=str
    print(str)
    #for i in range(1,len(str)-1,2):
        #if str[i]
    return flag,token
