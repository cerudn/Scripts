#!/usr/bin/python
import sys, subprocess
# Autor albceru

import commands
import subprocess

gateway_red= commands.getoutput('route | grep default|awk \'{print $2 "#"$8}\'')
gateway_red=gateway_red.split("\n")[0]

gateway,red = gateway_red.split("#")
ip = commands.getoutput("ifconfig "+red+" | sed -n 2p |grep inet |cut -c 23-34")

scaneo=commands.getoutput("nmap -sP "+gateway+"/24 |grep scan | cut -c 22-33 |sed '$d'")

print scaneo

lineas =scaneo.split('\n')

numeros=0
for numero in lineas:
	numeros += 1

print "dispositivos conectados a la red "+ str(numeros)
