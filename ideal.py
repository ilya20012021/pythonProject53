import pandas as pd
import numpy as np
import os
def search():
    df = pd.read_csv("db.csv")
    col = list(df["имя хранилища"])
    d = str(input("Введите имя БД для дальнейшей работы:"))
    if d in col:
        d1 = os.path.exists(f"{d}.txt")
        if d1 == True:
            f = open(f"{d}.txt", "r").readlines()
            f1 = "".join(f)
            f2 = f1.split()
            if len(f2) == 4:
                print("Анализ стартовал...")
                dd1 = pd.read_json(f"{f2[0]}.json")
                dd2 = pd.read_json(f"{f2[1]}.json")
                dd3 = pd.read_json(f"{f2[2]}.json")
                dd4 = pd.read_json(f"{f2[3]}.json")
                d1 = max(list(dd1["nums"]))
                d2 = max(list(dd2["nums"]))
                d3 = max(list(dd3["nums"]))
                d4 = max(list(dd4["nums"]))
                a = []
                a.append(d1)
                a.append(d2)
                a.append(d3)
                a.append(d4)
                x = pd.DataFrame({"n": a})
                r = x.loc[x["n"] == x["n"].max()]
                kl = r.index
                sd = []
                for i in kl:
                    sd.append(i)
                tik = open(f"db_{d}.txt", "r").readlines()
                tik1 = "".join(tik)
                tik2 = tik1.split()
                znach = tik2.index(min(tik2))
                data = pd.DataFrame({"x1": [0, 0, 0, 0],
                                     "x2": [0, 0, 0, 0]})

                for i in sd:
                    data.at[i, "x1"] = 1

                data.at[znach, "x2"] = 1
                x3 = np.array(list(data["x1"])) * np.array(list(data["x2"]))
                data["answer"] = x3
                x = list(data["x1"])
                y = list(data["x2"])
                z = list(data["answer"])
                data1 = pd.DataFrame({"x1": x,
                                      "x2": y,
                                      "answer": z}, index=["Google", "Yahoo", "Duckduckgo", "ask"])
                print("Итог:")
                print(data1)
                print("---------------")
                cl = data1.loc[data1["answer"] == 1]
                if (len(cl["answer"]) > 0):
                    print("Ответ найден")
                    print(cl)
                else:
                    print("Поиск прошел не идеально")

            else:
                print("невозможно провести анализ")

        else:
            print("???")
    else:
        print("???")
