import lexer


token_patt = [
    (r'[ \n\t]+',              None),
    (r'#[^\n]*',               None),
    (r',',                     None),
    (r'\=',                    'R'),
    (r'\(',                    'OP'),
    (r'\)',                    'CP'),
    (r';',                     'SPLIT'),
    (r'\+|-|\*|/',             'ARIF'),
    (r'<=|<|>=|>|!=|==',       'COMPAR'),
    (r'and|or|not',            'LOG'),
    (r'if|while',               'H_OP'),
    (r':',                     'DO'),
    (r'\[.]',                     'INDEX'),
    (r'\[.*]',                     'LIST'),
    (r'else',                  'ELSE'),
    (r'.remove\(.\)',                  'REMOVE'),
    (r'.add\(.*\)',                  'ADD'),
    (r'end',                   'END'),
    (r'0|([1-9][0-9]*)',         'DIGIT'),
    (r'[A-Za-z][A-Za-z0-9_]*', 'ID'),

]

def lex(text):
    return lexer.find_tokens(text, token_patt)