from selenium import webdriver
import time
import datetime  
name = str(input('Enter your name')) # Name
email = str(input('Enter your Email ID')) # Email ID
phone_number = str(input('Enter your Phone number')) # Phone Number

web = webdriver.Chrome(r'C:\Program Files (x86)\chromedriver') # system path of chromedriver
web.get(r'https://docs.google.com/forms/d/e/1FAIpQLSdjUSiRPAD3jUqsUGB2ATcyMfOrFWt8Y3Jsoyuxsd19eniZiQ/viewform?usp=sf_link') # this is url link of attendence form



# using now() to get current time  

current_time = datetime.datetime.now() 
main_hour = str(current_time.hour)


fday = current_time.day 
fmonth = current_time.month
fyear = current_time.year 
finaltime = str(str(fday)+str(fmonth)+str(fyear))
    


time.sleep(3)

tymlst = [['07','35'],['08','35'],['09','20'],['10','05']]


def Monday():
    monday_subjectlst = ['Physics','Chemistry','English','Maths']
    for i in range(0,4):
        # Name
        fname = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        fname.send_keys(name)

        #Email ID

        femail = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        femail.send_keys(email)

        #Class

        fclass = web.find_element_by_xpath(".//*[contains(text(),'12th A')]").click()

        # Subject
        dropdown = web.find_element_by_css_selector('.quantumWizMenuPaperselectOption')
        dropdown.click()
        time.sleep(0.80)
        item = web.find_element_by_css_selector('.exportSelectPopup [data-value="{hey}"]'.format(hey = monday_subjectlst[i]))
        item.click()

        # Date


        date = finaltime
        fdate = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
        fdate.send_keys(date)


        # Time 

        hr = tymlst[i][0]
        fhr = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input')
        fhr.send_keys(hr)

        mi = tymlst[i][1]
        fmi = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input')
        fmi.send_keys(mi)

        btn = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()

        bnt2 = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()


def Tuesday():
    Tuesday_subjectlst = ['Physics','Chemistry','I.P','Maths']
    for i in range(0,4):
        # Name
        fname = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        fname.send_keys(name)

        #Email ID

        femail = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        femail.send_keys(email)

        #Class

        fclass = web.find_element_by_xpath(".//*[contains(text(),'12th A')]").click()

        # Subject
        dropdown = web.find_element_by_css_selector('.quantumWizMenuPaperselectOption')
        dropdown.click()
        time.sleep(0.80)
        item = web.find_element_by_css_selector('.exportSelectPopup [data-value="{hey}"]'.format(hey = Tuesday_subjectlst[i]))
        item.click()

        # Date


        date = finaltime
        fdate = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
        fdate.send_keys(date)


        # Time 

        hr = tymlst[i][0]
        fhr = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input')
        fhr.send_keys(hr)

        mi = tymlst[i][1]
        fmi = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input')
        fmi.send_keys(mi)

        btn = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()

        bnt2 = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()


def Wednesday():
    Wednesday_subjectlst = ['Maths','IP','English','Physics']
    for i in range(0,4):
        # Name
        fname = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        fname.send_keys(name)

        #Email ID

        femail = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        femail.send_keys(email)

        #Class

        fclass = web.find_element_by_xpath(".//*[contains(text(),'12th A')]").click()

        # Subject
        dropdown = web.find_element_by_css_selector('.quantumWizMenuPaperselectOption')
        dropdown.click()
        time.sleep(0.80)
        item = web.find_element_by_css_selector('.exportSelectPopup [data-value="{hey}"]'.format(hey = Wednesday_subjectlst[i]))
        item.click()

        # Date


        date = finaltime
        fdate = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
        fdate.send_keys(date)


        # Time 

        hr = tymlst[i][0]
        fhr = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input')
        fhr.send_keys(hr)

        mi = tymlst[i][1]
        fmi = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input')
        fmi.send_keys(mi)

        btn = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()

        bnt2 = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()


def Thursday():
    Thursday_subjectlst = ['English','IP','Chemistry','Physics']
    for i in range(0,4):
        # Name
        fname = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        fname.send_keys(name)

        #Email ID

        femail = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        femail.send_keys(email)

        #Class

        fclass = web.find_element_by_xpath(".//*[contains(text(),'12th A')]").click()

        # Subject
        dropdown = web.find_element_by_css_selector('.quantumWizMenuPaperselectOption')
        dropdown.click()
        time.sleep(0.80)
        item = web.find_element_by_css_selector('.exportSelectPopup [data-value="{hey}"]'.format(hey = Thursday_subjectlst[i]))
        item.click()

        # Date


        date = finaltime
        fdate = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
        fdate.send_keys(date)


        # Time 

        hr = tymlst[i][0]
        fhr = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input')
        fhr.send_keys(hr)

        mi = tymlst[i][1]
        fmi = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input')
        fmi.send_keys(mi)

        btn = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()

        bnt2 = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()


def Friday():
    Friday_subjectlst = ['English','IP','Chemistry','Maths']
    for i in range(0,4):
        # Name
        fname = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        fname.send_keys(name)

        #Email ID

        femail = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        femail.send_keys(email)

        #Class

        fclass = web.find_element_by_xpath(".//*[contains(text(),'12th A')]").click()

        # Subject
        dropdown = web.find_element_by_css_selector('.quantumWizMenuPaperselectOption')
        dropdown.click()
        time.sleep(0.80)
        item = web.find_element_by_css_selector('.exportSelectPopup [data-value="{hey}"]'.format(hey = Friday_subjectlst[i]))
        item.click()

        # Date


        date = finaltime
        fdate = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
        fdate.send_keys(date)


        # Time 

        hr = tymlst[i][0]
        fhr = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input')
        fhr.send_keys(hr)

        mi = tymlst[i][1]
        fmi = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input')
        fmi.send_keys(mi)

        btn = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()

        bnt2 = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()


def Saturday():
    Saturday_subjectlst = ['English','Chemistry','Maths','Physics']
    for i in range(0,4):
        # Name
        fname = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        fname.send_keys(name)

        #Email ID

        femail = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        femail.send_keys(email)

        #Class

        fclass = web.find_element_by_xpath(".//*[contains(text(),'12th A')]").click()

        # Subject
        dropdown = web.find_element_by_css_selector('.quantumWizMenuPaperselectOption')
        dropdown.click()
        time.sleep(0.80)
        item = web.find_element_by_css_selector('.exportSelectPopup [data-value="{hey}"]'.format(hey = Saturday_subjectlst[i]))
        item.click()

        # Date


        date = finaltime
        fdate = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
        fdate.send_keys(date)


        # Time 

        hr = tymlst[i][0]
        fhr = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input')
        fhr.send_keys(hr)

        mi = tymlst[i][1]
        fmi = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input')
        fmi.send_keys(mi)

        btn = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()

        bnt2 = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()


while True:
    current_time = datetime.datetime.now() 
    main_hour = str(current_time.hour)

    date=str(str(fday)+' '+str(fmonth)+' '+str(fyear))
    day, month, year = date.split(' ') 
    day_name = datetime.date(int(year), int(month), int(day)) 
    mainday = day_name.strftime("%A")


    if main_hour == str(9) and mainday == 'Thursday': # Here 16 is Hour of day  or 16:00pm
        Thursday()
        break
    elif main_hour == str(9) and mainday == 'Monday':
        Monday()
        break
    elif main_hour == str(11)  and mainday == 'Tuesday':
        Tuesday()
        break
    elif main_hour == str(11) and mainday == 'Wednesday':
        Wednesday()
        break
    elif main_hour == str(9) and mainday == 'Friday':
        Friday()
        break
    elif main_hour == str(10) and mainday == 'Saturday':
        Saturday()
        break




