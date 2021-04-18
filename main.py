records=[]
balanceCheck=[]
class Budget:
	def __init__(self,name):
		self.name=name 
	def deposit(self,amount,use):
		self.amount=amount
		self.use=use
		records.append ({self.amount:self.use})
		print(f"successfully deposited {self.amount} naira for {self.use} in {self.name} budget")
		print(records)
	def withdraw(self,amount,need):
		self.amount=amount
		self.need=need
		records.append({-self.amount:self.need})
		print(f"succesful withdrawal of {self.amount} for {self.need} from {self.name} budget")
		print(records)
	def transfer(self,amount,receiver):
		self.amount=amount
		self.receiver = receiver 
		records.append({-self.amount:self.receiver})
		print(f"{self.amount} naira was transfered from {self.name} budget to {self.receiver} budget successfully.")
		print(records)
	def balance(self):
		for transactions in records:
			for key in transactions.items():
				print(key)
				balanceCheck.append(key[0])
		print(balanceCheck)
		balance=sum(balanceCheck)
		print(f" Available balance in food budget is {balance} naira")
		
print("WELCOME TO SURE BUDGET")
x=True
while x==True:
	print("Budget categories include \n 1 food \n 2 clothing \n 3 health \n 4 miscellanous \n 5 exit")
	category= int(input("Select a budget category : "))
	if category ==1:
		name="food"
	elif category ==2:
		name= "clothing"
	elif category ==3:
		name ="health"
	elif category==4:
		name = "miscellanous"
	elif category==5:
		exit()
	else:
		print("Invalid category")
		continue 
		x=False
	name=Budget(name)
	isoptionvalid=True
	while isoptionvalid==True:
		action=int(input("1 deposit \n 2 withdrawal\n 3 transfer \n 4 check balance\n select an action:"))
		if action==1:
			amount=int(input("How much to be deposited:\n"))
			use=input("What to be used for:\n")
			print(amount ,use)
			name.deposit(amount,use)
		elif action==2:
			amount=int(input("How much to be withdrawn :\n"))
			need=input("what is it needed for:\n")
			name.withdraw(amount,need)
		elif action==3:
			amount=int(input("How much do you want to transfer:\n"))
			receiver=input("What category do you wish to transfer to:\n")
			name.transfer(amount,receiver)
		elif action==4:
			name.balance()
		else :
			print("invalid action")
			isoptionvalid=False
		another=int(input("Do you want to perform another transaction? 1 yes or 2 no:"))
		if another==1:
			pass
		else:
			exit()
	