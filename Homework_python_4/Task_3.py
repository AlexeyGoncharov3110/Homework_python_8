# Задача_3
# Возьмите задачу о банкомате из семинара 2. 
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления
# и снятия средств в список.

balance = 0
def check_balance(balance):
    print(f'Ваш текущий баланс: {balance} рублей".format(balance)')
def deposit(balance, amount):
    balance += amount
    print(f'Сумма {amount} рублей успешно внесена на счет.".format(amount)')
    return balance

def withdraw(balance, amount):
    if balance >= amount:
        balance -= amount
        print(f'Сумма {amount} рублей успешно снята со счета.format(amount)')
    else:
        print("На вашем счете недостаточно средств.")
    return balance
def atm():
    balance = 0
while True:
    print("Добро пожаловать в банкомат!")
    print("Выберите действие:")
    print("1. Проверить баланс")
    print("2. Внести деньги")
    print("3. Снять деньги")
    print("4. Выйти")
    choice = input("Введите номер действия: ")
    if choice == "1":
        check_balance(balance)
    elif choice == "2":
        amount = float(input("Введите сумму для внесения: "))
        balance = deposit(balance, amount)
    elif choice == "3":
        amount = float(input("Введите сумму для снятия: "))
        balance = withdraw(balance, amount)
    elif choice == "4":
        print("Спасибо за использование нашего банкомата!")
        break
    else:
        print("Неверный ввод. Повторите попытку.")
atm()