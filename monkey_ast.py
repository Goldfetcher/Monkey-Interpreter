class Node:
    pass


class Expression(Node):
    pass


class IntegerLiteral(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"IntegerLiteral({self.value})"