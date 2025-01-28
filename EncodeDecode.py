def encode(string):
    # 3D cube structure with characters
    cube = [[["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
            [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
            [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", " "]]
           ]
    result = []
    
    # Iterate through each character in the input string
    for i in string:
        # Traverse the 3D cube
        for layerid, layer in enumerate(cube):
            for rowid, row in enumerate(layer):
                for colid, char in enumerate(row):
                    # If the character matches, generate the encoded position
                    if i == char:
                        # Create the position in the format: "." * (colid + 1), "." * (rowid + 1), "." * (layerid + 1)
                        a = " ".join(["." * (colid + 1), "." * (rowid + 1), "." * (layerid + 1)])
                        result.append(a)
    
    # Return the encoded string by joining the results with a space
    return " ".join(result)

def decode(string):
    # 3D cube structure with characters
    cube = [[["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
            [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
            [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", " "]]
           ]
    
    mc = []
    # Split the input string into individual parts based on space
    letters = string.split()
    
    # Iterate through the letters in chunks of 3 (each chunk represents the position of one character)
    for i in range(0, len(letters), 3):
        # Get the layer, row, and column lengths based on the number of dots in each position
        layer = len(letters[i])
        row = len(letters[i + 1])
        col = len(letters[i + 2])
        
        # Adjust the indexes to match the cube structure (subtract 1 to get 0-based indexes)
        layerid = layer - 1
        rowid = row - 1
        colid = col - 1
        
        # Append the decoded character from the cube to the result list
        mc.append(cube[layerid][rowid][colid])
    
    # Join the decoded characters into a string and return the result
    return "".join(mc)
