class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def to_postfix (infix):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["^"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []
    tokenList = list(infix)

    for token in tokenList:
        if token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return ''.join(postfixList)

# Clever
'''
def to_postfix (infix):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}
    postfix = []
    stack = []
    for ch in infix:
        if ch in '0123456789':
            postfix.append(ch)
        elif ch in '(':
            stack.append(ch)
        elif ch in ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and prec[stack[-1]] >= prec[ch]:
                postfix.append(stack.pop())
            stack.append(ch)

    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)
'''
