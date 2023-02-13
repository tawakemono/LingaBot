


for i in range(5):

    # リストの作成
    my_list = ["あいうえお"+ str(i), "さしすせそ", "たちつてと"]

    filepass = "ansfile/my_list"+ str(i) +".txt"

    # ファイルを開く
    with open(filepass, "w") as f:
        # リストの要素を1行ずつ書き込む
        for item in my_list:
            f.write(str(item) + "\n")

    list = []

    with open(filepass, "r") as file:
        for line in file:
            list.append(str(line.strip()))


    print(list)