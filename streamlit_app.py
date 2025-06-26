# streamlit_app.py

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
            # ===============================
            # 📦 Tokenization
            # ===============================
            lexer.input(user_input)
            token_data = []
            while True:
                tok = lexer.token()
                if not tok:
                    break
                token_data.append({
                    "Type": tok.type,
                    "Value": tok.value,
                    "Line": tok.lineno,
                    "Position": tok.lexpos
                })

            # 📊 Show tokens in table
            st.subheader("🧾 Tokens")
            st.dataframe(token_data, use_container_width=True)

            # ===============================
            # 🧠 Parsing and Evaluation
            # ===============================
            ast = parser.parse(user_input, lexer=lexer)
            result = evaluate(ast, st.session_state.symtab)

            # ✅ Show result
            st.success("✅ Output:")
            st.code(result)

            # 📘 Show symbol table
            st.info("📘 Symbol Table:")
            st.json(st.session_state.symtab.table)

        except SyntaxError as e:
            st.error(f"🚫 Syntax Error: {str(e)}")

        except Exception as e:
            st.error(f"❌ Runtime Error: {str(e)}")
