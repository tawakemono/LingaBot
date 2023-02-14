import json

Unitnum = 1

data = {}

Alist = []
Qlist = []

Alist2 = ["aaa","bbb"]
Qlist2 = ["aaa","bbb"]

for i in range(0,103):
    Unitnum = (i * 25) +1
    Qfilepass = "ansfile/Qestionlist"+str(Unitnum)+"_"+str(Unitnum+24)+".txt"
    Afilepass = "ansfile/Anserlist"+str(Unitnum)+"_"+str(Unitnum+24)+".txt"

    with open(Afilepass, "r") as file:
        for line in file:
            Alist.append(str(line.strip()))

    with open(Qfilepass, "r") as file:
        for line in file:
            Qlist.append(str(line.strip()))


    Alist2 = Alist[:]
    Qlist2 = Qlist[:]

    Alist.clear()
    Qlist.clear()

    data["Answerlist"+str(Unitnum)+"_"+str(Unitnum+24)] = Alist2
    data["Qestionlist"+str(Unitnum)+"_"+str(Unitnum+24)] = Qlist2

    print(Alist2)
    print(Qlist2)

    print(data)



# ファイルに書き込む
with open("data.json", "w") as file:
    json.dump(data, file,indent=4)

