# Program to code and decode messages

code = {
    "1": "9",
    "2": "8",
    "3": "7",
    "4": "6",
    "5": "0"
}

def code_and_decode_msg():
    coded_message = input("Please, enter your message: ")
    decoded_message = []

    for c in coded_message:
        if c in code.keys():
            decoded_message.append(code[c])
        elif c in code.values():
            for k, v in code.items():
                if c == v:
                    decoded_message.append(k)
                    break
        else:
            decoded_message.append(c)

    print("".join(decoded_message))


code_and_decode_msg()