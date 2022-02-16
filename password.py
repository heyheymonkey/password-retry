password = "a123456"
i = 0
while i < 3:
	num = input("請輸入密碼:")
	if num != password:
		print("密碼錯誤!",2-i,"次機會")
		i = i + 1
	else:
		print("登入成功!")
		break