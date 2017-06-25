from flask import Flask , abort , jsonify,request,render_template
import json
from json import JSONDecoder
import spell

app=Flask(__name__)

done=[]
success=[]
flag = 0
data = json.load(open('jsonChat.json'))

@app.route("/",methods=['GET','POST'])
def index():
	lis=[]
	del done[:]
	del success[:]
	lis.append('Welcome to online recharge')
	lis.append('Please select from the below options for the type of recharge')
	# print ('after return')
	f = json.load(open(data[1]["rechargeTypes"]))
	for j,i in enumerate(f):
		lis.append(str(j+1)+' : '+i)	
	return render_template('chatWindow.html',data=lis)

def options2(opt,f):
	if opt.isdigit():
		token = opt.split(' ')
	else:
		opt = spell.correction(opt.lower())
		token = opt.split(' ')
	

	checkFlag=0
	print ('token is ',token)
	print ('f is ',f)
	for i in token:
		for k,j in enumerate(range(len(f))):
			print ('j is ',j)
			print ('i is ',i)
			print ('k is ',k)
			if len(i)==1:
				opt=str(i)
				# print ('f j ',f[int(opt)-1])
				if int(opt)-1 > len(f):
					i = 'Rs '+i
					print ('i from here ',i)
				else:
					checkFlag=1
					break
			if len(i.lower())>=2 and i.lower() in f[j].lower():
				opt=str(k+1)
				checkFlag=1
				break
		if checkFlag==1:
			break
	print ('opt is ',opt)
	return opt,checkFlag

def options(opt,f):
	opt = spell.correction(opt.lower())
	token = opt.split(' ')		
	checkFlag=0

	# print ('f is ',f)
	for i in token:
		for j in f:
			# print ('j is ',j)
			# print ('i is ',i)
			if len(i)==1 and (int(i)==1 or int(i)==2 or int(i)==3 or int(i)==4 or int(i)==5):
				opt=str(i)
				checkFlag=1
				break
			if len(i.lower())>2 and i.lower()in j.lower():
				opt=str(j)
				checkFlag=1
				break
		if checkFlag==1:
			break
	return opt,checkFlag

@app.route("/parse_data",methods=['GET','POST'])
def chat():
	lis=[]
	
	if len(done)==0:
		opt = request.json
		# opt = spell.correction(opt.lower())
		# token = opt.split(' ')
		f = json.load(open(data[1]["rechargeTypes"]))
		# checkFlag=0
		# for i in token:
		# 	for j in f:
		# 		print ('j is ',j)
		# 		print ('i is ',i)
		# 		if len(i)==1 and (int(i)==1 or int(i)==2 or int(i)==3 or int(i)==4 or int(i)==5):
		# 			opt=str(i)
		# 			checkFlag=1
		# 			break
		# 		if len(i.lower())>2 and i.lower()in j.lower():
		# 			opt=str(j)
		# 			checkFlag=1
		# 			break
		# 	if checkFlag==1:
		# 		break
		opt,checkFlag=options(opt,f)
		if checkFlag==0:
			return jsonify(lis=9999)
		print ('opt is ',opt.lower())
		# print ('token is ',token)
		# print ('opt is ',opt)		
		num = 0
		f = json.load(open(data[1]["rechargeTypes"]))
		for j,i in enumerate(range(len(f))):
			if opt.lower() == f[j].lower():
				finOpt = opt.lower()
				num = int(j)
				break
			elif len(opt) == 1 and (j) == (int(opt)-1):
				num = int(opt)
				finOpt = f[j].lower()
				break	
		# lis=[]
		lis.append("The "+finOpt+" options are as follows -")
		
		flag = 0
		fl = 0
		f = json.load(open(data[2]["rechargeSubTypes"]))
		for i in f[0].keys():
			print ('i from here is '+i)
		for j,i in enumerate(range(len(f))):			
			if str(finOpt) in f[j].keys():
				# print ('finOpt '+str(finOpt)+' '+f[j][finOpt])
				for i,k in enumerate(f[j][finOpt]):
					lis.append(str(i+1)+' : '+k)					
					flag = 1

		done.append(opt)
		done.append(flag)
		done.append(finOpt)
		# print('done from 1 ',done)
		success.append(finOpt)
		subcat = finOpt
		if flag==0:
			f = json.load(open(data[3]["giveOptions"]))
			a=1
			for i in f:
				if str(subcat) in i.keys():
					for j in  (i[str(subcat)]):
						lis.append(str(a)+' : '+j)
						# print (str(a)+' : '+j)
						a+=1
					break
			success.append(subcat)
	elif len(success)==1:		
		# print('done ',done)
		finOpt = done.pop()
		flag=done.pop()		
		print('flag ',flag)
		f = json.load(open(data[2]["rechargeSubTypes"]))
		flag2 = 0
		if flag == 1:
			subcat = request.json

			# subcat,checkFlag=options(subcat,f[finOpt])
			# print('subcat ',subcat)
			# if(int(subcat)>len(f)):
			#     return subcat,1
			for i,j in enumerate(range(len(f))):
				# print (f[j].keys())
				# print ('finopt ',finOpt)
				if finOpt in f[j].keys():
					for k in f[j][finOpt]:
						subcat,checkFlag=options2(subcat,f[j][finOpt])
						if checkFlag ==0:
							flag2=1
							break
						if len(subcat) == 1:
							fl = int(subcat)
							subcat = f[j][finOpt][int(subcat)-1].lower()
							# print ('len is ',len(f[j][finOpt]))
							# print ('f1 is ',fl)
							if fl == len(f[j][finOpt]):								
								flag2 = 1
							break
						else:
							fl = f[j][finOpt].index(subcat)+1
							if fl == len(f[j][finOpt]):
								flag2 = 1
							break					
				else:
					print()

		else: subcat = finOpt
		if flag2==1:
			return jsonify(lis=9999)		
		
		f = json.load(open(data[3]["giveOptions"]))
		a=1
		for i in f:
			if str(subcat) in i.keys():
				for j in  (i[str(subcat)]):
					lis.append(str(a)+' : '+j)
					print (str(a)+' : '+j)
					a+=1
				break
		success.append(subcat)
		print ('success ',len(success))
	else:
		final = request.json
		subcat = success.pop()
		flag2 = 0
		f = json.load(open(data[3]["giveOptions"]))
		for i,j in enumerate(range(len(f))):
				# print (f[j].keys())
				# print ('finopt ',finOpt)
				if str(subcat) in f[j].keys():
					for k in f[j][subcat]:
						final,checkFlag=options2(final,f[j][subcat])
						# print ('final is ',final)
						if checkFlag ==0:
							flag2=1
							break
						if len(final) == 1:
							fl = int(final)
							final = f[j][subcat][int(final)-1].lower()
							print ('subcat is ',subcat)
							print ('len is ',len(f[j][subcat]))
							print ('f1 is ',fl)
							if fl == len(f[j][subcat])+1:
								flag2 = 1
							break
						else:
							fl = f[j][subcat].index(final)+1
							if fl == len(f[j][subcat]):
								flag2 = 1
							break					
				else:
					print()
		
		if flag2==1:
			return jsonify(lis=9999)

		print ('final subcat ',final)
		lis.append('So your final recharge to be done is '+final)
		lis.append("Your recharge will be done soon")
		lis.append("Thank you!! Have a great day :)")
		del done[:]
		del success[:]
		# print ('done ',done)
		# print ('success ',success)

	return jsonify(lis=lis)


if __name__ == '__main__':
	app.run(port=8081,debug=True)    