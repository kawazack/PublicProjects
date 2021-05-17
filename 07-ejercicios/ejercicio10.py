"""
Exercise 10. The programm needs to get requests how many alumns are in class,
ask user for their marks, saves it in a counter, and finally
print in the screen how many have passed and how many have suspended.

"""
from colorama import init, Fore, Back, Style


iteration_counter=1
alumn_mark=0
counter_approved=0
counter_suspended=0
alumnsinclass = int(input("How many alumns you have in your class?\n"))
while iteration_counter<= alumnsinclass:
    alumn_mark=float(input(f"What is the score of the alumn {iteration_counter}?\n"))
    if alumn_mark >=0 and alumn_mark<5:
            counter_suspended+=1
    elif alumn_mark >=5 and  alumn_mark <=10:
        counter_approved+=1
    else:
        print(f"{Back.RED}{Fore.BLACK} Sorry. This is not a valid input. You are cheating!{Style.RESET_ALL}")
        continue
    iteration_counter+=1

print(f"The alumns that have approved are: {counter_approved}")
print(f"The alumns that have suspended are: {counter_suspended}")