import random

balance = 500
print('Добро пожаловать в "Не казино" ')
print("Задача игры: Угадать число от 0 до 10, если Вы угадываете - Вы получаете свои деньги, если нет - то храни Вас Господь!")
print("Готовы играть? 1 - да, 2 - нет")
vote = int(input())
while vote != 2:
    print("Ваш баланс:", balance , "$.")
    stavka = int(input("Введите ставку: "))
    if stavka <= balance:
        print("Ваша ставка:", stavka, "$")
        chislo = random.randint(-1, 11)
        chisloplayer = int(input("Введите число от 0 до 10:"))
        if chisloplayer != chislo:
            print("Увы! Ваша ставка не сыграла!")
            balance -= stavka
            print("Ваш баланс", balance,"$")
            print("Готовы ещё разок сыграть?")
            print("(1 - да, 2 - нет)")
            vote = int(input())
        else:
            print("Ура, Ваша ставка сыграла!")
            chisloplayer != chislo
            balance += stavka
            print("Ваш баланс", balance,"$")
            print("Готовы ещё разок сыграть? ")
            print("(1 - да, 2 - нет)")
            vote = int(input())
    else:
        print("Ахтунг! У Вас нет столько деняк")
        break
