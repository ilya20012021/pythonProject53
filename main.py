import first
import h
import ideal
import researching

n = 1

while n != 0:

    m = ["Получение данных из поисковых систем(get info 1)","изучение веб-ресурсов(search info 2)","поиск идеального результата(find info 3)","помощь(--help)"]
    for i in m:
        print(i)

    s = str(input())
    if s == "get info 1":
        first.first()
    elif s == "search info 2":
        researching.science()
    elif s == "find info 3":
        ideal.search()
    elif s == "--help":
        h.hh()
    else:
        print("---------------")
    ans = ["да", "нет"]
    ans_n = "/".join(ans)
    print(f"Хотите ли вы продолжить работу с данным ПО?{ans_n}")
    s = str(input("Введите ответ:"))
    if s == ans[0]:
        n += 1
    elif s == ans[1]:
        break
    else:
        print("Ничего непонятно")

