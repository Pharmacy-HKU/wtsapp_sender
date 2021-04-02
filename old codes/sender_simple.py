# -*- coding: UTF-8 -*-

import PySimpleGUI as sg
from selenium import webdriver
import csv
import time
import itertools  
  


message_head = str("尊敬的")
messagesss = str("先生/女士：%0a感謝您對香港大學李嘉誠醫學院藥理及藥劑學系「香港2019冠狀病毒病疫苗的藥物警戒計劃：社區安全監察項目」的支持，協助我們跟進市民在接種疫苗後的異常反應。我們會於接種疫苗後第1、2、3天及第1、2、4星期關注您的健康狀況。%0a-------%0a我們早上經短信或電郵發送了問卷的鏈接，問卷只需約2分鐘完成，希望您能抽空回應，讓我們了解您現時的狀況。%0a-------%0a*或者若您沒有異常反應或特別症狀，您可以直接在此回覆”沒有異常反應或特別症狀” 來完成問卷。*%0a---------%0a*若您已完成並已提交了今天的問卷，則不用理會這信息*。感謝您的時間和參與。%0a---------%0a所有收集的資料將僅用於匿名研究，只有參與此項目的研究人員才能讀取。%0a為答謝您的參與，完成第一劑問卷後我們會向參加者送出超市的$50電子禮券，完成第二劑問卷後會再向參加者送出超市的$100電子禮券。%0a如有任何疑問，請通過 carehk@hku.hk、致電 2831 5110、或回覆WhatsApp，與我們聯絡。")
filesss = str("name.csv")



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

def main():
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
            
if __name__ == '__main__':
    main()


THREAD_EVENT = '-THREAD-'
cp = sg.cprint
def the_thread(window):
    """
    The thread that communicates with the application through the window's events.

    Once a second wakes and sends a new event and associated value to the window
    """
    i = 0
    while True:
        time.sleep(1)
        window.write_event_value('-THREAD-', (threading.current_thread().name, i))      # Data sent is a tuple of thread name and counter
        cp('This is cheating from the thread', c='white on green')
        i += 1

def main():
    """
    The demo will display in the multiline info about the event and values dictionary as it is being
    returned from window.read()
    Every time "Start" is clicked a new thread is started
    Try clicking "Dummy" to see that the window is active while the thread stuff is happening in the background
    """

    layout = [  [sg.Text('Output Area - cprint\'s route to here', font='Any 15')],
                [sg.Multiline(size=(65,20), key='-ML-', autoscroll=True, reroute_stdout=True, write_only=True, reroute_cprint=True)],
                [sg.T('Input so you can see data in your dictionary')],
                [sg.Input(key='-IN-', size=(30,1))],
                [sg.B('Start A Thread'), sg.B('Dummy'), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout, finalize=True)

    while True:             # Event Loop
        event, values = window.read()
        cp(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event.startswith('Start'):
            threading.Thread(target=the_thread, args=(window,), daemon=True).start()
        if event == THREAD_EVENT:
            cp(f'Data from the thread ', colors='white on purple', end='')
            cp(f'{values[THREAD_EVENT]}', colors='white on red')
    window.close()

