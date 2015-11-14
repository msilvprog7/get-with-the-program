##
## Operations
##

PLAYER_WALK = "walk"
PLAYER_RUN  = "run"
PLAYER_JUMP = "jump"
PLAYER_ROLL = "roll"
PLAYER_STOP = "stop"

##
## Statements
##

class ActionStatement():
    op = None
    num = 0

    def run(self, state):
        state.perform_action(self.op, self.num)
        return (None, state)

class WalkStatement(ActionStatement):
    def __init__(self, num, run):
        super(WalkStatement,self).__init__(*args, **kwargs)
        self.num = num

        if run:
            self.op = PLAYER_RUN
        else:
            self.op = PLAYER_WALK

class JumpStatement(ActionStatement):
    def __init__(self):
        super(JumpStatement,self).__init__(*args,**kwargs)
        self.num = 1
        self.op = PLAYER_JUMP

class RollStatement(ActionStatement):
    def __init__(self):
        super(RollStatement,self).__init__(*args,**kwargs)
        self.num = 1
        self.op = PLAYER_ROLL

class StopStatement(ActionStatement):
    def __init__(self):
        super(StopStatement,self).__init__(*args,**kwargs)
        self.num = 1
        self.op = PLAYER_STOP
