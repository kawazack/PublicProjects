number_list= []
number = None
while (number != 'done') or (number != 'Done'):
    try:
        number = int(input('What is your number?'))
        number_list.append(number)
        print(type(number))
    except:
        print("Your maximum typed number is: " + str(max(number_list)), "Your minimum typed number is: "+ str(min(number_list)))
        break 
