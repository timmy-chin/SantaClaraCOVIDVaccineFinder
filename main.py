# Before you can use these codes, install selenium into your laptop by using python. In your terminal, type "python 3 pip -m install selenium". For windows, type "python pip install selenium". If it says installation successful, great! You are good to go
# If pip install did not work, try to troubleshoot on google, there are many resources out there that can help you with this issue
# Next, you have to install chromedriver on your laptop so that you can allow selenium to control chrome. Go to https://chromedriver.chromium.org/downloads and download your version of chrome
# Lastly, look for your chromedriver file in downloads and copy its location (it should look like Users/name/Downloads/chromedriver) and insert the location into the first variable




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Insert chromedriver location into the parenthesis
browser = webdriver.Chrome('Chromedriver location')

#Stanford Healthcare
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[7])
browser.get('https://stanfordhealthcare.org/discover/covid-19-resource-center/patient-care/safety-health-vaccine-planning.html')

#Kaiser(Log In Required)
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[8])
browser.get('https://mydoctor.kaiserpermanente.org/covid-19/covid-19-vaccine')
try:
    signin = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-package/div/app-content/app-pm-body-content-renderer/div[3]/app-grid/div/div/div/app-cms-mdo-vaccine-booking-renderer/app-content-holder[2]/app-mdo-vertical-content-card-renderer/div/div/div[2]/div/button"))
    )
    signin.click()
    login = browser.find_element_by_xpath('//*[@id="username"]')
    login.send_keys('insert kaiser username')
    password = browser.find_element_by_xpath('//*[@id="password"]')
    password.send_keys('insert password')
    password.send_keys(Keys.ENTER)
except:
    time.sleep(1)

#Sutterhealth (Call Required)
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[9])
browser.get('https://www.sutterhealth.org/pamf/for-patients/health-alerts/covid-19-vaccine')


browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[10])
browser.get('https://myturn.ca.gov/')
try:
    trump1 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/div[1]/div/div[2]/div[3]/button"))
    )
    trump1.click()
    trump2 = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/form/span[1]/div/label/input')
    trump2.click()
    trump3 = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/form/span[2]/div/label/input')
    trump3.click()
    trump4 = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/form/span[3]/div/label/input')
    trump4.click()
    trumpboner = browser.find_element_by_xpath('//*[@id="q-screening-privacy-statement"]')
    trumpboner.click()
    trump5 = browser.find_element_by_xpath('//*[@id="q-screening-eligibility-age-range-16 - 49"]')
    trump5.click()
    trump6 = browser.find_element_by_xpath('//*[@id="q-screening-underlying-health-condition-Yes"]')
    trump6.click()
    trump7 = browser.find_element_by_xpath('//*[@id="q-screening-disability-No"]')
    trump7.click()
    trump8 = browser.find_element_by_xpath('//*[@id="q-screening-eligibility-industry"]/option[17]')
    trump8.click()
    trump9 = browser.find_element_by_xpath('//*[@id="q-screening-eligibility-county"]/option[47]')
    trump9.click()
    trumptrain = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/form/div/button[1]')
    trumptrain.click()
    time.sleep(2)
    zipcode = browser.find_element_by_xpath('//*[@id="location-search-input"]')
    zipcode.send_keys('95112')
    zipcode.send_keys(Keys.ENTER)
except:
    time.sleep(1)
    


browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[11])
browser.get('https://healow.com/apps/practice/bay-area-community-health-2998?v=1')
try:
    jack1 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='selSepcDiv']/b"))
    )
    jack1.click()
    time.sleep(2)
    jack2 = browser.find_element_by_xpath('//*[@id="specialityListXHRDiv"]/li[1]')
    jack2.click()
    jack3 = browser.find_element_by_xpath('//*[@id="wizard-three"]/div/div/a')
    jack3.click()
    time.sleep(2)
    jack4 = browser.find_element_by_xpath('//*[@id="locationListXHRDiv"]/li[1]/div[1]/span')
    jack4.click()
except:
    time.sleep(1)
    

    
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[12])
browser.get('https://www.elcaminohealth.org/covid-19-resource-center/schedule/vaccine?utm_source=SCCPH&utm_medium=referral&utm_campaign=covid19')
try:
    tom1 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='edit-a']/div[2]/label"))
    )
    tom1.click()
    time.sleep(3)
    tom2 = browser.find_element_by_xpath('//*[@id="edit-v"]/div[1]/label')
    time.sleep(3)
    tom2.click()
    tom3 = browser.find_element_by_xpath('//*[@id="edit-a1b"]/div[1]/label')
    tom3.click()
    time.sleep(3)
    tom5 = browser.find_element_by_xpath('//*[@id="edit-t"]/div[1]/label')
    tom5.click()
    tom4 = browser.find_element_by_xpath('//*[@id="edit-r"]/div[1]/label')
    tom4.click()
    tom6 = browser.find_element_by_xpath('//*[@id="webform-submission-covid-19-vaccination-elig-v11-node-165131-add-form"]/div[6]/label')
    tom6.click()

except:
    time.sleep(1)

    
#Change the inputs to your own info and location
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[13])
browser.get('https://www.riteaid.com/pharmacy/covid-qualifier')
try:
    jack1 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='dateOfBirth']"))
    )
    jack1.send_keys('09/24/1998')
    jack2 = browser.find_element_by_xpath('//*[@id="Occupation"]')
    jack2.click()
    jack2.send_keys('None of the Above')
    jack2.send_keys(Keys.ARROW_DOWN)
    jack2.send_keys(Keys.ENTER)
    jack3 = browser.find_element_by_xpath('//*[@id="city"]')
    jack3.send_keys('San Jose')
    jack4 = browser.find_element_by_id('eligibility_state')
    jack4.click()
    jack4.send_keys('California')
    jack5 = browser.find_element_by_id('mediconditions')
    jack5.click()
    jack5.send_keys('None of the Above')
    jack5.send_keys(Keys.ENTER)

except:
    time.sleep(1)

    
#Walmart (Login Required) use your own zip code
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[14])
browser.get('https://www.walmart.com/pharmacy/clinical-services/immunization/scheduled?imzType=covid&r=yes')
try:
    terence1 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='email']"))
    )
    terence1 = browser.find_element_by_xpath('//*[@id="email"]')
    terence1.send_keys('insert your email here')
    terence2 = browser.find_element_by_xpath('//*[@id="password"]')
    terence2.send_keys('insert password')
    terence2.send_keys(Keys.ENTER)
except:
    time.sleep(1)


browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[15])
browser.get('https://www.mhealthappointments.com/covidappt')
try:
    timmy1 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='fiftyMile-covid_vaccine_search']"))
    )
    timmy1.click()
    timmy2 = browser.find_element_by_xpath("//*[@id='covid_vaccine_search_input']")
    timmy2.send_keys('95112')
    timmy2.send_keys(Keys.ENTER)
except:
    time.sleep(1)


browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[16])
browser.get('https://www.cvs.com/immunizations/covid-19-vaccine')
try:
    tommy1 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "California"))
    )
    tommy1.click()
    time.sleep(3)
    button = browser.find_element_by_xpath(
        '//*[@id="vaccineinfo-CA"]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[3]/div/p[2]/a/strong')
    button.click()
    time.sleep(3)
    box1 = browser.find_element_by_xpath(
        '//*[@id="questionnaire"]/fieldset/section/div[2]/fieldset/div[2]/div[2]/label')
    box1.click()
    box2 = browser.find_element_by_xpath(
        '//*[@id="questionnaire"]/fieldset/section/div[3]/fieldset/div[2]/div[2]/label')
    box2.click()
    box3 = browser.find_element_by_xpath(
        '//*[@id="questionnaire"]/fieldset/section/div[4]/fieldset/div[2]/div[2]/label')
    box3.click()
    next1 = browser.find_element_by_xpath('//*[@id="content"]/div[3]/button')
    next1.click()
    time.sleep(3)
    box4 = browser.find_element_by_xpath('//*[@id="generic"]/section/div[2]/div/div/div[1]/label')
    box4.click()
    next5 = browser.find_element_by_xpath('//*[@id="content"]/div[3]/button')
    next5.click()
    time.sleep(3)
    state = browser.find_element_by_xpath('//*[@id="jurisdiction"]/option[6]')
    state.click()
    next2 = browser.find_element_by_xpath('//*[@id="content"]/div[3]/button')
    next2.click()
    age = browser.find_element_by_xpath('//*[@id="q1_0"]')
    age.send_keys('17')
    box5 = browser.find_element_by_xpath('//*[@id="generic"]/fieldset/section/div[3]/div/div/div[2]/label')
    box5.click()
    box6 = browser.find_element_by_xpath('//*[@id="qconsent"]')
    box6.click()
    next3 = browser.find_element_by_xpath('//*[@id="content"]/div[3]/button')
    next3.click()
    next4 = browser.find_element_by_xpath('//*[@id="content"]/div[3]/button')
    next4.click()
    time.sleep(3)
    zip = browser.find_element_by_xpath('//*[@id="address"]')
    zip.send_keys('95112')
    zip.send_keys(Keys.ENTER)
except:
    time.sleep(1)


#This is just a vaccine finder that leads you to other websites
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[17])
browser.get('https://vaccinefinder.org/search/')
try:
    mummy1 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='zipCode']"))
    )
    mummy1.send_keys("95112")
    mummy2 = browser.find_element_by_xpath('//*[@id="split-screen-content"]/form/div[2]/button')
    mummy2.click()
except:
    time.sleep(1)


#Walgreen (Login Required)
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[18])
browser.get('https://www.walgreens.com/findcare/vaccination/covid-19?ban=covid_vaccine_landing_schedule')
try:
    tasha0 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Schedule new appointment"))
    )
    time.sleep(3)
    tasha0.click()
    time.sleep(3)
    tasha1 = browser.find_element_by_id('inputLocation')
    tasha1.send_keys(Keys.BACKSPACE)
    tasha1.send_keys(Keys.BACKSPACE)
    tasha1.send_keys(Keys.BACKSPACE)
    tasha1.send_keys(Keys.BACKSPACE)
    tasha1.send_keys(Keys.BACKSPACE)
    tasha1.send_keys('95112')
    button = browser.find_element_by_xpath('//*[@id="wag-body-main-container"]/section/section/section/section/section[2]/div/span/button')
    button.click()
    time.sleep(3)
    button2 = browser.find_element_by_xpath('//*[@id="wag-body-main-container"]/section/section/section/section/section[4]/a/span')
    button2.click()
    email = browser.find_element_by_xpath('//*[@id="user_name"]')
    email.send_keys(''insert your email here'')
    password = browser.find_element_by_xpath('//*[@id="user_password"]')
    password.send_keys(''insert your password here')
    login = browser.find_element_by_xpath('//*[@id="submit_btn"]')
    login.click()
    time.sleep(5)
    box1 = browser.find_element_by_xpath('//*[@id="sq_100"]/div[2]/fieldset/div[7]/label/span[3]/span')
    box1.click()
    box2 = browser.find_element_by_xpath('//*[@id="eligibility-check"]')
    box2.click()
    search = browser.find_element_by_xpath('//*[@id="sp_100"]/div[2]/input')
    search.click()
    time.sleep(3)
    box3 = browser.find_element_by_xpath('//*[@id="sq_100"]/div[2]/fieldset/div[2]/label/span[3]/span')
    box3.click()
    box4 = browser.find_element_by_xpath('//*[@id="sq_102"]/div[2]/fieldset/div[2]/label/span[3]/span')
    box4.click()
    box5 = browser.find_element_by_xpath('//*[@id="sq_103"]/div[2]/fieldset/div[2]/label/span[3]/span')
    box5.click()
    box6 = browser.find_element_by_xpath('//*[@id="sq_104"]/div[2]/fieldset/div[2]/label/span[3]/span')
    box6.click()
    Next = browser.find_element_by_xpath('//*[@id="sp_100"]/div[3]/input')
    Next.click()
    time.sleep(3)
    Schedule = browser.find_element_by_xpath('//*[@id="hn-startVisitBlock-gb-terms"]')
    Schedule.click()
    time.sleep(3)
    box7 = browser.find_element_by_xpath('//*[@id="dose1"]')
    box7.click()
    box8 = browser.find_element_by_xpath('//*[@id="continueBtn"]')
    box8.click()
except:
    time.sleep(1)


browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[19])
browser.get('https://vax.sccgov.org/home?mkt_tok=eyJpIjoiTmpBMk1qa3lNREF3TmpJMSIsInQiOiJ5ZHdLak85TEcybmFZSGdwS0RCSVJVYzdjTjlleWtrRUsyRzY3TUVSTW8xaE54MXZWcnZXdjA1emNVbTBmbWpOY2dYbzRKUXBMSDNYVFpORVhNXC9POUZDN2lFNVpqa3pFZDNrSkVXTXN3aXYyMXFBbzBIaVcxeHlLV1VHRXNGSWIifQ%3D%3D')
try:
    input1 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='edit-65-up-scc-resident-no']"))
    )
    input1.click()
    input2 = browser.find_element_by_xpath('//*[@id="edit-can-you-attest-under-penalty-of-perjury-that-you-work-in-one-of-yes"]')
    input2.click()
    input3 = browser.find_element_by_xpath('//*[@id="edit-how-old-are-you-occupation-18"]')
    input3.click()
    input4 = browser.find_element_by_xpath('//*[@id="edit-have-you-had-another-vaccine-e-g-influenza-in-the-last-14-days-no"]')
    input4.click()
    input5 = browser.find_element_by_xpath('//*[@id="edit-are-you-currently-ill-with-covid-19-no"]')
    input5.click()
    input6 = browser.find_element_by_xpath('//*[@id="edit-do-you-have-a-known-severe-allergy-to-ul-li-polysorbate-li-li-or-no"]')
    input6.click()
    input7 = browser.find_element_by_xpath('//*[@id="edit-which-dose-number-first-dose"]')
    input7.click()
    input8 = browser.find_element_by_xpath('//*[@id="edit-vaccination-location-santa-clara-county-fairgrounds-expo"]')
    input8.click()
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[20])
browser.get('https://www.costco.com/covid-vaccine.html')
try:
    tommy1 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "California"))
    )
    tommy1.click()
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[27])
browser.get('https://www.kroger.com/rx/covid-eligibility')
try:
    tommy1 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "I Agree"))
    )
    tommy1.click()
    tommy2 = browser.find_element_by_link_text('No')
    tommy2.click()
    tommy3 = browser.find_element_by_xpath('//*[@id="content"]/div/section[2]/div/div/div/div/div/div/div/div/div/div/ul/li[5]/div/div[2]/div[2]/div/div/div/select/option[6]')
    tommy3.click()
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[30])
browser.get('https://hooverrx.com/book-covid-19-vaccine-appointment/')

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[31])
browser.get('https://lindarxpharmacy.godaddysites.com/covid-19-eng')

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[32])
browser.get('https://savemartluckysched.rxtouch.com/smsched/program/covid19/patient/advisory')
try:
    tommy1 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='zip-input']"))
    )
    tommy1.send_keys('95112')
    tommy1.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[33])
browser.get('https://myhealth.stanfordhealthcare.org/#/embedded-schedule/vt=1575&dept=8015190001')

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[34])
browser.get('https://forms.stanfordchildrens.org/service/covid-19-vaccination/covac.jsp?')

#Healthmart (Login Required)
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[35])
browser.get('https://scrcxp.pdhi.com/Portal/Member/d1e1f5d5-007f-4167-b8d1-1ea83cb3b215/?qitq=8f2d9b46-8e98-4f0e-90b7-b5ec6cb048a4&qitp=bba979f9-9593-43dd-b93c-0f99139502b4&qitts=1617715238&qitc=pdhi&qite=covid19vaccination&qitrt=Safetynet&qith=ce90a6f0c9b7d3d0a85c51231a92652d')
try:
    tommy1 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='Username']"))
    )
    tommy1.send_keys('insert your username here')
    password = browser.find_element_by_xpath('//*[@id="Password"]')
    password.send_keys('Insert your password here')
    password.send_keys(Keys.ENTER)
    time.sleep(3)
    start = browser.find_element_by_xpath('//*[@id="covid-vaccination-carousel"]/div/div[1]/div[2]/div/button')
    start.click()
    time.sleep(3)
    button1 = browser.find_element_by_xpath('//*[@id="feverCoughBreathing-2"]')
    button1.click()
    button2 = browser.find_element_by_xpath('//*[@id="exposed-2"]')
    button2.click()
    button3 = browser.find_element_by_xpath('//*[@id="previousVaccine-2"]')
    button3.click()
    button4 = browser.find_element_by_xpath('//*[@id="anaphylactic-2"]')
    button4.click()
    button5 = browser.find_element_by_xpath('//*[@id="polysorbate-2"]')
    button5.click()
    button6 = browser.find_element_by_xpath('//*[@id="antibodies-2"]')
    button6.click()
    next = browser.find_element_by_xpath('//*[@id="covid-vaccination-carousel"]/div/div[2]/form/div/button[2]')
    next.click()
    time.sleep(3)
    button7 = browser.find_element_by_xpath('//*[@id="criteria-Other adult 16 years of age and older (check with your county)"]')
    button7.click()
    next2 = browser.find_element_by_xpath('//*[@id="covid-vaccination-carousel"]/div/div[4]/form/div/button[2]')
    next2.click()
    time.sleep(3)
    button8 = browser.find_element_by_xpath('//*[@id="gender-Male"]')
    button8.click()
    button9 = browser.find_element_by_xpath('//*[@id="racialBackground-Asian"]')
    button9.click()
    button10 = browser.find_element_by_xpath('//*[@id="ethnicBackground-NotHispanicOrLatino"]')
    button10.click()
    button11 = browser.find_element_by_xpath('//*[@id="allergic-false"]')
    button11.click()
    button12 = browser.find_element_by_xpath('//*[@id="bloodDisorder-No"]')
    button12.click()
    button13 = browser.find_element_by_xpath('//*[@id="immunocompromised-false"]')
    button13.click()
    button14 = browser.find_element_by_xpath('//*[@id="dermalFiller-No"]')
    button14.click()
    button15 = browser.find_element_by_xpath('//*[@id="pregnancy-NotPregnant"]')
    button15.click()

except:
    time.sleep(1)




