# save the varuiable assignments and look up variables in a symbol table. for futher use in future 
class SymbolTable: 
    def __init__(self):
        self.variables = {}

    def assign(self, var, value):
        self.variables[var] = value

    def get(self, var):
        if var not in self.variables:
            raise Exception(f"Undefined variable: {var}")
        return self.variables[var]
