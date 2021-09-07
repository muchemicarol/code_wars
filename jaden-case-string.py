"""Jaden Case String"""

def to_jaden_case(string):
    # ...
    string = string.split(" ")
    final_string = " ".join(word.capitalize() for word in string)
    
    return final_string
