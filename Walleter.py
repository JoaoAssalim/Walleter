import os

if not os.path.isdir(os.getcwd() + f'\\PythonWallet.txt'):
    wallet = open('PythonWallet.txt', 'w')
    wallet.write('0.00')
    wallet.close()

print('[1] - See Extract\n[2] - Add Money\n[3] - Remove Money\n[4] - Reset wallet')
option = input('-> ')

if option.isdigit():
    option = int(option)
    if option == 1:
        wallet = open('PythonWallet.txt', 'r')
        print(f'Your Amount is: ${wallet.read()}')
        wallet.close()
    
    elif option == 2:
        print('Enter just the value, without "$,€,R$..."\nIf the value contains cents, use "." and not "," \n')
        earnedAmount = input('How many did you earn: ')
        try:
            earnedAmount = float(earnedAmount)
            #Sum earned value with old amount
            wallet = open('PythonWallet.txt', 'r')
            for amount in wallet:
                newAmount = float(amount) + earnedAmount
            wallet.close()
            #write new amount
            wallet = open('PythonWallet.txt', 'w')
            wallet.write(f'{round(newAmount,2)}')
            wallet.close()
            #show att amount
            wallet = open('PythonWallet.txt', 'r')
            print(f'Your Amount is: ${wallet.read()}')
            wallet.close()
        except ValueError as e:
            print('Error: ', e)

    elif option == 3:
        print('Enter just the value, without "$,€,R$..."\nIf the value contains cents, use "." and not "," \n')
        earnedAmount = input('How many do you want remove: ')
        try:
            earnedAmount = float(earnedAmount)
            #Sum earned value with old amount
            wallet = open('PythonWallet.txt', 'r')
            for amount in wallet:
                if earnedAmount <= float(amount):
                    newAmount = float(amount) - earnedAmount
                    #write new amount
                    wallet = open('PythonWallet.txt', 'w')
                    wallet.write(f'{round(newAmount,2)}')
                    wallet.close()
                else:
                    print('Value is greater than your wallet!')
            wallet.close()

            #show att amount
            wallet = open('PythonWallet.txt', 'r')
            print(f'Your Amount is: ${wallet.read()}')
            wallet.close()
        except ValueError as e:
            print('Error: ', e)

    elif option == 4:
        #reset wallet
        wallet = open('PythonWallet.txt', 'w')
        wallet.write('0.00')
        wallet.close()
        #show amount
        wallet = open('PythonWallet.txt', 'r')
        print(f'Amount Reseted: ${wallet.read()}')
        wallet.close()