class Environment:
    def __init__(self):
        self.store = {}

    def get(self, name):
        return self.store.get(name)

    def set(self, name, value):
        self.store[name] = value
        return value


def eval(node, env):
    # IntegerLiteral → return number
    if type(node).__name__ == "IntegerLiteral":
        return node.value

    # Identifier → fetch value from environment
    elif type(node).__name__ == "Identifier":
        return env.get(node.value)

    # InfixExpression → compute left and right
    elif type(node).__name__ == "InfixExpression":
        left = eval(node.left, env)
        right = eval(node.right, env)

        if node.operator == "+":
            return left + right
        elif node.operator == "-":
            return left - right
        elif node.operator == "*":
            return left * right
        elif node.operator == "/":
            return left // right  # integer division

    # LetStatement → store variable
    elif type(node).__name__ == "LetStatement":
        val = eval(node.value, env)
        env.set(node.name.value, val)
        return val

    return None