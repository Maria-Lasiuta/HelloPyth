from random import randint

#рахунок : k-комп'ютер g-гравець
def rock_paper_scissors(choice):
    # вибір гравця  камінь- 3,ножниці-2, папір - 1
    k = 0
    g = 0
    for a in choice:
        l = randint(1, 3)
        if a > l:
            g += 1
        elif a == 1 and l == 3:
            g += 1
        elif l == 1 and a == 3:
            k += 1
        elif l > a:
            k += 1
        print(f'computer - {l},gamer - {a}, {k}:{g}')
    print(k, g)
    if k > g:
        return f" Переміг комп'ютер, наступного разу пощастить."
    elif g > k:
        return f" Переміг гравець,вітаю!!"
    else:
        return f" Перемогла дружба - нічия."
choice = []
i = 0
for i in range(1,4):
    choice.append(int(input('Введіть число(1-3) відповідно до:'
                            '1-папір,2-ножиці,3-камінь: ')))
    i += 1
print(rock_paper_scissors(choice))
   
        
