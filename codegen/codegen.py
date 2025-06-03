import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parser.ast_nodes import NumberNode, VarNode, BinOpNode, AssignmentNode


def evaluate(node, symtab):
    if isinstance(node, NumberNode):
        return node.value
    elif isinstance(node, VarNode):
        return symtab.get(node.name)
    elif isinstance(node, BinOpNode):
        left = evaluate(node.left, symtab)
        right = evaluate(node.right, symtab)
        return eval(f"{left} {node.op} {right}")
    elif isinstance(node, AssignmentNode):
        value = evaluate(node.expr, symtab)
        symtab.assign(node.var, value)
        return value
