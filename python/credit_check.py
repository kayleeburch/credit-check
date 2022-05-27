def credit_check(string_input):
    credit_num = list(string_input)
    # to_num = list(map(lambda item : int(item), credit_num))
    for i, num in enumerate(credit_num):
        if i % 2 == 0:
            doubled_num = int(num) * 2
            credit_num[i] = str(doubled_num)
            if doubled_num > 9:
                #converted to string, break list to string, digits back into int and them summed
                greater_than_nine = sum([int(a) for a in str(doubled_num)])
                credit_num[i] = str(greater_than_nine)
        
    for i in range(0, len(credit_num)):
        credit_num[i] = int(credit_num[i])

    result = sum(credit_num) % 10 == 0
    if result == False:
        return "The number is invalid!"
    return 'The number is valid!'     
    
# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

