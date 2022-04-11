def to_camel_case(text):
    
    list = text.replace("-", " ").replace("_", " ")
    
    list = list.split()
    
    if len(text) == 0:
        
        return text
    
    return list[0] + ' '.join(list[1:]).title().replace(" ", "")
