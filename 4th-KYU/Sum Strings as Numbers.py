# https://www.codewars.com/kata/5324945e2ece5e1f32000370 Kata link

def sum_strings(x, y):
    """
    Adds two non-negative integer numbers represented as strings.
    Returns the sum as a string without converting inputs directly to integers.
    """
    
    # Handle empty string cases by treating them as "0"
    if x == "":
        x = "0"
    if y == "":
        y = "0"
    
    # Remove leading zeros
    x = x.lstrip('0')
    y = y.lstrip('0')
    
    # If both strings become empty after stripping, return "0"
    if x == "" and y == "":
        return "0"
    
    # Reverse the strings to process from least significant digit
    x = x[::-1]
    y = y[::-1]
    
    max_len = max(len(x), len(y))  # Find the maximum length
    carry = 0  # Initialize carry for addition
    result = []  # List to store the result digits
    
    # Iterate over each digit and compute sum
    for i in range(max_len):
        
        xi = int(x[i]) if i < len(x) else 0  # Convert character to integer, or 0 if out of range
        yi = int(y[i]) if i < len(y) else 0  
        
        total = xi + yi + carry  # Compute sum including carry
        carry = total // 10  # Compute new carry value
        result.append(str(total % 10))  # Store the current digit
    
    # If there's a carry left, add it to the result
    if carry:
        result.append(str(carry))
    
    # Reverse the result and join as string
    return ''.join(result[::-1])

"""
Alternative version (not optimized for performance):

This version constructs lists from the input strings, reverses them, 
and performs digit-wise addition. However, it is not optimized for efficiency.


def sum_strings(x, y):
    a = [i for i in x][::-1]  # Reverse x
    b = [j for j in y][::-1]  # Reverse y

    # Equalize lengths by padding with zeros
    a.extend(['0'] * (len(b) - len(a)))
    b.extend(['0'] * (len(a) - len(b)))

    l = 0  # Store the sum as an integer
    for i, (ai, bi) in enumerate(zip(a, b)):
        power = 10 ** i  # Calculate power of 10 for position
        l += (int(ai) + int(bi)) * power

    return str(l)  # Convert result back to string
"""
