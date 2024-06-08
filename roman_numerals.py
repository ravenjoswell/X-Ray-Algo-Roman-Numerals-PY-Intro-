def to_roman(num):
    output = ""
    roman_numeral_arabic = {
        "M" : 1000,
        "CM": 900,
        "D" : 500, 
        "CD": 400,
        "C" : 100, 
        "L" : 50, 
        "XL": 40,
        "X" : 10, 
        "IX": 9, 
        "V" : 5, 
        "IV": 4,
        "I" : 1, 
    }
    # goal is get a key , value out of a dict
    for roman, arabic in roman_numeral_arabic.items():
        temp = num // arabic
        if temp == 0:
            continue
        
        num -= temp * arabic
        output += roman * temp
       
    return output 


print(to_roman(944))
 