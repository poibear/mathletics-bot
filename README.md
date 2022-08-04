# mathletics-bot
upgraded mathletics bot to include level 2 solving (forked from charlie-grayh

# Requirements
1. python
2. chrome
3. selenium

Required Packages: selenium, webdriver-manager
``` 
$ pip install selenium
$ pip install webdriver-manager
``` 

# Startup

1. start the script
2a. uncomment any functions if desired
2. profit!

# Using devtools-bot.py

if you dont want to open a new window every time you want to start a new match, use this bot

1. run `.\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"` in the same directory as chrome.exe
2. start the script (devtools-bot.py)
3. log into mathletics and start an online addition game
4. wait until the first question shows up, then press enter
5. run the script again and it should work with the previous window you had opened
