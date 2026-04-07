import ply.yacc as yacc
import ply.lex as lex
import math
from translator import translate
from calctype import calc_type
tokens = (
    'MATRIX','SCALAR', 'NUMBER', 'VECTOR',
    'PLUS','MINUS','TIMES', 'TRANSP', 'DIVIDE',
    'LPAREN','RPAREN','DOT','INVERSE','POWER'
    )

# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_TRANSP   = r'\^T'
# t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_MATRIX  = r'[A-Z][A-Z0-9]*'
t_SCALAR  = r'[a-z0-9]+'
t_POWER   = r'\*\*'
t_DOT     = r'@'
t_INVERSE = r'~'
t_VECTOR = r'_[a-z0-9]+'

R = []
U = {}
seq = ""
T = {}

functions = {'exp':math.exp,'sin':math.sin}
global idx
idx = 0
def t_NUMBER(t):
    r'\d+\.?\d*'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DOT','DIVIDE'),
    ('left','POWER'),
    ('left','TRANSP','INVERSE')
    )


def p_statement_expr(t):
    'statement : expression'
    # print(t[1])
    # print("R = ",R)
    for r in R:
        # print(f"{r[0]} = {r[1]} {r[3]} {r[2]}")
        try:
            seq += f"{r[0]} = {r[1]} {r[3]} {r[2]}"
        except:
            seq = ""
def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_transp(t):
    """
    expression : expression TRANSP
    """
    global idx
    idx += 1
    # print(idx)
    data = [f"x{idx}", t[1][0], "", "^T"]
    # print(data)
    R.append(data)
    t[0] = data
    tp = calc_type(data, T)
    T[data[0]] = tp

def p_expression_binoper(t):
    '''expression : expression PLUS expression
       | expression MINUS expression
       | expression TIMES expression
       | expression DOT expression
       | expression DIVIDE expression
       | expression POWER expression

                  '''
    global idx
    idx += 1
    # print(idx,t[1])
    data = [f"x{idx}",t[1][0],t[3][0],t[2]]
    # print(data)
    R.append(data)
    t[0] = data
    tp = calc_type(data,T)
    T[data[0]] = tp

def p_expression_call(t):
    'expression : SCALAR LPAREN expression RPAREN'
    global idx
    idx += 1
    # print(idx,t[1])
    data = [f"x{idx}", t[3][0], '', t[1]]
    # print(data)
    R.append(data)
    t[0] = data
    tp = calc_type(data, T)
    # print("CALL",tp)
    T[data[0]] = tp


def p_expression_uminus(t):
    'expression : INVERSE expression'
    global idx
    idx += 1
    # print(idx)
    data = [f"x{idx}", t[2][0], "", "~"]
    # print(data)
    R.append(data)
    t[0] = data
    tp = calc_type(data, T)
    T[data[0]] = tp
    # print(data[0], tp)

def p_error(t):
    print("Syntax error at '%s'" % t.value)

def p_expression_matrix(t):
    '''
    expression : MATRIX
                 | SCALAR
                 | NUMBER
                 | VECTOR
    '''
    # print("init: ",str(t[1]))
    t[0] = [str(t[1]),"","",""]


mylex = lex.lex()


parser = yacc.yacc()

# parser.parse(expr)
# code = translate(R,T)
# print(code)
# print(T)


