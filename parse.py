import lexical as main
from lexical import tokens
import ply.lex as lex
import ply.yacc as yacc

#tree Data Structer 
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

#function print tree
def print_Tree(tree, level=1):
    print('    ' * (level - 1) + '--->' * (level > 0) + tree.data)
    for l in tree.children:
        if isinstance(l, Node):
            print_list(l, level + 1)
        else:
            if type(l) is list:
                for value in l:
                    if value == '\n':
                        value = 'newline'
                    if type(value) is int or type(value) is float:
                        value = str(value)
                    if (isinstance(value , Node)):
                        print_Tree(value, level + 1)
                    else:
                        print('    ' * level + '--->' + value)
            else:

                print('    ' * level + '+---' + str(l))
#build lex for lexical file
lexer = lex.lex(main)
#parser part
def p_error(p):
    print("Error in line ", (p.lineno), " Illegal " ,p.value)

def p_startforeach(p):
    "Start : foreach"
    print_Tree(p[1])
def p_foreach(p):
    """
    foreach : var ASSIGN var  BEGIN  statementlist END
    """
    x = Node('foreach')
    x.add_child(p[1:])
    p[0] = x

def p_statementlist(p):
    """
    statementlist : statement SEMICOLUMN statementlist
                  | statement SEMICOLUMN
    """
    x = Node('statementlist')
    x.add_child(p[1:])
    p[0] = x

def p_statement(p):
    """
    statement : var EQUAL expr
              | functioncall
    """
    x = Node('statment')
    x.add_child(p[1:])
    p[0] = x

def p_expr(p):
    """
    expr : var PLUS expr
         | var MINUS expr
         | var MULTIPLY expr
         | var DIVID expr
         | var
         | OPENPRACS expr CLOSEPRACS
    """
    x = Node('expr')
    x.add_child(p[1:])
    p[0] = x

def p_function(p):
    """
    functioncall : VAR OPENPRACS parameterList CLOSEPRACS
    """
    x = Node('functioncall')
    x.add_child(p[1:])
    p[0] = x

def p_parameterList(p):
    """
     parameterList : parameter
                   | parameter COMMA parameterList
    """
    x = Node('parameterList')
    x.add_child(p[1:])
    p[0] = x

def p_parameter(p):
    """
     parameter : expr
    """
    x = Node('parameter')
    x.add_child(p[1:])
    p[0] = x

def p_var(p):
    """
     var : VAR
         | constant
    """
    x = Node('var')
    x.add_child(p[1:])
    p[0] = x

def p_constant(p):
    """
     constant : INT
              | FLOAT
    """
    x = Node('constal')
    x.add_child(p[1:])
    p[0] = x

#Build Parser
parser = yacc.yacc()

 #input
input = """a => b
BEGIN:
a = b / z;
add(a+b,s,(a+5.5));
END:"""

#Parse input
parser.parse(input)