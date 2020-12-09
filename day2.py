#part1
inputs = my_string.split(",")
#inputs = [1,0,0,0,99]
inputs = [int(x) for x in inputs]
inputs[1] = 12
inputs[2] = 2
counter = 0
for entry in inputs[::4]:
    if entry == 99:
        print(inputs[0])
        break
    elif entry == 1:
        result = inputs[inputs[counter+1]] + inputs[inputs[counter+2]]
        inputs[inputs[counter+3]] = result
    elif entry == 2:
        result = inputs[inputs[counter+1]] * inputs[inputs[counter+2]]
        inputs[inputs[counter+3]] = result
    counter += 4



#part2
desired_output = 19690720
output_found = False

counter1 = 0
counter2 = -1
while output_found == False:
    inputs = my_string.split(",")
    inputs = [int(x) for x in inputs]
    counter = 0
    if counter2 == 99:
        counter2 = -1
        counter1 += 1
    inputs[1] = counter1
    inputs[2] = counter2
    counter2 += 1
    for entry in inputs[::4]:
        if entry == 99:
            if inputs[0] == desired_output:
                print(100 * inputs[1] + inputs[2])
                output_found = True
            break
        elif entry == 1:
            result = inputs[inputs[counter+1]] + inputs[inputs[counter+2]]
            inputs[inputs[counter+3]] = result
        elif entry == 2:
            result = inputs[inputs[counter+1]] * inputs[inputs[counter+2]]
            inputs[inputs[counter+3]] = result
        counter += 4
        

