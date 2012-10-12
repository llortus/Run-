class State(object):
    def __init__(self):
        pass

    def enter(self):
        """Initialize data that might not be initialized in init"""
        pass

    def exit(self):
        """State is finished, perform cleanup if necessary"""
        pass

    def reason(self):
        """Conditional or logic to see if the current state needs to end, and a new one started"""
        pass

    def act(self):
        """Per-frame behavior"""
        pass

class StateMachine(object):

    def __init__(self, host, first_state=None):
        self.host = host
        self.current_state = first_state

    def transition(self, new_state):
        """Transition to a new State"""
        self.current_state.exit()

        self.current_state = new_state

        # provide state references to host object and fsm instance
        self.current_state.host = self.host
        self.current_state.fsm = self

        self.current_state.enter()

    def update(self):
        if self.current_state: # only update if we have a state
            new_state = self.current_state.reason()

            if new_state: # if reason provides new state
                # do transition
                self.transition(new_state)
            else:
                # otherwise act with current state
                self.current_state.act()