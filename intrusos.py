#!/usr/bin/python
# -*- coding: utf-8 -*-

import commands
import subprocess

#Autor albceru
#Programa para detectar intrusos en la red, si la mac no coincide con las almacenadas por el usuario en mac_amigas
#Rellenar archivo mac_amigas con las mac que se conozcan poniendo una mac por línea   .
#Se necesita tener instalado nmap

mac_amigas = []
archivo = open("mac_amigas","r")

for mac in archivo.readlines():
    mac_amigas.append(mac[:-1])


archivo.close()
gateway_red= commands.getoutput('route | grep default|awk \'{print $2 "#"$8}\'')
gateway_red=gateway_red.split("\n")[0]

gateway, red = gateway_red.split("#")
ip = commands.getoutput("ifconfig "+red+" | sed -n 2p |grep inet |cut -c 23-34")

scaneo=commands.getoutput("nmap -sP "+gateway+"/24 |grep scan | cut -c 22-33 |sed '$d'")


mac_router=commands.getoutput("arp "+gateway+" |grep ether| cut -c 34-50")
mac_amigas.append(mac_router)


scaneo = scaneo.split('\n')
texto = ''
for linea in scaneo:
    if not linea in ip:
        mac=commands.getoutput("arp "+linea+" |grep ether| cut -c 34-50")

        if not mac in mac_amigas:
            texto+="Intruso = "+linea+" => "+mac+"\n"
if texto:

    print texto
