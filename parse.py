import lexical as main
from lexical import *
import ply.lex as lex
import ply.yacc as yacc
import sys
from PyQt5.QtWidgets import *

#tree Data Structer 
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

#function print tree
def print_Tree(tree, level=1):
    global globz
    globz.append('    ' * (level - 1) + '--->' * (level > 0) + tree.data)
    for l in tree.children:
        if isinstance(l, Node):
            print_Tree(l, level + 1)
        else:
            if type(l) is list:
                for value in l:
                    if type(value) is int or type(value) is float:
                        value = str(value)
                    if (isinstance(value , Node)):
                        print_Tree(value, level + 1)
                    else:
                        globz.append('    ' * level + '--->' + value)
            else:

                globz.append('    ' * level + '+---' + str(l))
#build lex for lexical file
lexer = lex.lex(main)
#parser part
def p_error(p):
    global globz
    try:
        globz.append("Syntax error at " + p.value)
    except:
        globz.append("Syntax error")

def p_startforeach(p):
    '''Start : foreach
             | foreach Start'''
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


#input
"""input = a => b BEGIN:
a = a + z + 5 + z;
add(a+b,s,(a+5.5 + 5));
z(s);
END:"""

#Parse input
def parser(input):
    parser = yacc.yacc()
    parser.parse(input)



class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Concept Task'
        self.left = 100
        self.top = 100
        self.width = 700
        self.height = 600
        self.setFixedSize(self.width,self.height)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create
        self.textEdite = QTextEdit(self)
        self.textEdite.move(20, 0)
        self.textEdite.resize(500, 300)
        # Create
        self.reusltText = QTextEdit(self)
        self.reusltText.move(20, 320)
        self.reusltText.resize(500, 280)
        self.reusltText.setReadOnly(True)

        # Create a button in the window
        self.button = QPushButton('parse', self)
        self.button.move(550, 140)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        self.reusltText.setText('')
        textboxValue = self.textEdite.toPlainText()
        parser(textboxValue)
        if len(getarr()) >= 1:
            self.reusltText.setText('')
            for x in getarr():
                self.reusltText.append(x)
            clearARRAYERROR()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    globz = ex.reusltText
    sys.exit(app.exec_())