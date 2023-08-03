import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


class dpda_machine:
    def __init__(self, states, alphabet, stack_alphabet, transitions, start_state, start_stack_symbol, accept_states):
        self.current_state = None
        self.stack = None
        self.states = states
        self.alphabet = alphabet
        self.stack_alphabet = stack_alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.start_stack_symbol = start_stack_symbol
        self.accept_states = accept_states

    # def run(self, input_string):
    #     print("It is running")
    #     current_state = self.start_state
    #     stack = [self.start_stack_symbol]
    #     input_index = 0
    
    def process_input(self, input_string):

        self.current_state = self.start_state
        self.stack = [self.start_stack_symbol]
        
        for symbol in input_string:
            print("Stack: ", self.stack)
            if self.current_state is None:
                return False
            stack_top = self.stack[-1] if self.stack else None
            key = (self.current_state, symbol, stack_top)
            print("key and stack top", key, " ", stack_top)
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


def readfile():
    print("reading file")
    filename = filedialog.askopenfilename()
    with open(filename, 'r') as file:
        file_data = {}
        current_section = None

        for line in file:
            line = line.strip()

            if line == '':
                continue

            if line.endswith(':'):
                current_section = line[:-1]
                file_data[current_section] = []
            else:
                file_data[current_section].append(line)

    return file_data


def main():
    print("1-Stack 1-Way DPDA")

    print("Please read file")
    dpdaFile_data = readfile()

    states = set(dpdaFile_data['States'])
    alphabet_inputs = set(dpdaFile_data['Alphabet Inputs'])
    stack_alphabets = set(dpdaFile_data['Stack Alphabets'])
    start_state = dpdaFile_data['Start State'][0]
    starting_stack_symbol = dpdaFile_data['Starting Stack Symbol'][0]
    final_state = dpdaFile_data['Final States'][0]
    transitionsRaw_list = dpdaFile_data['Transitions']  # DONT REMOVE PROBABLY WILL BE USEFUL FOR FRONTEND

    print(transitionsRaw_list)

    transitions = set()
    # Iterate through each string in the input list
    for transition_str in transitionsRaw_list:
        # Split the string by commas to get the components of the transition
        q_from, symbol_read, symbol_write, q_to, stack_write = transition_str.split(',')

        # Create a tuple representing the transition and add it to the set
        transition = (q_from.strip(), symbol_read.strip(), symbol_write.strip(), q_to.strip(), stack_write.strip())
        transitions.add(transition)

    print("File Read")

    print("States:", states, type(states))
    print("Alphabet Inputs:", alphabet_inputs)
    print("Stack Alphabets:", stack_alphabets)
    print("Start State:", start_state)
    print("Starting Stack Symbol:", starting_stack_symbol)
    print("Final States:", final_state)
    print("Transitions:", transitions)
    
    
    # Creation of DPDA
    dpda_machine_1 = dpda_machine(states, alphabet_inputs, stack_alphabets, transitions, start_state, starting_stack_symbol, final_state)
    
    

    input_string = input("Input String to be read: ")
    print(input_string)

    if dpda_machine_1.process_input(input_string):
        print(f'String "{input_string}" is accepted.')
    else:
        print(f'String "{input_string}" is not accepted.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
