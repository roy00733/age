driving = input('你有開過車嗎? ')
if driving != '有' and driving !='沒有':
	raise SystemExit
age = input('請輸入年齡 ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你可以開車了')
	else:
		print('你怎麼可以開車?')
else:
	if age >= 18:
		print('你可以去考駕照了')
	else:
		print('請等18歲以後再考駕照')