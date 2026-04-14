class Node:
    pass


class Expression(Node):
    pass


class IntegerLiteral(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"IntegerLiteral({self.value})"


# Introducing let feature 
class Node:
    pass


class Expression(Node):
    pass


class IntegerLiteral(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


class InfixExpression(Expression):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.operator} {self.right})"


class Identifier(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value


class LetStatement(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"let {self.name} = {self.value};"
