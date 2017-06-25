import json
from json import JSONDecoder
import re
import nltk
from nltk.tag import pos_tag, map_tag
from nltk.tag.stanford import StanfordNERTagger

def ret_password(passwd):
	tok = passwd.split(' ')
	p = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,20}')
	passwd = ''
	for i in tok:
		if p.search(i) is not None:
			passwd = p.search(i).group()
	return passwd

data = json.load(open('jsonChat.json'))
print ('Welcome to online recharge.')
mob = ''
passw = ''
email = ''

# while mob == '':
#  mob = input("Please provide your "+data[0]["ask"][0]+'\n')
#  text = nltk.word_tokenize(mob)
#  posTagged = pos_tag(text)
#  simplifiedTags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in posTagged]
#  for i,j in simplifiedTags:
# 	   if j == 'NUM' and len(i) == 10:
# 		     mob = str(i)
# 		     break
# 	   else:
# 		     mob = ''
#  if mob == '':
# 	   print ('please give correct information')
# while passw == '':
#  passw = input("Please provide your "+data[0]["ask"][1]+'\n')
#  passw = ret_password(passw)	
#  if passw == '':
# 	   print ('please give correct information')

# while email == '':
#  email = input("Please provide your "+data[0]["ask"][2]+'\n')
#  if email == '':
# 	   print ('please give correct information')

# data[0]["ask"][0] = mob
# data[0]["ask"][1] = passw
# data[0]["ask"][2] = email
# print("Thank you for your information!\n")
def options():
	print ('Please select from the below options for the type of recharge\n')
	# print ('con ',open(str(data[1]["rechargeTypes"])).read())
	f = json.load(open(data[1]["rechargeTypes"]))
	for j,i in enumerate(f):
		print (str(j+1)+' : '+i)

	print ()
	# print ()
	opt = input('')
	# if(int(opt)>len(f)):
	# 	    return opt,1
	finOpt = ''
	num = 0
	# print ('opt is '+opt+' dtype is ',type(opt))
	for j,i in enumerate(range(len(f))):
		if opt.lower() == f[j].lower():
			finOpt = opt.lower()
			num = int(j)
			break
		elif len(opt) == 1 and (j) == (int(opt)-1):
			num = int(opt)
			finOpt = f[j].lower()
			break

	print ("The "+finOpt+" options are as follows -")
	print ()
	# print ('num s ',num)
	# print ('finopt s ',finOpt)

	flag = 0
	fl = 0
	f = json.load(open(data[2]["rechargeSubTypes"]))
	# print ('f ',f)
	# print ('rst is ',f[0])
	for j,i in enumerate(range(len(f))):
		if str(finOpt) in f[j].keys():
			for i,k in enumerate(f[j][finOpt]):
				print (str(i+1)+' : '+k)
				flag = 1
		else:
			print()
	print()
	f = json.load(open(data[2]["rechargeSubTypes"]))
	  
	flag2 = 0
	if flag == 1:
		subcat = input('')
		# if(int(subcat)>len(f)):
		#     return subcat,1
		for i,j in enumerate(range(len(f))):
			# print (f[j].keys())
			# print ('finopt ',finOpt)
			if finOpt in f[j].keys():
				for k in f[j][finOpt]:
					if len(subcat) == 1:
						fl = int(subcat)
						subcat = f[j][finOpt][int(subcat)-1].lower()
						# print ('len is ',len(f[j][finOpt]))
						# print ('f1 is ',fl)
						if fl == len(f[j][finOpt]):
							# print ('here')
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
	# print ('subcat is ',subcat)
	# print ("The "+subcat+" options are as follows -")
	return subcat,flag2	

# print ("Please type in the options for what you are here:-\n")
subcat,num = options()
print ('num from outside ',num)
while num == 1:
	print ("Please type in the options for what you are here:-\n")
	print ('num is ',num)
	subcat,num = options()
if num == 4:
	print ('subcat is ',subcat)
f = json.load(open(data[3]["giveOptions"]))
a=1
for i in f:
	if str(subcat) in i.keys():
		for j in  (i[str(subcat)]):
			print (str(a)+' : '+j)
			a+=1
		break		
final = input(' ')
print("Your recharge will be done")
print("Thank you!! Have a great day :)");
