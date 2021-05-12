# this line of code checks whether the phone number is an actual nigerian phone numnber that starts with a +234
# check whether the number is 14 digits 
# check whether the number starts with a +234
# check if all the digits after the plus sign is a decimal number 

def isNumber(num): 
    # checks if the length of the nnumber is 14 
    if len(num) != 14:
        print("This is not a valid nigerian number check whether you forgot to add a plus or something.")
    # checks if there is a plus sign
    if num[0] != '+':
        print('Your number is meant to start with a plus')
    
    #checks if the first three numbers after the plus sign is 234
    if num [1] != '2' and num [2] != '3'  and num [3] != '4': 
        print('This is not a Nigerian number')

    #Checks if there all the strings theere are decimals 
    for i in range(1, 14): 
        if not num[i].isdecimal():
            return 'This is not a nigerian Number'

    return 'This is  a Nigerian Number'

print(isNumber('+2348ab6790029'))
    
    