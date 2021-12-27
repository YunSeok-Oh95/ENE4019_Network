import requests
import time
import csv
import telegram
from time import gmtime, strftime
from telegram.ext import Updater, CommandHandler
from telegram import Update, Bot
from apscheduler.schedulers.background import BackgroundScheduler
f=open('coinPrice.csv','w',newline="")
title=["Date", "USD-BTC", "EUR-B8TC"]
wr=csv.writer(f)
wr.writerow(title)
f.close()
def coin():
    global excurrencyl
    global excurrency2
    currency1: str="USD"
    currency2: str="EUR"
    r=requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms="+currency1+ ", "+currency2)
    line=r.json
    coinpriceInfo=(strftime("%Y-%m-%d-%H:%W:%S",time.localtime()),line[currency1] , line[currency2)]
    print(strftime("%Y-%m-%d-%H:%W:%S", time.localtime())+" "+str(line[currency1])+" "+str(line[currency2]))
    f=open('coinPrice.csv','a’,newline='\n')
    wr=csv.writer(f)
    wr.writerow(coinpriceInfo)
    f.close()
if (excurrencyl<=line[currency1] and excurrency2<=line[currency2)):
    bot.send_message(chat_id=id, text="Bithumb USD-BTC: "+str(line(currency1])+", Up "+str(round(line[currency1]-excurrency1,2))+"\nBithumb EUR-BTC: "+str(line(currency2])+", Up "+str(round(line(currency2)-excurrency2,2)))
elif (excurrencyl>sline(currencyl) and excurrency2<#line[currency2) ):
    bot.send_message(chat_id=id, text="Bithumb USD-BTC: "+str(line(currency1])+", Down "+str(round(line[currency1]-excurrency1,2))+"\nBithumb EUR-BTC: "+str(line(currency2])+", Up "+str(round(line(currency2)-excurrency2,2)))
elif (excurrencylestline(currencyl1) ond excurrency2>=line[currency2] ):
    bot.send_message(chat_id=id, text="Bithumb USD-BTC: "+str(line(currency1])+", Up "+str(round(line[currency1]-excurrency1,2))+"\nBithumb EUR-BTC: "+str(line(currency2])+", Down "+str(round(line(currency2)-excurrency2,2)))
elif(excurrencyl>=line(currency1) and excurrency2>=line[currency2) ):
    bot.send_message(chat_id=id, text="Bithumb USD-BTC: "+str(line(currency1])+", Down "+str(round(line[currency1]-excurrency1,2))+"\nBithumb EUR-BTC: "+str(line(currency2])+", Down "+str(round(line(currency2)-excurrency2,2)))

def start(update, context):
    bot.send_message(chat_id=id, text="시작합니다")
    currency1:str="USD"
    currency2:str="EUR”
    r=requests.get("https://min-ap.cryptocompare.com/data/price?fsym-BTC&tsyms="+currency1+", "+currency2)
    line=r.json
    coinpriceInfo=(strftime("%Y-%m-%d-%H:%W:%S",time.localtime()),line[currency1] , line[currency2)]
    bot.send_message(chat_id=id, text="Bithumb USD-BTC: "+str(line[currency1] )+"\nBithumb EUR-BTC: "+str(line[currency2)))
    global excurrency1
    global excurrency2
    excurrency1=line[currency1]
    excurrency2=line[currency2]

    sched.add_job(coin, ‘cron’, second="59", id="test_2")
def stop(update, context):
    bot.send_message(chat_idzid, text="멈춥니다")
    sched.remove_job('test_2')

excurrency1=0
excurrency2=0
sched=BackgroundScheduler()
sched.start()
token= 'Token'
id="id"
bot = telegram. Bot (token)
updater = Updater(token=token, use_context=True)
dispatcher=updater.dispatcher
start_handler=CommandHandler('start', start)
stop_handler=CommandHandler('stop',stop)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(stop_handler)
updater.start polling()
updater.idle()