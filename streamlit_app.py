# streamlit_app.py
# Streamlit frontend for Calculator Compiler

import streamlit as st
from utils.symbol_table import SymbolTable
from codegen.codegen import evaluate
from parser.parser import parser
from lexer.my_lexer import lexer

st.set_page_config(page_title="Mini Calculator Compiler", layout="centered")

st.title("🧮 Calculator with Variables - Compiler Project")
st.markdown("Enter expressions like `x = 5 + 3 * 2` or just `x + 4`")

# Symbol table persists across runs
if "symtab" not in st.session_state:
    st.session_state.symtab = SymbolTable()

# Input field
user_input = st.text_area("Enter your code:", height=150)

if st.button("Run"):
    if user_input.strip() == "":
        st.warning("Please enter some code.")
    else:
        try:
            # Parse the user input into an AST
            ast = parser.parse(user_input, lexer=lexer)

            # Evaluate using your evaluator
            result = evaluate(ast, st.session_state.symtab)

            st.success("✅ Output:")
            st.code(result)

            st.info("📘 Symbol Table:")
            st.json(st.session_state.symtab.table)

        except SyntaxError as e:
            st.error(f"🚫 Syntax Error: {str(e)}")

        except Exception as e:
            st.error(f"❌ Runtime Error: {str(e)}")
