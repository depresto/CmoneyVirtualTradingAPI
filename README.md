# CMoney Virtual Trading API / Cmoney 股市大富翁 API

提供

## System requirements 系統需求

### Programming language & packages 程式語言&套件

Python 3.6

- bs4
- requests

### Installation 安裝

```bash
pip install bs4 request

git clone https://github.com/depresto/CmoneyVirtualTradingAPI.git
cd CmoneyVirtualTradingAPI
```


## Usage 使用說明

### Futures exchange simulation 期貨模擬交易

Initialize 初始化

``` python
from cmoneyvtapi import FuturesExchange

fut = FuturesExchange(username, password)

if (fut.session == None):
	print("Login error")
else:
	'''
	Your code
	'''
```


Get all today's order records 取得所有今日委託記錄

```python
# If look up self record
# accountId = None or accountId = user ID

fut.getOrder(accountId= None)

''' Example return
[{
	'KindType': 1, 
	'CombinationType': 0, 
	'Id': 'TXFD8', 
	'Name': '臺指期', 
	'Bs': 'S', 
	'ShowBs': '賣出', 
	'OrdPr': '10,765.00', 
	'OrdQty': '1', 
	'UnPay': '83,093', 
	'UnQty': '1', 
	'Time': '2018/03/26 09:22:38', 
	'StCode': '2', 
	'StatueMessage': '委託成功', 
	'CanDel': '0', 
	'CNo': '', 
	'NoteId': '0', 
	'IsPublicNote': '0', 
	'Cp': 'None', 
	'Month': '201804', 
	'Key': 'TXF', 
	'Condition': 'ROD', 
	'Color': 'c2'
}]
'''
```

Get all transactions in a specific period of time (from n days ago). 
取得特定時間內的交易紀錄 (n天前 ~ 今天)

```python
# If look up self record
# accountId = None or accountId = user ID
# days: n days ago

fut.getTransaction(accountId= None, days= None)

''' Example return
{'stock': '', 'stockname': '', 'data': [{
	'KindType': 1, 
	'CombinationType': 0, 
	'Id': 'TXFD8', 
	'Name': '臺指期', 
	'Bs': 'S', 
	'ShowBs': 
	'新倉賣出', 
	'DealPr': '10,735.00', 
	'DeQty': '2', 
	'Fee': '100', 
	'Tax': '86', 
	'Time': '2018/03/23<br>13:44:27', 
	'NoteId': '0', 
	'IsPublicNote': '0', 
	'OrderNo': '11548177', 
	'Cp': 'None', 
	'Month': '201804', 
	'Key': 'TXF', 
	'IsOffset': 'False', 
	'IncomeLoss': '0', 
	'Ratio': '0', 
	'Color': 'c2', 
	'Cost': '166,000'
}]}
'''
```

Get all realized gains and losses in a specific period of time (from n days ago).
取得特定時間內已實現損益 (n天前 ~ 今天)

```python
# If look up self record
# accountId = None or accountId = user ID
# days: n days ago

fut.getProfit(accountId= None, days= None)

'''Example return
[{
	'KindType': 1, 
	'CombinationType': 0, 
	'Id': 'TXFD8', 
	'Name': '臺指期', 
	'IQty': '3', 
	'Month': '201804', 
	'ShowBs': '買進<br>賣出', 
	'Cp': 'None', 
	'BuyAvgPr': '10,796.33', 
	'SellAvgPr': '10,795.00', 
	'SellTotal': '248,202', 
	'BuyTotal': '249,000', 
	'IncomeLoss': '-1,356', 
	'Ratio': '-0.54', 
	'Fee': '300', 
	'Tax': '258', 
	'Key': 'TXF'
}]
'''
```