# this line of code checks whether the phone number is an actual nigerian phone numnber that starts with a +234
# check whether the number is 14 digits 
# check whether the number starts with a +2348146790029
# check if all the digits after the plus sign is a decimal number 

def isPhoneNumber(text): 
    # checks if the length of the nnumber is 14 
    if len(text) != 14:
        return("This is not a valid nigerian number check whether you forgot to add a plus or something.")
    # checks if there is a plus sign
    if text[0] != '+':
        return('Your number is meant to start with a plus')
    
    #checks if the first three numbers after the plus sign is 234
    if text[1] != '2' and text[2] != '3'  and text[3] != '4': 
        return('This is not a Nigerian number')

    #Checks if there all the strings theere are decimals 
    for i in range(0,14): 
        if not text[i].isdecimal():
            return 'This is not a nigerian Number'

    return 'This is  a Nigerian Number'

msg = 'Call me at +2346159790029 or +2346784560016'
foundNumber = False
for i in range(len(msg)):
    chunk = msg[i:i+14] 
    if isPhoneNumber(chunk):
        print(f'A  phone number has been found {chunk}')
        foundNumber = True 
if not foundNumber:
    print('No number could be found ')


#print(isNumber('+2348ab67900c9'))
    
    