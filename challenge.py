import csv

class MempoolTransaction:
	"""class for transactions in mempool"""
	
	def __init__(self,txid,fee,weight,parents):
		self.txid=txid
		self.fee=fee
		self.weight=weight
		self.parents=parents

	def get_elements(self):
		print(self.txid)
		print(self.fee)
		print(self.weight)
		print(self.parents)

lst=[]
def parse_mempool_csv():
	"""Parse the CSV file and return a list of MempoolTransactions."""
	with open('mempool.csv') as f:
		r=1
		csv_reader = csv.reader(f, delimiter=',')
		for row in csv_reader:
			if(r==1):
				r=r+1
			else:
				r=r+1
				lst.append(MempoolTransaction(row[0],row[1],row[2],row[3]))
		
	
def write_transactions():
	""" writes the b=valid transactions in transactions.txt"""



parse_mempool_csv()
