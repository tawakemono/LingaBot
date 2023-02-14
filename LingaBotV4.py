from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

Qlist = []
Alist = []



def login(loginid,loginpass):
    try:
        #リンガポルタのページへ行く
        driver.get('https://w5.linguaporta.jp/user/seibido/')
        wait. until(EC.presence_of_all_elements_located)#すべての要素が表示されるまで待機

        #IDを入力
        element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/table/tbody/tr[1]/td/input")#elementに入力欄のパスを代入
        element.clear()#入力欄の中を削除
        element.send_keys(loginid)#自分のログインID

        #passを入力
        element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/table/tbody/tr[2]/td/input")
        element.clear()
        element.send_keys(loginpass)#自分のパスワード

        #ログインボタンを押す
        element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/form/table/tbody/tr[3]/td/div/input")
        driver.execute_script('arguments[0].click();', element)#ボタンを押す
#        print("Can Login")

    except:
        print("Cannot login")


def selectcoset():
    try:
        #本の選択画面へ移行
        wait. until(EC.presence_of_all_elements_located)
        element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/dl/dt[2]/form/a")
        driver.execute_script('arguments[0].click();', element)

        #coset2600を選択
        wait. until(EC.presence_of_all_elements_located)
        element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/form/div/div[2]/div[3]/input")
        driver.execute_script('arguments[0].click();', element)
#        print("Can go cosset page")

    except:
        print("Incorrect password")
        print("Cannot go coset page")



def selectUnit(unit_num):
    #ユニット選択
    wait. until(EC.presence_of_all_elements_located)
    unit_num = (unit_num)/25
    script = "select_unit('drill', '" + str(1810 + (unit_num)*4) + "', '');"
    try:
        driver.execute_script(script)
    except:
        print("Cannot select Unit")


def Answer():
    #回答
    wait.until(EC.presence_of_all_elements_located)
    try:
        question = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/div/div[2]")
        question = str(question.text)
        if(question in Qlist):
            print("question in Qlist")
            #Qlistから問題番号を取得
            i = Qlist.index(question)
            a=i
            print("listnum = "+str(a))

            #Alistから答えを取得
            anser = Alist[i]
            anser = str(anser)
            anser = anser.replace(" ","")
            print("question = "+question)
            print("anser = "+anser)

            #答えを入力
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/div/div[3]/div/input")
            element.clear
            element.send_keys(anser)

            #回答ボタンを押す
            wait. until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/input[3]")))
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/input[3]")
            driver.execute_script('arguments[0].click();', element)

            #次へ進を押す
            WebDriverWait(driver, 10). until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form/input[1]")))
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form/input[1]")
            driver.execute_script('arguments[0].click();', element)
            print("正解")

        else:
            print("question not in Qlist")
            print("question = "+question)
            #回答欄に適当な答えを入力
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/div/div[3]/div/input")
            element.clear
            element.send_keys("a")

            #回答ボタンを押す
            wait. until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/input[3]")))
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/input[3]")
            driver.execute_script('arguments[0].click();', element)

            #正解を見るを押す
            wait. until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form[1]/input[2]")))
            wait.until(EC.presence_of_all_elements_located)
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form[1]/input[2]")
            driver.execute_script('arguments[0].click();', element)

            #問題の答えを入手
            wait. until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form/input[1]")))
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form[1]/div/div[3]/input")
            anser = element.get_attribute("value")
            Alist.append(str(anser))
            Qlist.append(question)

            #次に進むを押す
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form/input[1]")
            driver.execute_script('arguments[0].click();', element)

            #print(Alist)
            #print(Qlist)

        return(0)


    except:
        print("Cannot Anser")
        return(1)

def CheckUnitEnd():
    #ユニットが終わっているかの確認
    wait. until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td/div[3]/form/input")))
    try:
        element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td")
        botti = str(element.text)
        botti = botti.replace(" ","")
        if(botti == "問題が有りません。"):
            return(1)
        else:
            return(0)
    except:
        return(1)



json_file = open("data.json","r")

json_dict = json.load(json_file)

print("自分のIDを入力してください")
loginid = str(input())
print("ログインパスワードを入力してください")
loginpass = str(input())

while(1):
    print("開始する番号を入力して下さい")
    Unitnum = int(input())
    if Unitnum % 25 == 1:
        Unitnum = Unitnum + 24
        break
    else:
        print("無効な番号です。入力しなおして下さい。")

while(1):
    print("終了する番号を入力して下さい")
    Unitnum_end = int(input())
    if Unitnum_end % 25 == 0:
        Unitnum_end = Unitnum_end + 25
        break
    else:
        print("無効な番号です。入力しなおして下さい。")


while(1):
    if(Unitnum >= Unitnum_end):
        print("指定されたUnitまでの解答が完了しました")
        break
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Now    "+str(Unitnum-24)+"->"+str(Unitnum))
    #Chromeを開く
    options = Options()
    #options.add_argument('--headless')
    options.add_argument('--disable-logging')
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    #タイムアウトの時間を設定
    wait = WebDriverWait(driver, 20)
    login(loginid,loginpass)
    selectcoset()
    selectUnit(Unitnum)
    a = CheckUnitEnd()
    Alist = json_dict["Answerlist"+str(Unitnum-24)+"_"+str(Unitnum)]
    Qlist = json_dict["Qestionlist"+str(Unitnum-24)+"_"+str(Unitnum)]
    if(a == 1):
        print("This unit is already done")
        Qlist.clear()
        Alist.clear()
        Unitnum = Unitnum+25
        driver.close()
        continue
    while(1):
        print("======================================")
        b = 0
        b = Answer()
        if(b == 1):
            break