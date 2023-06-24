from search_engines import Yahoo
import time
import requests
import pandas as pd
import json
import os

import third


def second():
    f = open("task.txt", "r").readlines()
    f1 = "".join(f)
    f1 = f1.split()
    u = pd.read_csv("db.csv")
    t1 = time.time()
    engine = Yahoo()
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
    if name1 != "":
        g = list(u["имя хранилища"])
        y = os.path.exists(f"{g[len(g) - 1]}.txt")
        if y == True:
            k1 = open(f"{g[len(g) - 1]}.txt", "r").readlines()
            k2 = "".join(k1)
            k3 = k2.split()
            name2 = os.path.exists(f"{name1}.json")
            if name1 not in k3 and name2 != True:
                with open(f"db_{p[len(p) - 1]}.txt", "a+") as file:
                    file.write(f'{dt}\n')
                with open(f"{g[len(g) - 1]}.txt", "a+") as f:
                    f.write(f'{name1}\n')
                with open(f"{name1}.json", "a+") as f:
                    f.write(df3)
                third.third()
            else:
                print("?!?!?")
        else:
            print("???")
            third.third()
    else:
        print("???")
        third.third()