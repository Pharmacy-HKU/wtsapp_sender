# -*- coding: UTF-8 -*-
import PySimpleGUI as sg
from selenium import webdriver
import csv
import time
import itertools  
from datetime import datetime
from datetime import timedelta
import openpyxl
import sys
import re
# Waiting
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

sg.theme('DarkAmber')   # Add a little color to your windows

# All the stuff inside your window. This is the PSG magic code compactor...
layout = [ [sg.Text('Pls select your chrome driver (for message sending)')],
            [sg.Input(sg.user_settings_get_entry('-drivename-', ''), key='-driveplace-'), sg.FileBrowse(size=(10, 1), file_types=(("exe", "chromedriver.exe"),))],
            [sg.Text('Pls select your content file in csv or xlsx')],
            [sg.Input(sg.user_settings_get_entry('-filename-', ''), key='-IN-'), sg.FileBrowse(size=(10, 1), file_types=(("CSV", "*.csv"),("Excel","*xlsx"),)), sg.Button('Read')], 
            [sg.Text('Reminder:'),sg.Radio('Chn', group_id="RADIO1", default=True, key="-C1-"),
                                     sg.Radio('Eng', group_id="RADIO1", key ="-C2-")],
                                     [sg.Text("2nd dose checking:"),sg.Radio("Chn", group_id="RADIO1", key ="-C3-"),
                                     sg.Radio("Eng", group_id="RADIO1", key ="-C4-")],
            [sg.Text('Time for QR scanning:'),sg.Slider(key="-Slider1-",range=(1, 50), orientation='h', size=(20, 10), default_value=15)],
            #[sg.Text('Time for msg loading:'),sg.Slider(key="-Slider2-",range=(1, 15), orientation='h', size=(20, 10), default_value=5)],
            #[sg.Text('Time after msg loading:'),sg.Slider(key="-Slider3-",range=(1, 10), orientation='h', size=(20, 10), default_value=2)],
            [sg.Output(size=(65,10), key='-OUTPUT-')],
            [sg.Button("Send"),sg.VerticalSeparator(),sg.Button('Exit'),sg.VerticalSeparator(),sg.Button("Help"),
             sg.Text("Pls contact FM for any bugs.")]]

# Create the Window
window = sg.Window('Care Project Whatapps Sender - v6.1', layout)

def main():
    class WhatsappBot:
        def __init__(self):
            self.t1 = t1
#            self.t2 = t2
#            self.t2 = t2
            self.contatos = users
            self.names = names
            self.mensagem = messagesss
            self.click_number = 0
            options = webdriver.ChromeOptions()
            options.add_argument('lang=en-US')
            options.add_argument('disable-infobars');
            options.add_argument("disable-notifications");
            options.add_argument("disable-popup-blocking");
            prefs = {'profile.default_content_setting_values' :  {  'notifications' : 2  }  }
            options.add_experimental_option("prefs",prefs)
            self.driver = webdriver.Chrome(executable_path = drivepath)
            self.driver.implicitly_wait(30) 
        def SendMessages(self):
            wait = WebDriverWait(self.driver, 30 ,1) # Set a waiting time of 30 seconds for elements loading
            self.driver.get('https://web.whatsapp.com/') # Get into the wtsapp login-in page 
            time.sleep(t1)
            success_phone_number = list() 
            success_name = list()
            for (contato,name) in itertools.zip_longest(self.contatos,self.names): # loop the name number
                #should_restart = True # Set a indicator of fail sending 
                # Keep a record for those successful name and number
                #while should_restart: # If fail sending, the sending process will be restarted
                try:
                    link = 'https://web.whatsapp.com/send?phone='+ contato + '&text=' + message_head +name + " "+ self.mensagem
                    self.driver.get(link)
                    self.driver.execute_script("window.onunload=null; window.onbeforeunload=null")
                    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_3QfZd"))) # until the page finished loading
                    time.sleep(1)
                    chat_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_1E0Oz'))) # until the chat box is loaded
                    time.sleep(1) 
                    chat_box.click() # click the send button 
                    time.sleep(1)
                    elements_for_last_msg = "div[class='_11liR'] div[class*='GDTQm'][class*='message-out'] div[class='UFTvj'] span[class='_17Osw']" # get the time of last msg 
                    if len(elements_for_last_msg)>0:
                        # get the time of last msg 
                        time_in_page =str(self.driver.find_elements_by_css_selector(elements_for_last_msg)[-1].get_attribute('innerHTML'))
                        if bool(re.search('下午|PM|晚上|pm',time_in_page)):
                            time_in_page_remove_original_AMPM = ''.join(list(filter(lambda ch: ch in '0123456789:', time_in_page))) + " PM"
                            time_in_page_formatted = datetime.strptime(time_in_page_remove_original_AMPM,"%I:%M %p")
                        elif bool(re.search('上午|AM|中午|am',time_in_page)):
                            time_in_page_remove_original_AMPM = ''.join(list(filter(lambda ch: ch in '0123456789:', time_in_page))) + " AM"
                            time_in_page_formatted = datetime.strptime(time_in_page_remove_original_AMPM,"%I:%M %p")
                        else:
                            time_in_page_formatted = datetime.strptime(time_in_page,"%H:%M")
                        send_time = time_in_page_formatted
                        time_margin = timedelta(minutes = 1)
                        present_time = datetime.strptime(datetime.now().strftime("%H:%M"),"%H:%M") # The current time 
                        # if the sending time for last msg is not far from the current time, means the msg has been successful sent.
                        if present_time - time_margin <= send_time <= present_time + time_margin:
                            #should_restart = False
                            self.click_number = self.click_number + 1
                            success_phone_number.append(contato)
                            success_name.append(name)
                        else:
                            next
                    else:
                        next
                except:
                    continue 
            self.driver.quit()
            fail_names = [x for x in self.names if x not in success_name]
            if len(fail_names)>0:
                warning_after_finish = "\n"+str(self.click_number)+"/"+str(lenofname)+" message has been sent. \nPls check the following msg:\n"+','.join(fail_names)+"\n\n"
                sg.Popup(warning_after_finish,title='')
            else:
                warning_after_finish = "\nThe message sending is finished.\n"+str(self.click_number)+"/"+str(lenofname)+" message has been sent.\n\n"
                sg.Popup(warning_after_finish)
            message_hint = window['-OUTPUT-'].get() + "\n"
            message_hint = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))+warning_after_finish+ message_hint
            window['-OUTPUT-'].update(message_hint)
  #  try:
    bot = WhatsappBot()
    bot.SendMessages()
#    except:
 #       sg.Popup('Wrong input or enviornment!\nCall FM, plz.')
# Event Loop to process "events"
while True:             
    event, values = window.read()
    if event == "Help":
        layout_help1 = [
                        [sg.Text("This is a app for automatically sending whatsapp messages to the Care project - 4 participants.\n Pls DO NOT circulate for other purpose.")],
                        [sg.Text("1.	Pls ensure you have the content file (csv), bulk sender(Care Watspp sender v1.exe) and the chrome drive (chromedriver.exe) in your PC.")],
                        [sg.Image(r'./image/pic1.png')],
                        [sg.Text("2.	Prepare your content files in csv format. The data structure looks like the following pic:")],
                        [sg.Image(r'./image/pic2.png')],
                        [sg.Text("Pls remember to add the 852 in front of the telephone number.\nPls remember to save the file into csv UTF-8 format,\notherwise it may show the Chinese character incorrectly.\n Now the v2 support the excel file.")],
                        [sg.Image(r'./image/pic3.png')],
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
                                [sg.Image(r'./image/pic4.png')],
                                [sg.Text("5.	Some meta info will be shown below. Pls check if the number and name are correct.")],
                                [sg.Image(r'./image/pic5.png')],
                                [sg.Text("6.	After double check, click Send. There will be a fake chrome coming out with whatsapp webpage.")],
                                [sg.Image(r'./image/pic6.png')],
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
            elif "xlsx" in filename: 
                book = openpyxl.load_workbook(filename)
                sheet = book.active
                names = []
                users = []
                for name in sheet['A']:
                    names.append(name.value)
                for phone in sheet['B']:
                    users.append(str(phone.value))
                names = names[1:]
                users = users[1:]
            lenofname = len(names)
            message_hint = window['-OUTPUT-'].get() + "\n"
            message_hint = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))+"\nThere are "+str(lenofname)+" people waiting for their messages.\nThe first name is " + str(names[0]) + "\nThe last name is "+ str(names[-1])+"\nPls check the file if the information is not correct.\n\n" + message_hint
            window['-OUTPUT-'].update(message_hint)
        except:
            sg.Popup('No or wrong file!\nCall FM, plz.')
    
    if event == "Send":
        if values["-C1-"]==True:
            message_head = str("尊敬的 ")
            #messagesss = str("go")
            messagesss = str("先生/女士：%0a感謝您對香港大學李嘉誠醫學院藥理及藥劑學系「香港2019冠狀病毒病疫苗的藥物警戒計劃：社區安全監察項目」的支持，協助我們跟進市民在接種疫苗後的異常反應。我們會於接種疫苗後第1、2、3天及第1、2、4星期關注您的健康狀況。%0a-------%0a我們早上經短信或電郵發送了問卷的鏈接，問卷只需約2分鐘完成，希望您能抽空回應，讓我們了解您現時的狀況。%0a-------%0a*或者若您沒有異常反應或特別症狀，您可以直接在此回覆”沒有異常反應或特別症狀” 來完成問卷。*%0a---------%0a*若您已完成並已提交了今天的問卷，則不用理會這信息*。感謝您的時間和參與。%0a---------%0a所有收集的資料將僅用於匿名研究，只有參與此項目的研究人員才能讀取。%0a為答謝您的參與，完成第一劑問卷後我們會向參加者送出超市的$50電子禮券，完成第二劑問卷後會再向參加者送出超市的$100電子禮券。%0a如有任何疑問，請通過 carehk@hku.hk、致電 2831 5110、或回覆WhatsApp，與我們聯絡。")
        elif values["-C2-"]==True:
            message_head = str("Dear ")
            messagesss = str(",%0aThank you for your support to “COVID-19 vaccines Adverse events Response and Evaluation (CARE) Programme: Intensive Monitoring” of the Department of Pharmacology and Pharmacy, HKU. We are following up on vaccine recipients about any adverse reactions you have. We will follow-up on the 1, 2, 3 days and 1, 2, 4 weeks after your dose of vaccine.%0a-------%0aWe sent out the online survey link to you via SMS or email this morning. The survey will only take 2 minutes. It would be appreciated if you can spare a few minutes to let us know your current conditions. %0a-------%0a*Or you can also reply with your adverse reactions or reply “No adverse reactions or unusual symptoms” to our WhatsApp to complete the survey.*%0a---------%0a*Please disregard this message if you have already completed the survey.* Thank you for your time and participation.%0a---------%0aAll data collected will be used for research anonymously.%0aAs a token of appreciation, you will receive an HKD50 supermarket e-voucher upon completion of first dose surveys, and another HKD100 supermarket e-voucher after the completion of second dose surveys.%0aPlease do not hesitate to contact us at email: carehk@hku.hk, phone:2831 5110, or reply our WhatsApp with any questions you may have.")
        elif values["-C3-"]==True:
            message_head = str("尊敬的 ")
            messagesss = str("先生/女士：%0a因應第二劑疫苗的新安排，麻煩請回答以下問題，以助我們更新紀錄。%0a%0a請問您 *是否已經* 接種了 *第二劑* 新冠疫苗？%0a--> 如未有，請回答 %0a1.*「未」*%0a2. *第二劑接種日期:* %0a%0a--> 如 *已經接種*，請回答以下問題：%0a1. *第二劑接種日期：*%0a2. *任何異常反應* 或回覆 *'沒有異常反應或特別症狀'* %0a%0a非常感謝您的時間和參與！")
        elif values["-C4-"]==True:
            message_head = str("Dear ")
            messagesss = str(",%0aTo allow arrangement for follow-up on your second-dose, please reply with the following information. %0a%0a*Have you received second dose of COVID-19 vaccine?* %0a--> If _*not*_, please answer the following:%0a1. *'Not yet'* %0a2. *Date* of your second dose:%0a%0a--> If _*yes*_, please reply the following:%0a1. *Date* of your second dose:%0a2. *Any adverse reactions* or reply *'No adverse reactions or unusual symptoms'* %0a%0aThank you for your time and participation.")
        t1 = int(values['-Slider1-'])
        #t2 = int(values['-Slider2-'])
        #t3 = int(values['-Slider3-'])
        main()
        
window.close()

