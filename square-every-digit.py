"""Square Every Digit"""
def square_digits(num):
    
    num = map(int, str(num))
    
    num = list(num)
    
    squared_num = "".join(number ** 2 for number in num)
    
    return squared_num
