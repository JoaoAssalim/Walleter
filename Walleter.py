import os
class Walleter:


    def __init__(self):
        print('Welcome to Walleter!\n')
        walleter = open('PythonWallet.txt', 'a')
        if os.stat("PythonWallet.txt").st_size == 0:
            walleter.write('0.00')
        walleter.close()

    def seeExtract(self):
        with open('PythonWallet.txt', 'r') as walletExtract:
            print(f'Your Amount is: ${walletExtract.read()}')

    def addAmount(self):
        print('Enter just the value, without "$,€,R$..."\nIf the value contains cents, use "." and not "," \n')
        earnedAmount = input('How many did you earn: ')
        try:
            earnedAmount = float(earnedAmount)
            #Sum earned value with old amount
            with open('PythonWallet.txt', 'r') as lastAmount:
                for amount in lastAmount:
                    newAmount = float(amount) + earnedAmount
            #write new amount
            with open('PythonWallet.txt', 'w') as wallet:
                wallet.write(str(newAmount))
            #show att amount
            with open('PythonWallet.txt', 'r') as seeExtractWallet:
                print(f'Your Amount is: ${seeExtractWallet.read()}')
        except ValueError as e:
            print('Error: ', e)
    
    def removeAmount(self):
        print('Enter just the value, without "$,€,R$..."\nIf the value contains cents, use "." and not "," \n')
        earnedAmount = input('How many do you want remove: ')
        try:
            earnedAmount = float(earnedAmount)
            #Sum earned value with old amount
            with open('PythonWallet.txt', 'r') as lastAmount:
                for amount in lastAmount:
                    if earnedAmount <= float(amount):
                        newAmount = float(amount) - earnedAmount
                        #write new amount
                        with open('PythonWallet.txt', 'w') as wallet:
                            wallet.write(str(newAmount))
                        
                    else:
                        print('Value is greater than your wallet!')

            #show att amount
            with open('PythonWallet.txt', 'r') as seeExtractWallet:
                print(f'Your Amount is: ${seeExtractWallet.read()}')
        except ValueError as e:
            print('Error: ', e)
        
    def resetAmount(self):
        #reset wallet
        with open('PythonWallet.txt', 'w') as walletReset:
            walletReset.write('0.00')
        #show amount
        with open('PythonWallet.txt', 'r') as wallet:
            print(f'Amount Reseted: ${wallet.read()}')


if __name__ == '__main__':

    walletUser = Walleter()
    print('[1] - See Extract\n[2] - Add Money\n[3] - Remove Money\n[4] - Reset wallet')
    option = input('-> ')

    if option.isdigit():
        option = int(option)
        if option == 1:
            walletUser.seeExtract()
        
        elif option == 2:
            walletUser.addAmount()

        elif option == 3:
            walletUser.removeAmount()

        elif option == 4:
            walletUser.resetAmount()
