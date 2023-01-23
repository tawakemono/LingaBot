from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


Qlist = []
Alist = []


#Chromeを開く
driver = webdriver.Chrome()

#タイムアウトの時間を設定
wait = WebDriverWait(driver, 20)



def login():
    try:
        #リンガポルタのページへ行く
        driver.get('https://w5.linguaporta.jp/user/seibido/')
        wait. until(EC.presence_of_all_elements_located)#すべての要素が表示されるまで待機

        #IDを入力
        element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/table/tbody/tr[1]/td/input")#elementに入力欄のパスを代入
        element.clear()#入力欄の中を削除
        element.send_keys("i32132")#自分のログインID

        #passを入力
        element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/table/tbody/tr[2]/td/input")
        element.clear()
        element.send_keys("123456789")#自分のパスワード

        #ログインボタンを押す
        element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/form/table/tbody/tr[3]/td/div/input")
        element.click()#ボタンを押す

    except:
        print("Cannot login")
        pass


def selectcoset():
    try:
        #本の選択画面へ移行
        wait. until(EC.presence_of_all_elements_located)
        element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/dl/dt[2]/form/a")
        element.click()

        #coset2600を選択
        wait. until(EC.presence_of_all_elements_located)
        element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/form/div/div[2]/div[3]/input")
        element.click()

    except:
        print("Cannot go coset page")
        pass


def selectUnit(unit_num):
    #ユニット選択
    wait. until(EC.presence_of_all_elements_located)
    unit_num = (unit_num)/25
    script = "select_unit('drill', '" + str(1810 + (unit_num)*4) + "', '');"
    try:
        driver.execute_script(script)
    except:
        pass


def ans():
    time.sleep(1)
    wait. until(EC.presence_of_all_elements_located)
    #回答
    try:
        #問題取得
        element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/div/div[2]")
        #Qlistに同じ問題が入っているか確認
        if(element.text in Qlist):
            #答えを入力
            print("Qinst in Q")
            i = Qlist.index(element.text)
            print(i)

            #Alistから答えを取得
            anser = Alist[i]
            anser = str(anser)
            anser = anser.replace(" ","")
            print(anser)

            #答えを入力
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/div/div[3]/div/input")
            element.clear
            element.send_keys(anser)

            #回答ボタンを押す
            time.sleep(1)
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/input[3]")
            element.click()

            #次へ進を押す
            time.sleep(1)
            wait. until(EC.presence_of_all_elements_located)
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form/input[1]")
            element.click()

        else:
            #適当な答えを入力
            Qlist.append(element.text)
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/div/div[3]/div/input")
            element.send_keys("a")

            #回答ボタンを押す
            time.sleep(1)
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/input[3]")
            element.click()

            #正解を見るボタンを押す
            wait. until(EC.presence_of_all_elements_located)
            time.sleep(1)
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form[1]/input[2]")
            element.click()

            #答えをlistへ入れる
            wait. until(EC.presence_of_all_elements_located)
            time.sleep(1)
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form[1]/div/div[3]/input")
            anser = element.get_attribute("value")
            Alist.append(anser)

            #次に進むを押す
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form/input[1]")
            element.click()

            print(Alist)
            print(Qlist)

    except:
        print("ellor")
        return(1)

Unitnum = 100

while(1):

    login()
    selectcoset()
    selectUnit(Unitnum)
    print(Unitnum)
    while(1):
        b=0
        b = ans()
        if(b == 1):
            try:
                plase = "/html/body/div[2]/div/div/table/tbody/tr[4]/td/form[2]/input[2]"
                element = driver.find_element(By.XPATH,plase)
            except:
                break
        else:
            pass


time.sleep(3)

"""
            wait. until(EC.presence_of_all_elements_located)
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form[1]/input[2]")
            element.click()

            wait. until(EC.presence_of_all_elements_located)
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form[1]/div/div[3]/input/value")
            Alist.append(element.text)
            print(Alist)
"""
