# mathletics-bot
upgraded mathletics bot to include level 2 solving (forked from [charlie-gray](https://github.com/charlie-gray/mathletics-bot))

## requirements
1. python (w/ pip)
2. chrome
3. selenium

Required Packages: selenium, webdriver-manager
``` 
$ pip install selenium
$ pip install webdriver-manager
``` 

## startup

1. start the script
2a. uncomment any functions if desired
2. profit!

## connecting program to existing chrome application

if you dont want to open a new window every time you want to start a new match, do the following:

1. open cmd and navigate to your chrome installation directory (default is C:\Program Files\Google\Chrome\Application)
2. run `.\chrome.exe --remote-debugging-port=9222`
3. uncomment line 14
4. run main.py
