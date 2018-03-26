# CMoney Virtual Trading API / Cmoney 股市大富翁 API



提供

## Programming language 程式語言

Python 3.6


## Package requirements 套件需求

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
```


Get all today's order records 取得所有今日委託記錄

```python
# If look up self record
# accountId = None 
# or accountId = user ID
fut.getOrder(accountId = None)

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
#  	accountId = None or accountId = user ID
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