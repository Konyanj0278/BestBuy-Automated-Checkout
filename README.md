 BestBuy-Automated-Checkout
A bot to constantly run and purchase item on BestBuy.com


Hello all,

I created this bot to help me get a new RTX 30 series graphics card through BestBuy. I was able to get the card and now want to share this bot with everyone.

Requirements:\
 Selenium\
 Tkinter\
 Chrome webdriver
 
Orginal Release v1.0:\
With this intial release the code does work as of 11/4/20 and is able to purchase any item that registers as in stock on the BestBuy website. It does require that you give the SKU number of the item you are trying to get. This is easily avaialbe on the products webpage.
  
  
How to use:

1) Make sure that all required libraries are installed.
2) Rename the "config_" file to "config".
3) Save the Chrome webdriver in the same directory as BestBuybot.py
4) Open the config file with a text editor and fill in the parrameters with your information, if you are an employee of BestBuy there    is a field for your employee number.
5) Edit the code and change the field of bot.searctag() to contain the sku that you want, do note that this field takes a string and    not an integer. 
6) Run bot and Enjoy

Picture of code working:

![BestBuy Bot Succsess](https://user-images.githubusercontent.com/55165705/98168055-df014300-1e9e-11eb-9eeb-f8911be903d2.JPG)


Link to latest version of ChromeWebdriver:
https://chromedriver.chromium.org/downloads
