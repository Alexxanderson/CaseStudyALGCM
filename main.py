# STALGCM CASE-STUDY S11 (DETERMINISTIC PUSHDOWN AUTOMATA)
# Bien Aaron Miranda
# Dominic Luis Baccay
# Luis Miguel Rana

# imports tkinter
from tkinter import *
from tkinter import filedialog

window = Tk()

# Global Variables
dpdaFile_data = ""
dpda_Machine = ""


###########################################################################
#                 BACKEND
###########################################################################

# 1-way 1-Stack Deterministic Pushdown Automata Class
class dpda_machine:
    def __init__(self, states, alphabet, stack_alphabet, transitions, start_state, start_stack_symbol, accept_state, details):
        self.current_state = None  # Current State, utilized on process
        self.stack = None  # Current Stack, utilized on process
        self.states = states  # Set of Possible States
        self.alphabet = alphabet  # Set of input alphabets
        self.stack_alphabet = stack_alphabet  # Set of stack alphabet
        self.transitions = transitions  # Set of Transitions
        self.start_state = start_state  # Start State
        self.start_stack_symbol = start_stack_symbol  # Starting Stack Symbol
        self.accept_state = accept_state  # Final state
        self.details = details

    # Processes the string of input and outputs if it is accepted or rejected based on the DPDA Design
    def process_input(self, input_string, tracing_text, currentState_Label, steps_Label, traceInput_Label, stack_Label,
                      time_step):

        self.current_state = self.start_state
        self.stack = [self.start_stack_symbol]
        i = 0
        string_to_show = input_string

        # Update the initial labels and text
        tracing_text.insert(END, f"Starting State: {self.current_state}\n")
        tracing_text.insert(END, f"Starting Stack: {self.stack}\n")
        tracing_text.insert(END, f"Input String: \"{input_string.split()}\" \n")
        currentState_Label.config(text=self.current_state)
        steps_Label.config(text=i)
        stack_Label.config(text=f"{self.stack}")
        traceInput_Label.config(text=f"{string_to_show}")

        def process_loop():
            nonlocal i, time_step, string_to_show

            print(i)
            print(len(input_string))
            print(self.current_state, " ", self.accept_state)

            if i >= len(input_string):
                if self.current_state == self.accept_state:
                    print(f'String "{input_string}" is accepted.')
                    tracing_text.insert(END, f'String "{input_string.split()}" is accepted. \n')
                else:
                    print(f'String "{input_string}" is not accepted.')
                    tracing_text.insert(END, f'String "{input_string.split()}" is not accepted. \n')
                return

            symbol = input_string[i]
            stack_top = self.stack[-1] if self.stack else None
            key = (self.current_state, symbol, stack_top)

            if key not in self.transitions:
                print(f'String "{input_string.split()}" is not accepted.')
                tracing_text.insert(END, f'String "{input_string.split()}" is not accepted. \n')
                return

            next_state, push_to_stack = self.transitions[key]

            self.stack.pop()
            if push_to_stack != '':
                for to_append in push_to_stack:
                    self.stack.append(to_append)
            self.current_state = next_state

            string_to_show = input_string[i:]
            tracing_text.insert(END, f"State: {self.current_state}, Input: {symbol}, Stack on Top: {stack_top}\n")
            currentState_Label.config(text=self.current_state)
            steps_Label.config(text=(i + 1))
            stack_Label.config(text=f"{self.stack}")
            traceInput_Label.config(text=f"{string_to_show}")

            i += 1
            tracing_text.see(END)  # Scroll to the end of the Text widget
            window.update()  # Update the GUI

            # Schedule the next iteration after a delay (e.g., 1000ms)
            window.after(time_step, process_loop)

        # Start the processing loop
        process_loop()


# Function used to instantiate the DPDA design based from the processed .txt file
def process_file_to_DPDA(dpda_data):
    details = set(dpda_data['Details'])
    states = set(dpda_data['States'])
    alphabet_inputs = set(dpda_data['Alphabet Inputs'])
    stack_alphabets = set(dpda_data['Stack Alphabets'])
    start_state = dpda_data['Start State'][0]
    starting_stack_symbol = dpda_data['Starting Stack Symbol'][0]
    final_state = dpda_data['Final States'][0]
    transitionsRaw_list = dpda_data['Transitions']

    transitions = {}
    # Iterate through each string in the input list
    for transition_str in transitionsRaw_list:
        # Split the string by commas to get the components of the transition
        q_from, symbol_read, top_stack, q_to, stack_write = transition_str.split(',')

        key = (q_from, symbol_read, top_stack)
        transitions[key] = (q_to, stack_write)

    print("States:", states, type(states))
    print("Alphabet Inputs:", alphabet_inputs)
    print("Stack Alphabets:", stack_alphabets)
    print("Start State:", start_state)
    print("Starting Stack Symbol:", starting_stack_symbol)
    print("Final States:", final_state)
    print("Transitions:", transitions)

    # Creation of DPDA
    dpda_machine_1 = dpda_machine(states, alphabet_inputs, stack_alphabets, transitions, start_state,
                                  starting_stack_symbol, final_state, details)
    return dpda_machine_1


###########################################################################
#                 BUTTON FUNCTIONS
###########################################################################

# Reads a .txt file and processes it to a data variable that is convertible into a DPDA design
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
        f"Details: \n {dpda_Machine.details}\n"
        f"States: {dpda_Machine.states}\n"
        f"Alphabet Inputs: {dpda_Machine.alphabet}\n"
        f"Stack Alphabets: {dpda_Machine.stack_alphabet}\n"
        f"Start State: {dpda_Machine.start_state}\n"
        f"Starting Stack Symbol: {dpda_Machine.start_stack_symbol}\n"
        f"Final States: {dpda_Machine.accept_state}\n"
        f"Transitions:\n"
    )

    for transition in dpda_Machine.transitions:
        text_to_insert += f"{transition} -> {dpda_Machine.transitions[transition]}\n"

    text_to_insert += "\n"

    machine_text.delete(1.0, END)
    machine_text.insert(1.0, text_to_insert)


# Processes the input at full speed
def run_action(input_box, currentState_Label, steps_Label, traceInput_Label, tracing_text, stack_Label):
    print("Run button clicked!")

    input_string = input_box.get()
    input_string_for_process = input_string + " "
    print(input_string)

    dpda_Machine.process_input(input_string_for_process, tracing_text, currentState_Label, steps_Label,
                               traceInput_Label, stack_Label, 0)


# Processes the input at a slower speed
def step_action(input_box, currentState_Label, steps_Label, traceInput_Label, tracing_text, stack_Label):
    print("Step button clicked!")

    input_string = input_box.get()
    input_string_for_process = input_string + " "
    print(input_string)

    # 1000 represents the time of delay
    dpda_Machine.process_input(input_string_for_process, tracing_text, currentState_Label, steps_Label,
                               traceInput_Label, stack_Label, 1000)


# Resets the content of input box, tracing text, current state, steps, trace input, and current stack
def reset_action(input_box, currentState_Label, steps_Label, traceInput_Label, tracing_text, stack_Label):
    print("Reset button clicked!")
    if input_box.get().strip():
        input_box.delete(0, END)
    if tracing_text.get(1.0, END).strip():
        tracing_text.delete(1.0, END)
    currentState_Label.config(text="")
    steps_Label.config(text="")
    traceInput_Label.config(text="")
    stack_Label.config(text="")


###########################################################################
#                 FRONTEND
###########################################################################

# The parent frontend window that shows all buttons and information needed to show
def create_window():
    input_string = StringVar()  # input string variable

    window.title("1-way 1-stack Deterministic Pushdown Automata")
    window.geometry("1280x640")  # Dimensions

    # File button
    file_button = Button(window, text="Open File", command=lambda: openFile(machine_text))

    # Controls
    controls_frame = LabelFrame(window, text="Controls")
    run_button = Button(controls_frame, text="Run(Full speed)",
                        command=lambda: run_action(input_box, currentState_Label, steps_Label, traceInput_Label,
                                                   tracing_text, stack_Label))
    step_button = Button(controls_frame, text="Step",
                         command=lambda: step_action(input_box, currentState_Label, steps_Label, traceInput_Label,
                                                     tracing_text, stack_Label))
    reset_button = Button(controls_frame, text="Reset",
                          command=lambda: reset_action(input_box, currentState_Label, steps_Label, traceInput_Label,
                                                       tracing_text, stack_Label))

    # Input String
    input_frame = LabelFrame(window, text="Please input the string:")
    input_box = Entry(input_frame, textvariable=input_string, width=20)

    # Current State
    currentState_frame = LabelFrame(window, text="Current State")
    currentState_Label = Label(currentState_frame, text="*")

    # Steps
    steps_frame = LabelFrame(window, text="Steps")
    steps_Label = Label(steps_frame, text="0")

    # Input String
    traceInput_frame = LabelFrame(window, text="Input String")
    traceInput_Label = Label(traceInput_frame, text="N/A")

    # Stack String
    stack_frame = LabelFrame(window, text="Stack")
    stack_Label = Label(stack_frame, text="[]")

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
    machine_frame.grid(row=5, rowspan=7, column=3, columnspan=7, padx=10, pady=10)
    tracing_frame.grid(row=5, rowspan=7, column=12, columnspan=7, padx=10, pady=10)

    # Arrange buttons in a grid layout within their own respective LabelFrame
    run_button.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    step_button.grid(row=1, column=0, padx=5, pady=5)
    reset_button.grid(row=1, column=1, padx=5, pady=5)
    input_box.grid(row=0, column=0, padx=5, pady=5)
    currentState_Label.grid(row=0, column=0, padx=5, pady=5)
    steps_Label.grid(row=0, column=0, padx=5, pady=5)
    traceInput_Label.grid(row=0, column=0, padx=5, pady=5)
    stack_Label.grid(row=0, column=0, padx=5, pady=5)
    machine_text.grid(row=0, column=0, padx=5, pady=5)
    tracing_text.grid(row=0, column=0, padx=5, pady=5)
    tracing_text.config(width=60, height=20)
    machine_text.config(width=60, height=20)
    stack_Label.config(width=120)
    traceInput_Label.config(width=120)

    # Shows the Window
    window.mainloop()


def main():
    create_window()


if __name__ == '__main__':
    main()
