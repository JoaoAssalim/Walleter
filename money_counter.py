import os
from colorama import Fore

print(Fore.BLUE+'To type a Float value use "." not ","!\n')
acount_option = input('"D" to delet money / "A" to add money: ').upper()

if acount_option == 'A':
    safed_money = input(Fore.CYAN+'How much do you earned today: ')
    print()
    safed_money = float(safed_money) if safed_money.isdigit() and float(safed_money) > 0 else print(Fore.RED+'ENTER A VALUE GREATER THAN 0\n')

    #if the "money.txt" is nule, it add a zero value
    if os.stat("money.txt").st_size == 0:
        with open('money.txt', 'a') as none_money:
            none_money.write('$0.00') 
    try:
        #get the latest value in money.txt separet de simbols and sum with the newest value
        with open('money.txt', 'r') as last_money:
            for i in last_money:
                last_safed_money = i
            value_money = last_safed_money.split("$")
        value_money = float(value_money[1])
        new_value_money = value_money + safed_money

        #Delet the oldest value
        with open("money.txt","r+") as money:
            counted_money = money.readlines()
            money.seek(0)
            for line in counted_money:
                if last_safed_money not in line:
                    money.write(line)
            money.truncate()

        #add the newest value
        with open('money.txt', 'a') as new_money:
            new_money.write(f'${new_value_money:.2f}')

        print(Fore.GREEN+f'Your wallet has: ${new_value_money:.2f}')
    except:
            print(Fore.YELLOW+'Sorry, I cannot do it for you ;(')

elif acount_option == 'D':
    #delet the latest value and add '$0.00'
    with open("money.txt","r+") as money:
        money.truncate(0)
        money.write('$0.00')
    print(Fore.MAGENTA+'Your wallet is zero!')
else:
    print(Fore.RED+'Invalid Option!')