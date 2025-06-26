# interpreter.py

from parser import ast_nodes
import threading

# Global symbol table (shared across all threads)
symbol_table = {}

def evaluate(node):
    if isinstance(node, ast_nodes.NumberNode):
        return node.value

    elif isinstance(node, ast_nodes.VarNode):
        if node.name in symbol_table:
            return symbol_table[node.name]
        else:
            raise Exception(f"❌ Variable '{node.name}' not defined.")

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
            if right == 0:
                raise Exception("❌ Division by zero.")
            return left / right
        else:
            raise Exception(f"Unknown operator '{node.op}'")

    elif isinstance(node, ast_nodes.AssignmentNode):
        value = evaluate(node.expr)
        symbol_table[node.var] = value
        return value

    else:
        raise Exception("❌ Unknown AST node type.")


# =============================================
# ✅ Multi-threaded Expression Evaluator
# =============================================

def threaded_evaluate(expr_ast, thread_id=None):
    """
    Evaluate an expression AST in a separate thread.
    Optionally pass a thread ID for logging.
    """
    try:
        result = evaluate(expr_ast)
        print(f"🧵 Thread {thread_id}: ✅ Result = {result}")
    except Exception as e:
        print(f"🧵 Thread {thread_id}: ❌ Error: {e}")


def run_multithreaded_batch(ast_list):
    """
    Takes a list of ASTs and runs each in its own thread.
    Waits for all threads to finish.
    """
    threads = []
    for i, ast in enumerate(ast_list):
        t = threading.Thread(target=threaded_evaluate, args=(ast, i + 1))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
