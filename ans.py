


for i in range(5):

    # リストの作成
    my_list = ["item"+ str(i), "item2", "item3"]

    filepass = "anslist/my_list"+ str(i) +".txt"

    # ファイルを開く
    with open(filepass, "w") as f:
        # リストの要素を1行ずつ書き込む
        for item in my_list:
            f.write(item + "\n")

    list = []

    with open(filepass, "r") as file:
        for line in file:
            list.append(str(line.strip()))


    print(list)