import ply.yacc as yacc
from .ast_nodes import AssignmentNode, BinOpNode, NumberNode, VarNode
from lexer.my_lexer import tokens  # ✅ correct import

# Operator precedence rules
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Grammar rules
def p_statement_assign(p):
    'statement : ID EQUALS expression'
    p[0] = AssignmentNode(p[1], p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = BinOpNode(p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = NumberNode(p[1])

def p_expression_id(p):
    'expression : ID'
    p[0] = VarNode(p[1])

# Syntax error handling
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
        raise SyntaxError(f"Syntax error near '{p.value}'")
    else:
        print("Syntax error at end of input")
        raise SyntaxError("Syntax error at end of input")

# Build parser
parser = yacc.yacc()
