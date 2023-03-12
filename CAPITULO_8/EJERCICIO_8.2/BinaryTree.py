from PostfixTranslate import nextToken

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None

    def __str__(self):
        return str(self.value)

def buildExpressionTree(postfixExpr):
    stack = []
    tokens = postfixExpr.split()

    for token in tokens:
        if token in "+-*/":
            if len(stack) < 2:
                raise ValueError("Expresión no válida: muy pocos operandos")
            right = stack.pop()
            left = stack.pop()
            exprTree = BinaryTree(token)
            exprTree.left = left
            exprTree.right = right
            stack.append(exprTree)
        else:
            exprTree = BinaryTree(token)
            stack.append(exprTree)

    if len(stack) != 1:
        raise ValueError("Expresión no válida: demasiados operandos")

    return stack[0]

def preorder(tree):
    if tree is not None:
        print(tree.value, end=" ")
        preorder(tree.left)
        preorder(tree.right)

def inorder(tree):
    if tree is not None:
        if tree.isLeaf():
            print(tree.value, end=" ")
        else:
            print("(", end=" ")
            inorder(tree.left)
            print(tree.value, end=" ")
            inorder(tree.right)
            print(")", end=" ")

def postorder(tree):
    if tree is not None:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.value, end=" ")

def test(postfixExpr):
    try:
        exprTree = buildExpressionTree(postfixExpr)
        print("Árbol de expresión:", end=" ")
        inorder(exprTree)
        print("\nNotación de infijos:", end=" ")
        inorder(exprTree)
        print("\nNotación de prefijos:", end=" ")
        preorder(exprTree)
        print("\nNotación de sufijos:", end=" ")
        postorder(exprTree)
        print("\n")
    except ValueError as e:
        print(str(e))

# Test cases
test("91 95 + 15 + 19 + 4 *")
test("B B * A C 4 * * -")
test("42")
test("A 57 #")  # esto debería producir una excepción
test("+ / #")   # esto debería producir una excepción