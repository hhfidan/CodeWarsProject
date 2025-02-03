def valid_braces(string):
    open_braces = ["(", "[", "{"]
    close_braces = [")", "]", "}"]
    opc = {")": "(", "]": "[", "}": "{"}

    list1 = []  # List to hold opening braces

    for value in string:
        if value in open_braces:
            list1.append(value)  # Add opening braces to list1
        elif value in close_braces:
            # If there's a closing brace and list1 is empty, return False
            if not list1:
                return False
            # Check if the last opening brace matches the current closing brace
            last_open = list1[-1]
            if opc[value] != last_open:
                return False
            list1.pop()  # Remove the last opening brace since it matched

    # If there are still unmatched opening braces, return False
    return len(list1) == 0
