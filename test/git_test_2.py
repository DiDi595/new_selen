import time

def main():
    money = 1000
    korovki = 0
    kurotki = 0
    while True:
        try:
            print("--------------------------")
            print('Игра "Коровки и Курочки"')
            choise = int(input("1.Начать.\n"
                               "2.Помощь.\n"
                               "3.Выход.\n"
                               "Выбор: "))
            if choise == 1:
                game(money, korovki, kurotki)
            elif choise == 2:
                print("У Вас есть ферма. Вы можете покупать коровок или курочек за небольшую сумму.\n"
                      "Если Вы покупаете какое либо животное, после каждого действия Вам нужно подождать пока животные дадут деньги.\n"
                      "Для пропуска действия, нажмите Enter.\n"
                      "Одна коровка вам дает 100 рублей прибыли за 3 секунды\n"
                      "Одна курочка дает Вам 50 рублей прибыли за 1 секунду\n"
                      "НЕ НАЖИМАЙТЕ КЛАВИШИ, ПОКА ЖИВОТНЫЕ ДЕЛАЮТ ДЕНЬГИ!")
            elif choise == 3:
                exit("Пока!")
        except ValueError as error:
            print(f"\nОшибка.\nКод ошибки:\n{error}")

def game(money, korovki, kurotki):
    while True:
        if korovki > 0:
            print(f"\033[32mПодождите, коровки делают деньги...\033[0m")
            money += korovki * 100
            time.sleep(1)
            print(f"Коровки сделали {korovki * 100} рублей!")
        if kurotki > 0:
            print(f"\033[31mПодождите, курочки делают деньги...\033[0m")
            money += kurotki * 50
            print(f"Курочки сделали {kurotki * 50} рублей!")
        try:
            print("-----------------------")
            print(f"У Вас {money} рублей, {korovki} коровок и {kurotki} куротек.")
            choise = int(input("Что будем делать?\n1. Купить коровок (1000р).\n2. Купить курочек (500р).\n3. Выход\nВыбор: "))
            print("-----------------------")
            if choise == 1:
                if money >= 1000:
                    money -= 1000
                    korovki += 1
                    print("Молодец! Купил целых 1 коровок!!!")
                elif money < 1000:
                    print("Ай! Нехорошо обманывать!")
            elif choise == 2:
                if money >= 500:
                    money -= 500
                    kurotki += 1
                    print("Мои поздравления!!! Купил 1 кучотек!!!")
                elif money < 500:
                    print("Тебя мама не учила не обманывать?")
            elif choise == 3:
                exit_what = int(input("Вы точно хотите выйти?\n1. Да\n2. Нет\nВыбор:  "))
                if exit_what == 1:
                    exit("Пока!")
        except ValueError as error:
            pass

if __name__ == '__main__':
    main()