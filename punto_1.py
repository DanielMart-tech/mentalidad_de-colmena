# Program for required data

required_info = {} # Object to collect info

def data_input():
    required_data = open("required_data.txt")

    lines = required_data.readlines() # list of lines from file


    for line in lines:
        if line.endswith("*:\n"): # if line ends with '*:\n' indicates required data
            info = input(line)
            while info.strip() == "": # Checking info is not null
                print("Info required")
                info = input(line)
            required_info[line[:len(line) - 3]] = info # Storing info into the required_info object
        elif line.endswith(":\n") and not line.startswith("•"):
            info = input(line)
            required_info[line[:len(line) - 2]] = info
        else:
            print(line)

    required_data.close()