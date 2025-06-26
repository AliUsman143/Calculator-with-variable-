from lexer.my_lexer import lexer
from parser.parser import parser
from semantic.semantic_analyzer import SymbolTable
from codegen.codegen import evaluate
from interpreter import run_multithreaded_batch  # ✅ Import batch thread runner

def run_interactive_mode():
    symtab = SymbolTable()
    print("🧮 Mini Calculator Compiler (Type 'exit' to quit)")

    while True:
        try:
            text = input('calc> ').strip()
            if text.lower() in ['exit', 'quit']:
                print("👋 Exiting calculator.")
                break

            if not text:
                continue

            # Parse and evaluate
            ast = parser.parse(text, lexer=lexer)
            value = evaluate(ast, symtab)
            print("=>", value)

        except SyntaxError as se:
            print(f"🚫 Syntax Error: {se}")
        except Exception as e:
            print(f"❌ Runtime Error: {e}")


def run_batch_threaded_mode():
    print("📥 Enter multiple expressions (type 'run' to execute):")

    expressions = []
    while True:
        line = input(">> ").strip()
        if line.lower() == "run":
            break
        if line:
            expressions.append(line)

    asts = []
    for expr in expressions:
        try:
            ast = parser.parse(expr, lexer=lexer)
            asts.append(ast)
        except Exception as e:
            print(f"❌ Skipped invalid input '{expr}': {e}")

    run_multithreaded_batch(asts)


if __name__ == '__main__':
    print("Choose mode:")
    print("1. Interactive Mode (type one expression at a time)")
    print("2. Batch Threaded Mode (enter multiple expressions first)")
    choice = input("Enter 1 or 2: ").strip()

    if choice == '2':
        run_batch_threaded_mode()
    else:
        run_interactive_mode()
