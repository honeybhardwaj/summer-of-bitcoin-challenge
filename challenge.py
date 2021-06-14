import csv

class MempoolTransaction:
	"""class for transactions in mempool"""
	
	def __init__(self,txid,fee,weight,parents):
		self.txid=txid
		self.fee=fee
		self.weight=weight
		self.parents=parents

	# getter functions
	def get_taxid(self):
		return self.txid
	def get_weight(self):
		return self.weight
	def get_fee(self):
		return self.fee
	def get_parents(self):
		return self.parents

# List of  Mempool Transactions
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
		
	
def checkflag(flag):
	""" checker function for checking whether all parents are present"""
	element = True
	for i in flag:
		element= element & i
	return element

def write_transactions():
	""" writes the valid transactions in transactions.txt"""
	mempool=["",]
	file=open("Block.txt","a")
	
	for i in lst:
		if(int(i.get_weight())<4000000):
			flag=[]		
			for j in i.get_parents():				
				if(j in mempool):             # checks for all parent and add them in a flag list
					flag.append(True)
				else:
					flag.append(False)
			if(checkflag(flag)):
				mempool.append(i.get_taxid())    # if all condition are met write them in txt file
				file.write(i.get_taxid()+'\n')
	file.close()


# driver code 
parse_mempool_csv()
write_transactions()

