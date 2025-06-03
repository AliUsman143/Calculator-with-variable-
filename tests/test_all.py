# tests/test_all.py

import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parser.ast_nodes import NumberNode, VarNode, BinOpNode, AssignmentNode
from utils.symbol_table import SymbolTable
from codegen.codegen import evaluate

class TestCompiler(unittest.TestCase):
    def test_number_node(self):
        node = NumberNode(7)
        result = evaluate(node, SymbolTable())
        self.assertEqual(result, 7)

    def test_assignment_and_lookup(self):
        symtab = SymbolTable()
        assign = AssignmentNode('x', NumberNode(10))
        evaluate(assign, symtab)
        self.assertEqual(symtab.get('x'), 10)

    def test_binop_add(self):
        node = BinOpNode('+', NumberNode(2), NumberNode(3))
        result = evaluate(node, SymbolTable())
        self.assertEqual(result, 5)

    def test_binop_nested(self):
        symtab = SymbolTable()
        expr = BinOpNode('*',
                         BinOpNode('+', NumberNode(2), NumberNode(3)),
                         NumberNode(4))  # (2+3)*4 = 20
        result = evaluate(expr, symtab)
        self.assertEqual(result, 20)

if __name__ == '__main__':
    unittest.main()
