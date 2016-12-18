tokens=[
    'BEGIN',
    'END',
    'EQUAL',
    'PLUS',
    'MINUS',
    'VAR',
    'COMMA',
    'ASSIGN',
    'SEMICOLUMN',
    'MULTIPLY',
    'DIVID',
    'INT',
    'FLOAT',
    'OPENPRACS',
    'CLOSEPRACS',
]

t_COMMA = r','
t_ignore= r' '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_EQUAL = r'\='
t_ASSIGN = r'\=\>'
t_OPENPRACS = r'\('
t_CLOSEPRACS = r'\)'
t_SEMICOLUMN =r'\;'
t_MULTIPLY = r'\*'
t_DIVID = r'\/'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_BEGIN(t):
    r'BEGIN:'
    t.type = "BEGIN"
    return t

def t_END(t):
    r'END:'
    t.type = "END"
    return t

def t_VAR(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = 'VAR'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0.0
    return t

def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return
