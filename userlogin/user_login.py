#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys

username = input("Please input your name:").strip()
user_data = open('userdata','r+')
#user_data.seek(0,0)
user_flag=False        #设置一个标记.判断这个用户在数据库存在的话将其值改为真
for userline in user_data.readlines():
	userline = userline.strip().split(":")
	if userline[0] ==username and userline[2] =="lock":
		print("User:%s is Locked!" % username)
		#break
		sys.exit()
	elif userline[0] ==username:
		i = 0
		user_flag=True
		while i < 3:
			password = input("Please input your password:")
			if userline[1] ==password:
				print("User：%s is login sucess!" % username)
				sys.exit()
			else:
				print("Logon failure : unknown user name or bad password.")
				i += 1
		else:
			userline[2] = 1
			sys.exit("You tried too many times,You username will be lock!")
if user_flag!=True:			#当把数据文件遍历完仍然没发现这个用户.他的值还是假
	print("用户名不存在！")
user_data.close() # 还有就是程序sys.exit退出了.这个还怎么执行?

