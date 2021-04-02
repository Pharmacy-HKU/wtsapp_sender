# -*- coding: UTF-8 -*-
import PySimpleGUI as sg
from selenium import webdriver
import csv
import time
import itertools  


sg.theme('DarkAmber')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Pls select your chrome driver (for message sending)')],
            [sg.Input(sg.user_settings_get_entry('-drivename-', ''), key='-driveplace-'), sg.FileBrowse(size=(10, 1), file_types=(("exe", "chromedriver.exe"),))],
            [sg.Text('Pls select your content file in csv')],
            [sg.Input(sg.user_settings_get_entry('-filename-', ''), key='-IN-'), sg.FileBrowse(size=(10, 1), file_types=(("CSV", "*.csv"),)), sg.Button('Read')], 
            [sg.Radio('Chinese', "RADIO1", default=True, key="-C2-"),sg.Radio('English', "RADIO1")],
            [sg.Text('Time for QR scan(s):'),sg.Slider(key="-Slider1-",range=(1, 50), orientation='h', size=(20, 10), default_value=18, tick_interval=25)],
            [sg.Text('Time for msg loading(s):'),sg.Slider(key="-Slider2-",range=(1, 15), orientation='h', size=(20, 10), default_value=5, tick_interval=5)],
            [sg.Output(size=(60,10), key='-OUTPUT-')],
            [sg.Button("Send"),sg.VerticalSeparator(),sg.Button('Exit')]]

# Create the Window
window = sg.Window('Care Project - 4 : Whatapps sender', layout)

# Send the message

def main():
    class WhatsappBot:
        def __init__(self):
            self.t1 = t1
            self.t2 = t2
            self.contatos = users
            self.names = names
            self.mensagem = messagesss
            options = webdriver.ChromeOptions()
            options.add_argument('lang=en-US')
            self.driver = webdriver.Chrome(executable_path = drivepath)

        def SendMessages(self):
            linkWhatsAppCheck = 'https://web.whatsapp.com/'
            self.driver.get(linkWhatsAppCheck)
            time.sleep(t1)
            for (contato,name) in itertools.zip_longest(self.contatos,self.names):
                try:
                    link = 'https://web.whatsapp.com/send?phone='+ contato + '&text=' + '尊敬的 ' +name + " "+ self.mensagem
                    self.driver.get(link)
                    time.sleep(t2)
                    chat_box = self.driver.find_element_by_class_name('_1E0Oz')
                    chat_box.click()
                    time.sleep(1)
                except:
                    pass
            print("\nThe message sending are finished.")
    bot = WhatsappBot()
    bot.SendMessages()


# Event Loop to process "events"

while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == "Read":
        try:
            filename = values["-IN-"]
            drivepath = values["-driveplace-"]
            with open(r"{}".format(filename), encoding='UTF-8') as f:
                users = []
                names = []
                rows = csv.reader(f,delimiter=",",lineterminator="\n")
                next(rows, None)
                for row in rows:
                    user = row[1]
                    users.append(user)
                    name = row[0]
                    names.append(name)
            lenofname = len(names)
            message_hint = "There are "+str(lenofname)+" people waiting for their messages.\nThe first name is " + str(names[0]) + "\nThe last name is "+ str(names[-1])+"\nPls check the csv if the information are not correct."
            window['-OUTPUT-'].update(message_hint)
        except:
            sg.Popup('No or wrong file!\nCall FM, plz.')
    
    if event == "Send":
        try:
            if values["-C2-"]==True:
                message_head = str("尊敬的")
                messagesss = str("先生/女士：%0a感謝您對香港大學李嘉誠醫學院藥理及藥劑學系「香港2019冠狀病毒病疫苗的藥物警戒計劃：社區安全監察項目」的支持，協助我們跟進市民在接種疫苗後的異常反應。我們會於接種疫苗後第1、2、3天及第1、2、4星期關注您的健康狀況。%0a-------%0a我們早上經短信或電郵發送了問卷的鏈接，問卷只需約2分鐘完成，希望您能抽空回應，讓我們了解您現時的狀況。%0a-------%0a*或者若您沒有異常反應或特別症狀，您可以直接在此回覆”沒有異常反應或特別症狀” 來完成問卷。*%0a---------%0a*若您已完成並已提交了今天的問卷，則不用理會這信息*。感謝您的時間和參與。%0a---------%0a所有收集的資料將僅用於匿名研究，只有參與此項目的研究人員才能讀取。%0a為答謝您的參與，完成第一劑問卷後我們會向參加者送出超市的$50電子禮券，完成第二劑問卷後會再向參加者送出超市的$100電子禮券。%0a如有任何疑問，請通過 carehk@hku.hk、致電 2831 5110、或回覆WhatsApp，與我們聯絡。")
            else:
                message_head = str("Dear")  
                messagesss = str("先生/女士：%0a感謝您對香港大學李嘉誠醫學院藥理及藥劑學系「香港2019冠狀病毒病疫苗的藥物警戒計劃：社區安全監察項目」的支持，協助我們跟進市民在接種疫苗後的異常反應。我們會於接種疫苗後第1、2、3天及第1、2、4星期關注您的健康狀況。%0a-------%0a我們早上經短信或電郵發送了問卷的鏈接，問卷只需約2分鐘完成，希望您能抽空回應，讓我們了解您現時的狀況。%0a-------%0a*或者若您沒有異常反應或特別症狀，您可以直接在此回覆”沒有異常反應或特別症狀” 來完成問卷。*%0a---------%0a*若您已完成並已提交了今天的問卷，則不用理會這信息*。感謝您的時間和參與。%0a---------%0a所有收集的資料將僅用於匿名研究，只有參與此項目的研究人員才能讀取。%0a為答謝您的參與，完成第一劑問卷後我們會向參加者送出超市的$50電子禮券，完成第二劑問卷後會再向參加者送出超市的$100電子禮券。%0a如有任何疑問，請通過 carehk@hku.hk、致電 2831 5110、或回覆WhatsApp，與我們聯絡。")
            t1 = int(values['-Slider1-'])
            t2 = int(values['-Slider2-'])
            main()
        except:
            sg.Popup('Wrong input or enviornment!\nCall FM, plz.')
window.close()