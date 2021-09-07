"""Is Isogram"""
def is_isogram(string):
    #your code here
    if string == "":
        return True
    
    string = string.lower()
    sorted_str = sorted(string)
    list_string = list(string)
    
    str_length = len(list_string)
    for num in range(0, str_length+1):
        if str_length == num:
            return True
        elif string.count(string[num]) > 1:
            return False
