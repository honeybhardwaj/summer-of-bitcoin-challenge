import csv

class MempoolTransaction:
	"""class for transactions in mempool"""
	
	def __init__(self,txid,fee,weight,parents):
		self.txid=txid
		self.fee=fee
		self.weight=weight
		self.parents=parents

	def get_taxid(self):
		return self.txid
	def get_weight(self):
		return self.weight
	def get_fee(self):
		return self.fee
	def get_parents(self):
		return self.parents

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
				lst.append(MempoolTransaction(row[0],row[1],row[2],row[3].strip().split(';')))
		
	
def write_transactions():
	""" writes the valid transactions in transactions.txt"""
	mempool=[]
	file=open("Transactions.txt","a")
	#for i in lst:
	#	if(i.)

	file.close()



parse_mempool_csv()
for i in lst:
	print(i.get_parents())