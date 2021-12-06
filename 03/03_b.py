file = open("03_input.txt","r")

values = file.readlines()
values_original = values.copy()
columns = len(values[0])
total = len(values)

digit_count = [0,0]


def get_most_common(i):
    if i> (total/2):
        return 1
    return 0

def get_least_common(i):
    if i> (total/2):
        return 0
    return 1

def binaryToDecimal(binary):
    total = 0
    count = 0
    for digit in reversed(binary):
        total += int(digit)*  2 ** count
        count+=1
    return total

values_copy = values.copy()

for i in range(0,columns-1):
    
    # count the number of 0 and 1 digits
    digit_count=[0,0]
    for value in values_copy:
        digit_count[int(value[i])]+=1
        
    # if 0 has more entries than 1
    if digit_count[0] > digit_count[1]:
        for value in values:
            if digit_count[0] < 0: break
            if int(value[i]) == 0: digit_count[0]-=1
            if int(value[i]) != 0: values_copy.remove(value)
            
    # if 1 has more or the same entries than 0
    elif digit_count[1] >= digit_count[0]:
        for value in values:
            if digit_count[1] < 0: break
            if int(value[i]) == 1: digit_count[1]-=1
            if int(value[i]) != 1: values_copy.remove(value)
    
    values = values_copy.copy()
    if(len(values_copy)) == 1: break       

oxygen_generator_rating = binaryToDecimal(values[0].strip())

values = values_original.copy()
values_copy = values.copy()

for i in range(0,columns-1):
    
    # count the number of 0 and 1 digits
    digit_count=[0,0]
    for value in values_copy:
        digit_count[int(value[i])]+=1
        
    # if 0 has more entries than 1
    if digit_count[0] <= digit_count[1]:
        for value in values:
            if digit_count[0] < 0: break
            if int(value[i]) == 0: digit_count[0]-=1
            if int(value[i]) != 0: values_copy.remove(value)
            
            
    # if 1 has more or the same entries than 0
    elif digit_count[1] < digit_count[0]:
        for value in values:
            if digit_count[1] < 0: break
            if int(value[i]) == 1: digit_count[1]-=1
            if int(value[i]) != 1: values_copy.remove(value)

    values = values_copy.copy()
    if(len(values_copy)) == 1: break       

co2_scrubber_rating = binaryToDecimal(values[0].strip())

print("Life support rating: ", oxygen_generator_rating * co2_scrubber_rating)
