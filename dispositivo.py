#!/usr/bin/python
import sys, subprocess
# Autor albceru

import commands
import subprocess
ips=[]
gateway_red= commands.getoutput('route | grep default|awk \'{print $2 "#"$8}\'')
gateway_red=gateway_red.split("\n")[0]

gateway,red = gateway_red.split("#")
ip = commands.getoutput("ifconfig "+red+" | sed -n 2p |grep inet |cut -c 23-34")

scaneo=commands.getoutput("nmap -sP "+gateway+"/24 |grep scan | cut -c 22-33 |sed '$d'")



lineas =scaneo.split('\n')
ips.append(ip)
ips.append(gateway)

print gateway + " Router"
print ip +" Mi dispositivo"
numeros=0
text =''
for numero in lineas:
	numeros += 1
	if not numero in ips:
		text = numero +"\n"



print text+"dispositivos conectados a la red "+ str(numeros)
