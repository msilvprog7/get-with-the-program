##
## Operators
##

ARITH_MULT = "*"
ARITH_ADD  = "+"
ARITH_SUB  = "-"
ARITH_DIV  = "/"
ARITH_NEG  = "~"

COMP_LT = "<"
COMP_GT = ">"
COMP_EQ = "=="

LOG_AND = "&&"
LOG_OR  = "||"
LOG_NOT = "!"

##
## Expressions
##

class Expression():
    pass

class NumExpression():
    value = 0

    def __init__(self, num):
        self.value = num

    def run(self, state):
        return (self.value, state)

class BinaryExpression():
    op = None

    exp1 = None
    exp2 = None
    
    def __init__(self, op, exp1, exp2):
        self.op = op
        self.exp1 = exp1
        self.exp2 = exp2

    def run(self, state):
        val1, state = self.exp1.run(state)
        val2, state = self.exp2.run(state)

        answer = self.run_result(val1, val2)

        return (answer, state)

    def run_result(self, val1, val2):
        if self.op == ARITH_ADD:
            return val1 + val2
        elif self.op == ARITH_SUB:
            return val1 - val2
        elif self.op == ARITH_MULT:
            return val1 * val2
        elif self.op == ARITH_DIV:
            return val1 / val2

        elif self.op == COMP_LT:
            return val1 < val2
        elif self.op == COMP_GT:
            return val1 > val2
        elif self.op == COMP_EQ:
            return val1 == val2

        elif self.op == LOG_AND:
            return val1 and val2
        elif self.op == LOG_OR:
            return val1 or val2

class UnaryExpression():
    op = None
    exp1 = None

    def __init__(self, op, exp1):
        self.op = op
        self.exp1 = exp1

    def run(self, state):
        val1, state = self.exp1.run(state)

        answer = self.run_result(val1)

        return (answer, state)

    def run_result(self, val1):
        if self.op == ARITH_NEG:
            return -val1
        elif self.op == LOG_NOT:
            return not val1

##
## Statements
##

class Statement():
    pass

class WhileStatement():
    condition = None
    body = None

    def __init__(condition, body):
        self.condition = condition
        self.body = body

    def run(self, state):
        b, state = condition.run(state)

        if b:
            val, state = self.run_body(state)
            self.run(state)

        return

    def run_body(self, state):
        return self.body.run(state)

class SequenceStatement():
    substatements = []

    def __init__(sub):
        self.substatements = sub

    def run(self, state):
        for statement in substatements:
            val, state = statement.run(state)

class IfStatement():
    condition = None
    
    then_statement = None
    else_statement = None

    def __init__(condition, then, els):
        self.condition = condition
        self.then_statement = then
        self.else_statement = els

    def run(self, state):
        cval, state = self.condition.run(state)
        
        if cval:
            return self.then_statement.run(state)
        else:
            return self.else_statement.run(state)

class PassStatement():    
    def run(self, state):
        return (None, state)
