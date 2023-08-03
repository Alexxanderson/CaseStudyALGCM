# imports tkinter
from tkinter import *
from tkinter import filedialog


window = Tk()


def openFile():
    print("Open File Button Clicked!")


def run_action():
    print("Run button clicked!")


def pause_action():
    print("Pause button clicked!")


def step_action():
    print("Step button clicked!")


def reset_action():
    print("Reset button clicked!")


def enter_action():
    print("Enter Button Clicked!")


def create_window():
    input_string = StringVar()

    window.title("1-way 1-stack Deterministic Pushdown Automata")
    window.geometry("864x640")

    file_button = Button(window, text="Open File", command=openFile)

    # Controls
    controls_frame = LabelFrame(window, text="Controls")
    run_button = Button(controls_frame, text="Run", command=run_action)
    pause_button = Button(controls_frame, text="Pause", command=pause_action)
    step_button = Button(controls_frame, text="Step", command=step_action)
    reset_button = Button(controls_frame, text="Reset", command=reset_action)

    # Input String
    input_frame = LabelFrame(window, text="Please input the string:")
    input_box = Entry(input_frame, textvariable=input_string, width=30)

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

    # GridStyle Formatting
    file_button.grid(row=0, column=0, columnspan=2)

    controls_frame.grid(row=2, column=0, rowspan=3, columnspan=2, padx=10, pady=10, sticky="nsew")
    input_frame.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    currentState_frame.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    steps_frame.grid(row=10, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    traceInput_frame.grid(row=0, column=3, rowspan=2, columnspan=17, padx=10, pady=10)
    stack_frame.grid(row=3, column=3, columnspan=17, padx=10, pady=10)

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

    # Shows the Window
    window.mainloop()


def main():
    print("Yo")
    create_window()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
