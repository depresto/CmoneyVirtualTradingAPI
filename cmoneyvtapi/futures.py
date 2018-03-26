#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os.path, os
import json
import pickle
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta


class FuturesExchange():
  def __init__(self, username, password):

    if os.path.isfile('cookie.pk'):
      with open('cookie.pk', 'rb') as f:
        cookiesfile   = pickle.load(f)
        cookies       = requests.utils.cookiejar_from_dict(cookiesfile)
        self.session  = requests.session()
        self.session.cookies = cookies

    else:     
      login(username, password)

    r         = self.session.get("https://www.cmoney.tw/vt/")
    parser    = BeautifulSoup(r.content,'html.parser')

    ele       = parser.find(id="PageData")

    if (ele != None):
      self.AccountId = ele["aid"]
    else:
      self.login(username, password)
      self.AccountId = parser.find(id="PageData")["aid"]


  def login(self, username, password):
    LOGIN_URL = "https://www.cmoney.tw/member/login/"

    s       = requests.Session()
    r       = s.get(LOGIN_URL)

    parser  = BeautifulSoup(r.content,'html.parser')

    VIEWSTATE           = parser.find(id="__VIEWSTATE")['value']
    VIEWSTATEGENERATOR  = parser.find(id="__VIEWSTATEGENERATOR")['value']
    EVENTVALIDATION     = parser.find(id="__EVENTVALIDATION")['value']

    login_data={
      "__VIEWSTATE":                        VIEWSTATE,
      "__EVENTVALIDATION":                  EVENTVALIDATION,
      "__VIEWSTATEGENERATORT":              VIEWSTATEGENERATOR,
      "ctl00$ContentPlaceHolder1$mail":     username,
      "ctl00$ContentPlaceHolder1$pw":       password,
      "ctl00$ContentPlaceHolder1$check":    "True",
      "ctl00$ContentPlaceHolder1$loginBtn": "登入"
    }

    r = s.post(LOGIN_URL, data=login_data, headers={'Referer': r.url})

    if r.url == "https://www.cmoney.tw/member/":
      print("Login successful!")
      self.session = s

      with open('cookie.pk', 'wb') as f:
        pickle.dump(requests.utils.dict_from_cookiejar(self.session.cookies), f)

    else:
      print("Login failed")
      self.session = None


  def getTicker(self, month):
    URL = "https://www.cmoney.tw/vt/ashx/foaccountdata.ashx"

    params = {
      "act":      "GetFuturesPrice",
      "futKey":   "MXF",
      "futMonth": month
    }

    r = self.session.get(URL, params= params)

    data = json.loads(r.text)
    print(data)


  def PlaceOrder(self, symbol, month, isSell = False, amount = 1):
    URL = "https://www.cmoney.tw/vt/ashx/userset.ashx"

    params = {
      "act":      "NewFuturesEntrust",
      "aid":      self.AccountId,
      "futKey":   symbol,
      "futMonth": month,
      "isSell":   isSell,
      "condType": "IOC",
      "prFlag":   "MarketPr", # Buy/Sell at market price
      #"price": price,
      "amount":   amount
    }

    r   = self.session.post(URL, params)

    if r.text == '{"status":0,"message":""}':
      print("place order successful!")
    else:
      print("place order failed:")
      print(r.text)


  def getOrder(self, accountId = None):
    params = {
      "act": "EntrustQuery",
      "aid": accountId
    }

    return self.doRequest(params, accountId = accountId)


  def getTransaction(self, days= None, accountId = None):
    params = {
      "act": "OrderRecord",
      "aid": accountId,
      "stockFilter":  ""
    }

    return self.doRequest(params, accountId = accountId, days= days)


  def deleteOrder(self):
    URL = "https://www.cmoney.tw/vt/ashx/foaccountdata.ashx"
    # act=DeleteEntrust&aid=358850&GroupId=0&OrdNo=11506728


  def getProfit(self, days= 7, accountId= None):
    params = {
      "act":    "FOProfitAndLoss",
      "aid":    accountId,
      "profitLossType": "accomplished",
      "ordid":          ""
    }

    return self.doRequest(params, accountId = accountId, days= days)


  def doRequest(self, params, accountId = None, days= None):
    # URL = "https://www.cmoney.tw/vt/ashx/accountdata.ashx"
    URL = "https://www.cmoney.tw/vt/ashx/FOAccountData.ashx"

    if (accountId == None):
      # Get self data if account ID not entered
      params["aid"] = self.AccountId
      # URL = "https://www.cmoney.tw/vt/ashx/FOAccountData.ashx"

    if (days):
      days        = int(days)
      today       = date.today()
      nDaysAgo    = today - timedelta(days= days)

      params["startTime"] = "%s-%s-%s"% (nDaysAgo.year, nDaysAgo.month, nDaysAgo.day)
      params["endTime"]   = "%s-%s-%s"% (today.year, today.month, today.day)

    r = self.session.get(URL, params= params)
    data = json.loads(r.text)

    return data


  def deleteCookies(self):
    if os.path.isfile('cookie.pk'):
      os.remove('cookie.pk')
      print('Remove cookies file successful!')
    else:
      print('Cookies file not found.')


    
