import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager# Initiate the browser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

USERNAME = "" #mathletics username goes here
PASSWORD = "" #password goes here

options = Options()
#options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
if not "debuggerAddress" in options.experimental_options:
    options.add_experimental_option("detach", True) #so chrome doesnt close after program finishes
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
browser  = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.get('https://login.mathletics.com')
browser.maximize_window()

userbox = WebDriverWait(browser, timeout=5).until(lambda d: d.find_element(By.ID, 'username'))
pwdbox = WebDriverWait(browser, timeout=5).until(lambda d: d.find_element(By.ID, 'password'))

userbox.clear() #delete any info from text box
pwdbox.clear() #just in case browser uses autofill

userbox.send_keys(USERNAME)
pwdbox.send_keys(PASSWORD + Keys.ENTER)

# play btn on main page
playbtn = WebDriverWait(browser, timeout=10).until(lambda d: d.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/angular-react-bridge/nav/div[1]/ul/li[3]/div/div/div'))
playbtn.click()

browser.implicitly_wait(2)

# play btn on img
playbtn = WebDriverWait(browser, timeout=8).until(lambda d: d.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div/article/section/div[1]/carousel/section-panel/scale-nine-container/div/scale-nine-container/div/div/div/ul/carousel-item[1]/li/img'))
playbtn.click()

browser.implicitly_wait(2)

# ### COMPUTER CHALLENGE ###
# playbtn = WebDriverWait(browser, timeout=5).until(lambda d: d.find_element(By.XPATH, "/html/body/div[1]/ui-view/div/div[4]/div/div[2]/button"))
# playbtn.click()
# ##########################

### LEVEL 2 ###
# playbtn = WebDriverWait(browser, timeout=5).until(lambda d: d.find_element(By.XPATH, "//*[@id=\"livemathletics\"]/body/div[1]/ui-view/div/level-selector-directive/div/div[2]/button"))
# playbtn.click()

### GO BTN ###
playbtn = WebDriverWait(browser, timeout=10).until(lambda d: d.find_element(By.XPATH, '/html/body/div[1]/ui-view/div/div[4]/div/go-button/div/button[1]')) #* means classname in xpath
playbtn.click() #actual "go" button
##############

while True:
    try:
        question = WebDriverWait(browser, timeout=30).until(lambda d: d.find_element(By.XPATH, "//*[@id=\"livemathletics\"]/body/div[1]/ui-view/div/div[1]/div[2]/div[2]/aligned-question/div/form/div").text)

        question = question.replace(" =", "")
        if "-" in question:
            splitter = " - "
            question = question.split(splitter)
            answer = int(question[0]) - int(question[1])
        if "+" in question:
            splitter = " + "
            question = question.split(splitter)
            answer = int(question[0]) + int(question[1])
        # if "×" in question: #level 3, not yet coded for it
        #     splitter = " × "
        #     question = question.split(splitter)
        #     answer = int(question[0]) * int(question[1])
        
        browser.find_element(By.XPATH, "//*[@id=\"livemathletics\"]/body/div[1]/ui-view/div/div[1]/div[2]/div[2]/aligned-question/div/form/div/input").send_keys(answer)
        browser.find_element(By.XPATH, "//*[@id=\"livemathletics\"]/body/div[1]/ui-view/div/div[1]/div[2]/div[2]/aligned-question/div/form/div/input").send_keys(Keys.ENTER)
    except:
        break

sys.exit(0)
