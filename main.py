# imports tkinter
from tkinter import *
from tkinter import filedialog

window = Tk()

dpdaFile_data = ""
dpda_Machine = ""


###########################################################################
#                 BACKEND
###########################################################################
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

    def process_input(self, input_string):

        self.current_state = self.start_state
        self.stack = [self.start_stack_symbol]

        for symbol in input_string:
            print(symbol)
            # print("Stack: ", self.stack)
            if self.current_state is None:
                return False
            stack_top = self.stack[-1] if self.stack else None
            key = (self.current_state, symbol, stack_top)
            print("key and stack top", key, " ", stack_top)
            if key not in self.transitions:
                return False
            next_state, push_to_stack = self.transitions[key]

            self.stack.pop()
            if push_to_stack != '':
                for to_append in push_to_stack:
                    self.stack.append(to_append)
            self.current_state = next_state

            print("last check: current state ", self.current_state, "accept state: ", self.accept_states)
            print("stack: ", self.stack)

        if self.current_state == self.accept_states:
            return True
        else:
            return False


def process_file_to_DPDA(dpdaFile_data):
    states = set(dpdaFile_data['States'])
    alphabet_inputs = set(dpdaFile_data['Alphabet Inputs'])
    stack_alphabets = set(dpdaFile_data['Stack Alphabets'])
    start_state = dpdaFile_data['Start State'][0]
    starting_stack_symbol = dpdaFile_data['Starting Stack Symbol'][0]
    final_state = dpdaFile_data['Final States'][0]
    transitionsRaw_list = dpdaFile_data['Transitions']  # DONT REMOVE PROBABLY WILL BE USEFUL FOR FRONTEND

    # print(transitionsRaw_list)

    transitions = {}
    # Iterate through each string in the input list
    for transition_str in transitionsRaw_list:
        # Split the string by commas to get the components of the transition
        q_from, symbol_read, top_stack, q_to, stack_write = transition_str.split(',')

        key = (q_from, symbol_read, top_stack)
        transitions[key] = (q_to, stack_write)

    print("File Read")

    print("States:", states, type(states))
    print("Alphabet Inputs:", alphabet_inputs)
    print("Stack Alphabets:", stack_alphabets)
    print("Start State:", start_state)
    print("Starting Stack Symbol:", starting_stack_symbol)
    print("Final States:", final_state)
    print("Transitions:", transitions)

    # Creation of DPDA
    dpda_machine_1 = dpda_machine(states, alphabet_inputs, stack_alphabets, transitions, start_state,
                                  starting_stack_symbol, final_state)
    return dpda_machine_1


###########################################################################
#                 BUTTON FUNCTIONS
###########################################################################

def openFile(machine_text):
    print("Open File Button Clicked!")
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

    global dpdaFile_data
    dpdaFile_data = file_data

    global dpda_Machine
    dpda_Machine = process_file_to_DPDA(dpdaFile_data)

    text_to_insert = (
        f"States: {dpda_Machine.states}\n"
        f"Alphabet Inputs: {dpda_Machine.alphabet}\n"
        f"Stack Alphabets: {dpda_Machine.stack_alphabet}\n"
        f"Start State: {dpda_Machine.start_state}\n"
        f"Starting Stack Symbol: {dpda_Machine.start_stack_symbol}\n"
        f"Final States: {dpda_Machine.accept_states}\n"
        f"Transitions:\n"
    )

    for transition in dpda_Machine.transitions:
        text_to_insert += f"{transition} -> {dpda_Machine.transitions[transition]}\n"

    text_to_insert += "\n"

    machine_text.delete(1.0, END)
    machine_text.insert(1.0, text_to_insert)


def run_action(machine_text):
    print("Run button clicked!")
    machine_text.insert("1.0", dpdaFile_data)


def pause_action():
    print("Pause button clicked!")


def step_action():
    print("Step button clicked!")


def reset_action():
    print("Reset button clicked!")


def enter_action():
    print("Enter Button Clicked!")


###########################################################################
#                 FRONTEND
###########################################################################
def create_window():
    input_string = StringVar()

    window.title("1-way 1-stack Deterministic Pushdown Automata")
    window.geometry("864x640")

    file_button = Button(window, text="Open File", command=lambda: openFile(machine_text))

    # Controls
    controls_frame = LabelFrame(window, text="Controls")
    run_button = Button(controls_frame, text="Run", command=lambda: run_action(machine_text))
    pause_button = Button(controls_frame, text="Pause", command=pause_action)
    step_button = Button(controls_frame, text="Step", command=step_action)
    reset_button = Button(controls_frame, text="Reset", command=reset_action)

    # Input String
    input_frame = LabelFrame(window, text="Please input the string:")
    input_box = Entry(input_frame, textvariable=input_string, width=20)

    # Current State
    currentState_frame = LabelFrame(window, text="Current State")
    currentState_Label = Label(currentState_frame, text="Placeholder")

    # Steps
    steps_frame = LabelFrame(window, text="Steps")
    steps_Label = Label(steps_frame, text="Placeholder")

    # Input String
    traceInput_frame = LabelFrame(window, text="Input String(idk wtf this is yet)")
    traceInput_Label = Label(traceInput_frame, text="Placeholder")

    # Stack String
    stack_frame = LabelFrame(window, text="Stack")
    stack_Label = Label(stack_frame, text="Placeholder")

    # Machine
    machine_frame = LabelFrame(window, text="Machine")
    machine_text = Text(machine_frame, wrap=WORD)

    # Tracing
    tracing_frame = LabelFrame(window, text="Trace")
    tracing_text = Text(tracing_frame)

    # GridStyle Formatting
    file_button.grid(row=0, column=0, columnspan=2)

    controls_frame.grid(row=2, column=0, rowspan=3, columnspan=2, padx=10, pady=10, sticky="nsew")
    input_frame.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
    currentState_frame.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    steps_frame.grid(row=10, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    traceInput_frame.grid(row=0, column=3, rowspan=2, columnspan=17, padx=10, pady=10)
    stack_frame.grid(row=3, column=3, columnspan=17, padx=10, pady=10)
    machine_frame.grid(row=5, rowspan=5, column=3, columnspan=7, padx=10, pady=10)
    tracing_frame.grid(row=5, rowspan=5, column=12, columnspan=7, padx=10, pady=10)

    # Arrange buttons in a grid layout within the LabelFrame
    run_button.grid(row=0, column=0, padx=5, pady=5)
    pause_button.grid(row=0, column=1, padx=5, pady=5)
    step_button.grid(row=1, column=0, padx=5, pady=5)
    reset_button.grid(row=1, column=1, padx=5, pady=5)

    input_box.grid(row=0, column=0, padx=5, pady=5)
    currentState_Label.grid(row=0, column=0, padx=5, pady=5)
    steps_Label.grid(row=0, column=0, padx=5, pady=5)
    traceInput_Label.grid(row=0, column=0, padx=5, pady=5)
    stack_Label.grid(row=0, column=0, padx=5, pady=5)
    machine_text.grid(row=0, column=0, padx=5, pady=5)
    tracing_text.grid(row=0, column=0, padx=5, pady=5)

    # Shows the Window
    window.mainloop()


def main():
    print("Yo")
    create_window()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
