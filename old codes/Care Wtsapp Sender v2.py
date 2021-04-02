# -*- coding: UTF-8 -*-
import PySimpleGUI as sg
from selenium import webdriver
import csv
import time
import itertools  
from datetime import datetime
from pandas import read_excel

sg.theme('DarkAmber')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Pls select your chrome driver (for message sending)')],
            [sg.Input(sg.user_settings_get_entry('-drivename-', ''), key='-driveplace-'), sg.FileBrowse(size=(10, 1), file_types=(("exe", "chromedriver.exe"),))],
            [sg.Text('Pls select your content file in csv or excel')],
            [sg.Input(sg.user_settings_get_entry('-filename-', ''), key='-IN-'), sg.FileBrowse(size=(10, 1), file_types=(("CSV", "*.csv"),("Excel","*xlsx"),("Excel","*xls"),)), sg.Button('Read')], 
            [sg.Text('Msg Language'),sg.Radio('Chinese', "RADIO1", default=True, key="-C2-"),sg.Radio('English', "RADIO1")],
            [sg.Text('Time for QR scan(s):'),sg.Slider(key="-Slider1-",range=(1, 50), orientation='h', size=(20, 10), default_value=18, tick_interval=25)],
            [sg.Text('Time for msg loading(s):'),sg.Slider(key="-Slider2-",range=(1, 15), orientation='h', size=(20, 10), default_value=5, tick_interval=5)],
            [sg.Output(size=(65,10), key='-OUTPUT-')],
            [sg.Button("Send"),sg.VerticalSeparator(),sg.Button('Exit'),sg.VerticalSeparator(),sg.Button("Help"),
             sg.Text("Pls contact FM (minfan@connect.hku.hk) for any bugs.")]]

# Create the Window
window = sg.Window('Care Project - 4 : Whatapps sender - designed by fm - v2', layout)


# Second window for help file


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
                    link = 'https://web.whatsapp.com/send?phone='+ contato + '&text=' + message_head +name + " "+ self.mensagem
                    self.driver.get(link)
                    time.sleep(t2)
                    chat_box = self.driver.find_element_by_class_name('_1E0Oz')
                    chat_box.click()
                    time.sleep(1)
                except:
                    pass
            self.driver.quit()
            sg.Popup("\nThe message sending is finished.")
            message_hint = window['-OUTPUT-'].get() + "\n"
            message_hint = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))+"\nThe message sending is finished.\n\n" +message_hint
            window['-OUTPUT-'].update(message_hint)
    bot = WhatsappBot()
    bot.SendMessages()


# Event Loop to process "events"

while True:             
    event, values = window.read()
    if event == "Help":
        layout_help1 = [
                        [sg.Text("This is a app for automatically sending whatsapp messages to the Care project - 4 participants.\n Pls DO NOT circulate for other purpose.")],
                        [sg.Text("1.	Pls ensure you have the content file (csv), bulk sender(Care Watspp sender v1.exe) and the chrome drive (chromedriver.exe) in your PC.")],
                        [sg.Image(r'C:/Users/Fan Min/OneDrive - connect.hku.hk/Projects/cov19/Care 4 whatsapp bulk sender/pic1.png')],
                        [sg.Text("2.	Prepare your content files in csv format. The data structure looks like the following pic:")],
                        [sg.Image(r'C:/Users/Fan Min/OneDrive - connect.hku.hk/Projects/cov19/Care 4 whatsapp bulk sender/pic2.png')],
                        [sg.Text("Pls remember to add the 852 in front of the telephone number.\nPls remember to save the file into csv UTF-8 format,\notherwise it may show the Chinese character incorrectly.\n Now the v2 support the excel file.")],
                        [sg.Image(r'C:/Users/Fan Min/OneDrive - connect.hku.hk/Projects/cov19/Care 4 whatsapp bulk sender/pic3.png')],
                        [sg.Button("Next")]
        ]
        window2 = sg.Window("Help_1-CARE 4", layout_help1, modal=True)
        while True:
            event2, values2 = window2.read()
            if event2 == "Exit" or event2 == sg.WIN_CLOSED:
                break
            elif event2 == "Next": 
                window2.close()
                layout_help2 = [
                                [sg.Text("4.	Select the chrome driver & Your content file and press Read button. ")],
                                [sg.Image(r'C:/Users/Fan Min/OneDrive - connect.hku.hk/Projects/cov19/Care 4 whatsapp bulk sender/pic4.png')],
                                [sg.Text("5.	Some meta info will be shown below. Pls check if the number and name are correct.")],
                                [sg.Image(r'C:/Users/Fan Min/OneDrive - connect.hku.hk/Projects/cov19/Care 4 whatsapp bulk sender/pic5.png')],
                                [sg.Text("6.	After double check, click Send. There will be a fake chrome coming out with whatsapp webpage.")],
                                [sg.Image(r'C:/Users/Fan Min/OneDrive - connect.hku.hk/Projects/cov19/Care 4 whatsapp bulk sender/pic6.png')],
                                [sg.Button("Next")]
                                ]
                window3 = sg.Window("Help_2-CARE 4", layout_help2, modal=True)
                while True:
                    event3, values3 = window3.read()
                    if event3 == "Exit" or event3 == sg.WIN_CLOSED:
                        window3.close()
                        break
                    elif event3 =="Next":
                        window3.close()
                        layout_help3 = [
                                        [sg.Text("7.	Scan with you whatspp and just wait. The message will be automatically sent to the people. \nKEEP your whatsapp ONLINE. \nYou can do whatever you want with your PC, \nbut it will be great if you allocate all your RAM to the sender app.")],
                                        [sg.Text("Pls let me know if there are any bugs.")],
                                        [sg.Button("Close")]
                                        ]
                        window4 = sg.Window("Help_3-CARE 4", layout_help3, modal=True)
                        while True:
                            event4, values4 = window4.read()
                            if event4 == "Close" or event4 == sg.WIN_CLOSED:
                                window4.close()
                                break
    
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == "Read":
        try:
            filename = values["-IN-"]
            drivepath = values["-driveplace-"]
            if "csv" in filename:
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
            elif "xls" in filename or "xlsx" in filename: 
                users = []
                names = []
                rows = read_excel(filename)    
                users = [str(x) for x in rows.iloc[:,1].tolist()]
                names = rows.iloc[:,0].tolist()
            lenofname = len(names)
            message_hint = window['-OUTPUT-'].get() + "\n"
            message_hint = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))+"\nThere are "+str(lenofname)+" people waiting for their messages.\nThe first name is " + str(names[0]) + "\nThe last name is "+ str(names[-1])+"\nPls check the file if the information is not correct.\n\n" + message_hint
            window['-OUTPUT-'].update(message_hint)
        except:
            sg.Popup('No or wrong file!\nCall FM, plz.')
    
    if event == "Send":
        try:
            if values["-C2-"]==True:
                message_head = str("尊敬的 ")
                messagesss = str("先生/女士：%0a感謝您對香港大學李嘉誠醫學院藥理及藥劑學系「香港2019冠狀病毒病疫苗的藥物警戒計劃：社區安全監察項目」的支持，協助我們跟進市民在接種疫苗後的異常反應。我們會於接種疫苗後第1、2、3天及第1、2、4星期關注您的健康狀況。%0a-------%0a我們早上經短信或電郵發送了問卷的鏈接，問卷只需約2分鐘完成，希望您能抽空回應，讓我們了解您現時的狀況。%0a-------%0a*或者若您沒有異常反應或特別症狀，您可以直接在此回覆”沒有異常反應或特別症狀” 來完成問卷。*%0a---------%0a*若您已完成並已提交了今天的問卷，則不用理會這信息*。感謝您的時間和參與。%0a---------%0a所有收集的資料將僅用於匿名研究，只有參與此項目的研究人員才能讀取。%0a為答謝您的參與，完成第一劑問卷後我們會向參加者送出超市的$50電子禮券，完成第二劑問卷後會再向參加者送出超市的$100電子禮券。%0a如有任何疑問，請通過 carehk@hku.hk、致電 2831 5110、或回覆WhatsApp，與我們聯絡。")
            else:
                message_head = str("Dear ")
                messagesss = str(",%0aThank you for your support to “COVID-19 vaccines Adverse events Response and Evaluation (CARE) Programme: Intensive Monitoring” of the Department of Pharmacology and Pharmacy, HKU. We are following up on vaccine recipients about any adverse reactions you have. We will follow-up on the 1, 2, 3 days and 1, 2, 4 weeks after your dose of vaccine.%0a-------%0aWe sent out the online survey link to you via SMS or email this morning. The survey will only take 2 minutes. It would be appreciated if you can spare a few minutes to let us know your current conditions. %0a-------%0a*Or you can also reply with your adverse reactions or reply “No adverse reactions or unusual symptoms” to our WhatsApp to complete the survey.*%0a---------%0a*Please disregard this message if you have already completed the survey.* Thank you for your time and participation.%0a---------%0aAll data collected will be used for research anonymously.%0aAs a token of appreciation, you will receive an HKD50 supermarket e-voucher upon completion of first dose surveys, and another HKD100 supermarket e-voucher after the completion of second dose surveys.%0aPlease do not hesitate to contact us at email: carehk@hku.hk, phone:2831 5110, or reply our WhatsApp with any questions you may have.")
            t1 = int(values['-Slider1-'])
            t2 = int(values['-Slider2-'])
            main()
        except:
            sg.Popup('Wrong input or enviornment!\nCall FM, plz.')
window.close()

