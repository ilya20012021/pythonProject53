import json
import webbrowser

import pandas as pd

import os

def science():
    r = str(input("Введите имя БД для работы:"))
    if r != "":
        df = pd.read_csv("db.csv")
        c = list(df["имя хранилища"])
        if r in c:
            z = os.path.exists(f"{r}.txt")
            if z == True:
                f = open(f"{r}.txt", "r").readlines()
                f1 = "".join(f)
                f2 = f1.split()
                h = str(input("Введите имя таблицы для дальнейшей работы:"))
                if h in f2:
                    d = pd.read_json(f"{h}.json")
                    s = str(input("Введите строку, соответствующую вашему сайту:"))
                    if s.isdigit():
                        s = int(s)
                        if (0 <= s < len(d["work"])):
                            if (d.at[s, "work"] != "-"):
                                webbrowser.open(d.at[s, "results"])
                                d.loc[s, "nums"] += 1
                            else:
                                print("???")
                        else:
                            print("Нет строки!")

                        df1 = d.to_json()
                        df2 = json.loads(df1)
                        print(json.dumps(df2, indent=len(df2)))
                        df3 = json.dumps(df2, indent=len(df2))
                        with open(f"{h}.json", "a+") as f:
                            f.truncate(0)
                        with open(f"{h}.json", "a+") as f:
                            f.write(df3)

                    else:
                        print("???")
                else:
                    print("???")
            else:
                print("???")
        else:
            print("???")
    else:
        print("???")