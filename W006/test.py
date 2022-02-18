"""
dcard Sselenium
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  # 鍵盤上案件
import time
from bs4 import BeautifulSoup

path = "C:/Users/user/Desktop/Python/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.dcard.tw/f")
# 使用name來搜尋
search = driver.find_element_by_name("query")
# #輸入文字
# s=input()
search.clear()  # 讓輸入的地方清理乾淨
search.send_keys("巨蟹男")  # 如果沒加time很快關掉
search.send_keys(Keys.RETURN)  # return代表按下enter鍵
time.sleep(3)  # 需要等待因為頁面還在跑沒法一下子就搜到內容

title_container = []
content_container = []
like_container = []
comment_container = []

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sc-3yr054-1"))
    )
    element.click()
    time.sleep(5)


# 根據classname來找標題名 再把它放進一個空間
finally:
    # titles = soup.find_all("h4")
    titles = driver.find_elements_by_class_name("tgn9uw-3")  # 要選很多要用elements只有依樣藥就可以用element
    for title in titles:
        print(title.text)  # 取得title裡的文字
        title_container.append(title.text)

    contents = driver.find_elements_by_class_name("tgn9uw-4")
    for content in contents:  # 如果是這樣做的話 只會看到第一頁的狀態 實際內容不知道
        print(content.text)
        content_container.append(content.text)
    likes = driver.find_element_by_class_name('cgoejl-3')
    for like in likes:
        print(like.text)
        like_container.append(like.text)
    comments = driver.find_element_by_xpath(
        '//*[@id="__next"]/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[3]/article/div[3]/div[2]/div/span')
    for comment in comments:
        print(comment.text)
        comment_container.append(comment.text)
    time.sleep(5)
    driver.quit()

# link點進去
# link = driver.find_element_by_link_text("")    
# link.click() #點網頁
# driver.back() #回到上一頁
# driver.back() #在按一次上一頁
# driver.forward()
print(content_container)
'''implicitly_wait()隱式等待: 隱式等待是一個全局設置，
設置後所有的元素定位都會等待給定的時間，直到元素出現為止，
等待規定時間元素沒出現就報錯。
WebDriverWait()顯示等待: 就是設置一個等待時間，直到這個元素出現就停止等待，
如果沒出現就拋出異常。


page_next = browser.find_element_by_class_name("pageNext")
page_next.click()  # 點擊下一頁按鈕
'''
# driver.set_page_load_timeout(110)
