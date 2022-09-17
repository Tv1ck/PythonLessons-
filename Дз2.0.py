import random
startmoney = 10000
count = 0.001

win = 0
loose = 0

games = 0

Баланс = []
Игра = []

Баланс2 = []
Игра2 = []

Баланс3 = []
Игра3 = []

money = startmoney

while money > 0:
    bet = startmoney * count
    if bet > money:
        bet = money
    money -= bet
    
    Баланс.append(money)
    Игра.append(len(Игра)+1)

    ball = random.randint(1,37)
    if ball in range (1,19):
        money += bet * 2
        win += 1
    else:
        loose += 1
Игра = win + loose
print("Выиграно ставок: " + str(win) + " (" + str(win/Игра * 100) + "%). " + " Проиграно ставок: " + str(loose)  + " (" + str(loose/Игра * 100) + "%). ")

win = 0
loose = 0

while (money > 0) and (win + loose < Игра):
    bet = startmoney * count
    if bet > money:
        bet = money
    money -= bet
    
    Баланс2.append(money)
    Игра2.append(len(Игра2)+1)

    ball = random.randint(1,36)
    if ball in range (1,19):
        money += bet * 2
        win += 1
    else:
        loose += 1
print("Выиграно ставок: " + str(win) + " (" + str(win/Игра2 * 100) + "%). " + " Проиграно ставок: " + str(loose)  + " (" + str(loose/Игра2 * 100) + "%). ")

win = 0
loose = 0

while (money > 0) and (win + loose < games):
    bet = startmoney * count
    if bet > money:
        bet = money
    money -= bet

    Баланс3.append(money)
    Игра3.append(len(Игра3)+1)

    ball = random.randint(1,35)
    if ball in range (1,19):
        money += bet * 2
        win += 1
    else:
        loose += 1
print("Выиграно ставок: " + str(win) + " (" + str(win/Игра3 * 100) + "%). " + " Проиграно ставок: " + str(loose)  + " (" + str(loose/Игра3 * 100) + "%). ")
