#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("sudo apt install figlet")
os.system("clear")
os.system("figlet RAR-ZIP CRACKER AZE")
print("""

1) RAR Şifrə Qırmaq 
2) ZİP Şifrə Qırmaq
3) Qırılan Şifrələri Göstər
--- Tərcümə edən: Elman Kərimli || emikridat@gmail.com ---


""")

secim = input("Seçim : ")

if(secim=="1"):	
	rar = input("RAR Faylı : ")
	print("")
	os.system("sudo rar2john " + rar + " > hash.txt")
	os.system("sudo john hash.txt --pot=sifre.txt")


elif(secim=="2"):	
	zipdo = input("ZİP Faylı : ")
	print("")
	os.system("sudo zip2john " + zipdo + " > hash.txt")
	os.system("sudo john hash.txt --pot=sifre.txt")

elif(secim=="3"):
	print("")
	os.system("sudo cat sifre.txt")




