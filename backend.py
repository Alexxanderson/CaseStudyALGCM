import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


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

    states = dpdaFile_data['States']
    alphabet_inputs = dpdaFile_data['Alphabet Inputs']
    stack_alphabets = dpdaFile_data['Stack Alphabets']
    start_state = dpdaFile_data['Start State']
    starting_stack_symbol = dpdaFile_data['Starting Stack Symbol']
    final_states = dpdaFile_data['Final States']
    transitions = dpdaFile_data['Transitions']

    print("File Read")

    print("States:", states)
    print("Alphabet Inputs:", alphabet_inputs)
    print("Stack Alphabets:", stack_alphabets)
    print("Start State:", start_state)
    print("Starting Stack Symbol:", starting_stack_symbol)
    print("Final States:", final_states)
    print("Transitions:", transitions)

    input_string = input("Input String to be read: ")
    print(input_string)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
