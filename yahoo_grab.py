import urllib.request as req
import time
from datetime import datetime
#import pandas as pd

# Currently this just provides the url (example shown below) for grabbing a csv file of stock history off yahoo finance site
# 'https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=511070400&period2=1623456789&interval=1d&events=history&crumb=xJRR7KqN.Vl'

class Stock:
	def __init__(self, ticker = 'aapl', p1 = '2018 01 30', p2 = '2020 12 31', interval = '1d'):
		self.ticker = ticker.upper()
		self.p1 = str(int(datetime.strptime(p1, '%Y %m %d').timestamp()))	# convert start date to unix timestamp
		self.p2 = str(int(datetime.strptime(p2, '%Y %m %d').timestamp()))	# convert end date....
		self.interval = interval

		# combine into url
		base_url = 'https://query1.finance.yahoo.com/v7/finance/download/'
		self.combined_url = base_url + self.ticker + '?period1=' + self.p1 + '&period2=' + self.p2 + '&interval=' + self.interval + '&events=history&crumb=xJRR7KqN.Vl'

	def printURL(self):
		print(self.combined_url)

apple = Stock()
apple.printURL()


# Code below was used to download and manipulate data in python as a pandas dataframe. Currently not used...

#def getData(tempStock):
#    global r, text, DF
#    opener = req.build_opener()
#    opener.addheaders.append(('Cookie', 'B=bf19n5hdkeu4j&b=3&s=kb'))
#    r = opener.open(tempUrl)
#    text = r.read().decode('UTF-8')
#    DF = pd.read_csv(StringIO(text), lineterminator = '\n', header = 0, index_col = 0, parse_dates = [0])
#    return(DF)