import ast
from ast import FunctionDef, ClassDef, NodeVisitor, Name

def collectProgramDesign(path: str):
    with open(path, "r") as f:
        source = f.read()

    # parse the given file.
    myast = ast.parse(source)

    root_functions = []
    # root_classes = {}
    root_classes = {}
    # iterate root children.
    for child in myast.body:
        if isinstance(child, FunctionDef):
            root_functions.append(child.name)
        if isinstance(child, ClassDef):
            funcs = [func.name for func in child.body if isinstance(func, FunctionDef)]
            avisitor = MyClassVisitor(funcs)
            avisitor.visit(child)
            root_classes[child.name] = {"attrs": set(avisitor.getFieldList()), "funcs": funcs}

    return root_functions, root_classes

class MyClassVisitor(NodeVisitor):
    def __init__(self, funcs) -> None:
        super().__init__()
        self.fields = []
        self.funcs = funcs

    def visit_Attribute(self, node):
        if isinstance(node.value, Name) and node.value.id == "self" and node.attr not in self.funcs:
            self.fields.append(node.attr)
        return self.generic_visit(node)

    def getFieldList(self):
        return self.fields


if __name__ == '__main__':
    print(collectProgramDesign("./input.py"))
