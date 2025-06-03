from lexer.my_lexer import lexer
from parser.parser import parser
from semantic.semantic_analyzer import SymbolTable
from codegen.codegen import evaluate

if __name__ == '__main__':
    symtab = SymbolTable()
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        result = parser.parse(text)
        value = evaluate(result, symtab)
        print("=>", value)
