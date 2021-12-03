file = open("03_input.txt","r")

values = file.readlines()

columns = len(values[0])
total = len(values)

column_count = [0 for i in range(columns-1)]

for value in values:
    for i in range(columns-1):
        column_count[i] += (int(value[i]))


print(column_count)

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
        total += digit*  2 ** count
        count+=1
    return total


gama_rate = []
epsilon_rate = []    

for count in column_count:
    gama_rate.append(get_most_common(count))
    epsilon_rate.append(get_least_common(count))


print("Gama rate: ", gama_rate)
print("Epsilon rate: ", epsilon_rate)

binary_gama_rate = binaryToDecimal(gama_rate)
binary_epsilon_rate = binaryToDecimal(epsilon_rate)

print("Binary Gama rate: ", binary_gama_rate)
print("Binary Epsilom rate: ", binary_epsilon_rate)


print("Power consumption: ", binary_gama_rate * binary_epsilon_rate)
