# utils/symbol_table.py

class SymbolTable:
    def __init__(self):
        self.table = {}

    def assign(self, name, value):
        self.table[name] = value

    def get(self, name):
        value = self.table.get(name)
        if value is None:
            raise Exception(f"Undefined variable: {name}")
        return value

    def __str__(self):
        return str(self.table)
