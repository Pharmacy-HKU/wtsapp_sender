# -*- coding: UTF-8 -*-
from selenium import webdriver
import csv
import time
import itertools  
  
message_head = str("尊敬的")
messagesss = str("先生/女士：%0a感謝您對香港大學李嘉誠醫學院藥理及藥劑學系「香港2019冠狀病毒病疫苗的藥物警戒計劃：社區安全監察項目」的支持，協助我們跟進市民在接種疫苗後的異常反應。我們會於接種疫苗後第1、2、3天及第1、2、4星期關注您的健康狀況。%0a-------%0a我們早上經短信或電郵發送了問卷的鏈接，問卷只需約2分鐘完成，希望您能抽空回應，讓我們了解您現時的狀況。%0a-------%0a*或者若您沒有異常反應或特別症狀，您可以直接在此回覆”沒有異常反應或特別症狀” 來完成問卷。*%0a---------%0a*若您已完成並已提交了今天的問卷，則不用理會這信息*。感謝您的時間和參與。%0a---------%0a所有收集的資料將僅用於匿名研究，只有參與此項目的研究人員才能讀取。%0a為答謝您的參與，完成第一劑問卷後我們會向參加者送出超市的$50電子禮券，完成第二劑問卷後會再向參加者送出超市的$100電子禮券。%0a如有任何疑問，請通過 carehk@hku.hk、致電 2831 5110、或回覆WhatsApp，與我們聯絡。")
filesss = str("name.csv")

users = []
names = []
with open(r"{}".format(filesss), encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = row[1]
        users.append(user)
        name = row[0]
        names.append(name)

class WhatsappBot:
    def __init__(self):
        self.contatos = users
        self.names = names
        self.mensagem = messagesss
        options = webdriver.ChromeOptions()
        options.add_argument('lang=en-US')
        self.driver = webdriver.Chrome(executable_path = 'chromedriver.exe')

    def SendMessages(self):

        linkWhatsAppCheck = 'https://web.whatsapp.com/'
        self.driver.get(linkWhatsAppCheck)
        time.sleep(18)
            
        for (contato,name) in itertools.zip_longest(self.contatos,self.names):
            try:
                link = 'https://web.whatsapp.com/send?phone='+ contato + '&text=' + '尊敬的 ' +name + " "+ self.mensagem
                self.driver.get(link)
                time.sleep(8)
                chat_box = self.driver.find_element_by_class_name('_1E0Oz')
                chat_box.click()
                time.sleep(1)
            except:
                pass
        print("The messages sending are finished")

bot = WhatsappBot()
bot.SendMessages()
