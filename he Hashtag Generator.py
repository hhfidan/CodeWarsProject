# Hashtag Generator

def generate_hashtag(s):
    
    a = s.strip().title().replace(" ","")
    
    if not a or len(a) > 139:
        
        return False

    return "#" + a

This function generates a hashtag from a given string. The generated hashtag will:

- Start with a hashtag symbol `#`
- Capitalize the first letter of each word
- Remove any leading or trailing whitespace
- Remove all spaces between words

## Function Explanation

1. The function takes a string input `s`.
2. It removes leading and trailing whitespace using `strip()`.
3. It capitalizes the first letter of each word using `title()`.
4. It removes any spaces between the words using `replace(" ", "")`.
5. If the resulting string is empty or exceeds 139 characters, the function returns `False`.
6. If the resulting string is valid, it appends `#` at the beginning and returns the result.

## Example Usage

```python
print(generate_hashtag(" Hello there thanks for trying my Kata"))
# Output: #HelloThereThanksForTryingMyKata

print(generate_hashtag("    Hello     World   "))
# Output: #HelloWorld

print(generate_hashtag(""))
# Output: False
