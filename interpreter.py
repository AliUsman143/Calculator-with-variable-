from parser import ast_nodes

symbol_table = {}

def evaluate(node):
    if isinstance(node, ast_nodes.NumberNode):
        return node.value

    elif isinstance(node, ast_nodes.VarNode):
        if node.name in symbol_table:
            return symbol_table[node.name]
        else: #if variable is not define 
            raise Exception(f"Variable '{node.name}' not defined.")

    elif isinstance(node, ast_nodes.BinOpNode):
        left = evaluate(node.left)
        right = evaluate(node.right)

        if node.op == '+':
            return left + right
        elif node.op == '-':
            return left - right
        elif node.op == '*':
            return left * right
        elif node.op == '/':
            return left / right

    elif isinstance(node, ast_nodes.AssignmentNode):
        value = evaluate(node.expr)
        symbol_table[node.var] = value
        return value

    else:
        raise Exception("Unknown node type")
