from search_engines import Google
import requests
import time
import json
import pandas as pd
import os

import second

def first():
    f = open("task.txt","r").readlines()
    f1 = "".join(f)
    f1 = f1.split()
    if len(f1) != 0 and len(f1) == 1:
        print("Работа пошла!)")
        l = str(input("имя хранилища :"))
        if l != "":
            u = pd.read_csv("db.csv")
            p = list(u["имя хранилища"])
            if l not in p:
                u = u.append({"имя хранилища": l}, ignore_index=True)
                u = u.loc[:, ~u.columns.str.contains('^Unnamed')]
                u.to_csv("db.csv", index=True)
                t1 = time.time()
                engine = Google()
                result = engine.search(f1[0])
                res = result.links()[0:30]
                t2 = time.time()
                dt = t2 - t1
                p = list(u["имя хранилища"])
                id = [int(i) for i in range(len(res))]
                work = []
                nums = [0 for i in range(len(res))]
                for i in res:
                    try:
                        r = requests.get(i)
                        work.append("+")
                    except requests.exceptions.ConnectionError:
                        work.append("-")
                    except requests.exceptions.ReadTimeout:
                        work.append("-")
                df = pd.DataFrame({})
                df["id"] = id
                df["results"] = res
                df["work"] = work
                df["nums"] = nums
                df1 = df.to_json()
                df2 = json.loads(df1)
                print(json.dumps(df2, indent=len(df2)))
                df3 = json.dumps(df2, indent=len(df2))
                name1 = str(input("Введите имя таблицы:"))
                name2 = os.path.exists(f"{name1}.json")
                if name1 != "" and name2 != True:
                    with open(f"db_{p[len(p) - 1]}.txt", "a+") as file:
                        file.write(f'{dt}\n')
                    g = list(u["имя хранилища"])
                    with open(f"{g[len(g) - 1]}.txt", "a+") as f:
                        f.write(f'{name1}\n')
                    with open(f"{name1}.json", "a+") as f:
                        f.write(df3)
                    second.second()
                else:
                    print("???")
                    second.second()
            else:
                exit("Такая БД есть! Попробуйте еще раз!")
        else:
            print("???")
            second.second()
    else:
       print("???")

