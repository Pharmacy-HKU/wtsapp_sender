# -*- coding: UTF-8 -*-
from selenium import webdriver
import csv
import time
import itertools  
  
message_head = str("Dear")
messagesss = str(",%0aThank you for your support to “COVID-19 vaccines Adverse events Response and Evaluation (CARE) Programme: Intensive Monitoring” of the Department of Pharmacology and Pharmacy, HKU. We are following up on vaccine recipients about any adverse reactions you have. We will follow-up on the 1, 2, 3 days and 1, 2, 4 weeks after your dose of vaccine.%0a-------%0aWe sent out the online survey link to you via SMS or email this morning. The survey will only take 2 minutes. It would be appreciated if you can spare a few minutes to let us know your current conditions. %0a-------%0a*Or you can also reply with your adverse reactions or reply “No adverse reactions or unusual symptoms” to our WhatsApp to complete the survey.*%0a---------%0a*Please disregard this message if you have already completed the survey.* Thank you for your time and participation.%0a---------%0aAll data collected will be used for research anonymously.%0aAs a token of appreciation, you will receive an HKD50 supermarket e-voucher upon completion of first dose surveys, and another HKD100 supermarket e-voucher after the completion of second dose surveys.%0aPlease do not hesitate to contact us at email: carehk@hku.hk, phone:2831 5110, or reply our WhatsApp with any questions you may have.")
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
                link = 'https://web.whatsapp.com/send?phone='+ contato + '&text=' + 'Dear Mr/Ms ' +name + self.mensagem
                self.driver.get(link)
                time.sleep(8)
                chat_box = self.driver.find_element_by_class_name('_1E0Oz')
                chat_box.click()
                time.sleep(1)
            except:
                pass
            

bot = WhatsappBot()
bot.SendMessages()
