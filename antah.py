#Python3 code for Creating voice bot for Corporate Banking

import speech_recognition as sr  #to convert speech to text
import pyttsx3  #to convert text to speech
import mysql.connector  # to connect to mysql database
import time
import random


#main function
def main():
    mydb = mysql.connector.connect(
      host ="localhost",
      user ="root",
      passwd ="sanika",
      database = "voicebot"

    )#creating connection to mysql database

    if(mydb):
        print('*Connection to database Successful*')
    else:
        print('*Connection to database Failed*')

    mycursor = mydb.cursor()
    
    
    
    engine = pyttsx3.init() 
    ta1 = "Welcome to Corporate Banking!"
    print(ta1)
    engine.say(ta1)
    engine.runAndWait()

    voice = sr.Recognizer()


    # Login module:
    str2= ""
    flag = 0
    while (flag==0):
        ta2 = "\nSpeak the access phrase"
        print(ta2)
        engine.say(ta2)
        engine.runAndWait()
        print('Listening...')
        with sr.Microphone() as source:
            audio_text = voice.listen(source)
            text = voice.recognize_google(audio_text)
            print('>' + text)
        if(text[0:10] == 'login user'):
            time.sleep(4)
            str1 = '\nWelcome user'
            str2 = text[11:]
            str= str1 + ' ' +str2 + '!'
            print(str)
            engine.say(str)
            engine.runAndWait()
            sqlform = "Insert into login(name) values(%s)"
            val= [str2,]
            mycursor.execute(sqlform, val)
            mydb.commit()
            flag = 1
        else:
            time.sleep(2)
            t_1 = "Invalid user, Please try again."
            print(t_1)
            engine.say(t_1)
            engine.runAndWait()


    
    #Module selection
    print()
    time.sleep(2)
    flag1 = 'yes'
    while(flag1 == 'yes'):
        ta3="Which module you would like to access?"
        print(ta3)
        engine.say(ta3)
        engine.runAndWait()
        print("1. Lending")
        print("2. Cash")
        print("3. Trade Services")
        print("4. Treasury")
        time.sleep(2)
        print('\nListening...')
        with sr.Microphone() as source:
            voice.adjust_for_ambient_noise(source)
            audio_text1 = voice.listen(source)
            text1 = voice.recognize_google(audio_text1)
        print(">" + text1)  

        #Module 1
        if(text1 == 'lending'):
            print()
            time.sleep(2)
            ta4="Which instrument under that?"
            print(ta13)
            engine.say(ta13)
            engine.runAndWait()
            print("1. Loans")
            print("2. Facilities")
            print("3. Deals")
            print("4. Payments")
            print("5. Compliance Documents")
            print("6. Bills")

            print('\nListening...')
            with sr.Microphone() as source:
                audio_text13 = voice.listen(source)
                text13 = voice.recognize_google(audio_text13)
            print(">",text13)

        #Module 2
        elif(text1 == 'cash'):
            print()
            time.sleep(2)
            ta12="Which instrument under that?"
            print(ta12)
            engine.say(ta12)
            engine.runAndWait()
            print("1. Fund Transfers")
            print("2. Remittance")
            print("3. Bill Payments")
            print("4. Bulk Services")

            print('\nListening...')
            with sr.Microphone() as source:
                audio_text12 = voice.listen(source)
                text12 = voice.recognize_google(audio_text12)
            print(">",text12)


        #Module 3
        elif(text1 == 'trade services'):
            print()
            time.sleep(2)
            ta4="Which instrument under that?"
            print(ta4)
            engine.say(ta4)
            engine.runAndWait()
            print("1. Import Letter of Credit")
            print("2. Export Letter of Credit")
            print("3. Import collection")
            print("4. Export Collection")
            print("5. Financing request")

            print('\nListening...')
            with sr.Microphone() as source:
                voice.adjust_for_ambient_noise(source)
                audio_text2 = voice.listen(source)
                text2 = voice.recognize_google(audio_text2)
            print(">",text2)

            print()
            time.sleep(2)
            ta5="You can perform the following actions:- Initiation, Enquiry, Approval."
            print(ta5)
            engine.say(ta5)
            engine.runAndWait()  
            print('\nListening...')
            with sr.Microphone() as source:
                audio_text3 = voice.listen(source)
                text3 = voice.recognize_google(audio_text3)
            print(">",text3)

            print()
            ta6="Okay, Please provide the following details:"
            print(ta6)
            engine.say(ta6)
            engine.runAndWait() 
            ta7="Beneficiary Name"
            print(ta7)
            engine.say(ta7)
            engine.runAndWait()
            print('\nListening...')
            with sr.Microphone() as source:
                audio_text4 = voice.listen(source)
                text4 = voice.recognize_google(audio_text4)
            print(">",text4)

            print()
            ta8="LC Due date:"
            print(ta8)
            engine.say(ta8)
            engine.runAndWait()
            print('\nListening...')
            with sr.Microphone() as source:
                audio_text5 = voice.listen(source)
                text5 = voice.recognize_google(audio_text5)
            print(">",text5)

            print()
            ta9="Amount and currency"
            print(ta9)
            engine.say(ta9)
            engine.runAndWait()
            print('\nListening...')
            with sr.Microphone() as source:
                audio_text6 = voice.listen(source)
                text6 = voice.recognize_google(audio_text6)
            print(">",text6)
            
            #Insert into database
            random_id = ' '.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
            sql1 = "Insert into trade_services_ilc(id, beneficiary_name, lc_due_date, amt_and_curr) values(%s, %s, %s, %s)"
            val= [(id,text4, text5, text6),]
            mycursor.execute(sqlform, val)
            mydb.commit()

            print()
            ta7="Verify the given details:"
            print(ta7)
            engine.say(ta7)
            engine.runAndWait()
            print("Beneficiary Name:- ",text4)
            print("LC due date:- ",text5)
            print("Amount and Currency:- ",text6)
            with sr.Microphone() as source:
                audio_text7 = voice.listen(source)
                text7 = voice.recognize_google(audio_text7)
            print(">",text7)


            print()
            ta12="Initiating the Letter of Credit creation"
            print(ta12)
            engine.say(ta12)
            engine.runAndWait()

            print()
            time.sleep(4)
            ta13="Letter of Credit is successfully sent for Approval."
            print(ta13)
            engine.say(ta13)
            engine.runAndWait()

            
        ta14="Thank you, can I assist you with anything else? (Yes or No)"
        print(ta14)
        engine.say(ta14)
        engine.runAndWait()

        with sr.Microphone() as source:
            print('\nListening...')
            audio_text10 = voice.listen(source)
            text10 = voice.recognize_google(audio_text10)
        flag1 = text10
        print(">",text10)
        if(text10 =='no'):
            ta14="See you next time. Have a good day!"
            print(ta14)
            engine.say(ta14)
            engine.runAndWait()
            print(str2)
            sql = "DELETE FROM login WHERE name = %s"  #logging the user out
            del_name = (str2, )
            mycursor.execute(sql, del_name)
            mydb.commit()
            
    
        
if __name__ == "__main__":
    main()   