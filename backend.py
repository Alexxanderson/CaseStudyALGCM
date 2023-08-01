class DPDA:
    def __init__(self):
        self.stack = []
        self.transitions = {}
        self.current_state = None

    def add_transition(self, state, input_symbol, stack_symbol, next_state, push_to_stack):
        key = (state, input_symbol, stack_symbol)
        self.transitions[key] = (next_state, push_to_stack)

    def initialize(self, start_state, start_stack_symbol):
        self.current_state = start_state
        self.stack = [start_stack_symbol]

    def process_input(self, input_string):
        for symbol in input_string:
            if self.current_state is None:
                return False
            stack_top = self.stack[-1] if self.stack else None
            key = (self.current_state, symbol, stack_top)
            if key not in self.transitions:
                return False
            next_state, push_to_stack = self.transitions[key]
            if push_to_stack != '':
                self.stack.append(push_to_stack)
            self.current_state = next_state

        if self.current_state is None:
            return False

        while self.stack:
            stack_top = self.stack.pop()
            key = (self.current_state, '', stack_top)
            if key not in self.transitions:
                return False
            self.current_state, _ = self.transitions[key]

        return self.current_state == 'accept'


# Example usage:
dpda = DPDA()

# Define states and symbols
dpda_states = {'q0', 'q1', 'q2', 'accept'}
input_symbols = {'a', 'b'}
stack_symbols = {'Z', 'A'}

# Add transitions
dpda.add_transition('q0', 'a', 'Z', 'q1', 'A')  # Transition: q0 --a, Z/A--> q1
dpda.add_transition('q1', 'a', 'A', 'q1', 'A')  # Transition: q1 --a, A/A--> q1
dpda.add_transition('q1', 'b', 'A', 'q2', '')   # Transition: q1 --b, A/ε--> q2
dpda.add_transition('q2', 'b', 'A', 'q2', '')   # Transition: q2 --b, A/ε--> q2
dpda.add_transition('q2', '', 'Z', 'accept', '')  # Transition: q2 --ε, Z/ε--> accept

# Initialize the DPDA
dpda.initialize('q0', 'Z')

# Test some strings
test_strings = ['aabb', 'aaabb', 'ab', 'aabbb']
for string in test_strings:
    if dpda.process_input(string):
        print(f'String "{string}" is accepted.')
    else:
        print(f'String "{string}" is not accepted.')
