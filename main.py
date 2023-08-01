# imports tkinter
from tkinter import *


def create_window():
    window = Tk()
    window.title("1-way 1-stack Deterministic Pushdown Automata")
    window.geometry("864x640")

    label1 = Label(window, text="Label 1")
    label2 = Label(window, text="Label 2")
    button = Button(window, text="Click Me!")

    file_button = Button(window, text="File")
    input_button = Button(window, text="Input")

    attribute_editor_button = Button(window, text="Edit")
    add_state_button = Button(window, text="Add State")
    add_transition_button = Button(window, text="Add Transition")
    remove_state_button = Button(window, text="Remover")

    file_button.grid(row = 0, column = 0)
    input_button.grid(row = 0, column = 1)

    button.grid(row=1, column=0, columnspan=2, sticky="we")
    window.mainloop()


def main():
    print("Yo")
    create_window()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
