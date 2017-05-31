#!/usr/bin/python
# -*- coding: utf-8 -*-

import commands
import subprocess

#Autor albceru
#Programa para detectar intrusos en la red, si la mac no coincide con las almacenadas por el usuario en mac_amigas
#Rellenar archivo mac_amigas con las mac que se conozcan poniendo una mac por línea   .
#Se necesita tener instalado nmap

entrada =-1
while entrada is -1:
    print "Introduce 0 para obtener las ip y el numero de dispositivos que hay en la red"
    print "Introduce 1 para comprobar si hay intrusos "
    entrada = input()

    if entrada != 0 and entrada !=1 :
        entrada =-1
        print "Introduce 1 o 0 \n"
    print "\n"    
mac_amigas = []
ips =[]
archivo = open("mac_amigas","r")

# for mac in archivo.readlines():
#     mac_amigas.append(mac[:-1])
#
#
# archivo.close()
gateway_red= commands.getoutput('route | grep default|awk \'{print $2 "#"$8}\'')
gateway_red=gateway_red.split("\n")[0]

gateway, red = gateway_red.split("#")
ip = commands.getoutput("ifconfig "+red+" | sed -n 2p |grep inet |cut -c 23-34")

scaneo=commands.getoutput("nmap -sP "+gateway+"/24 |grep scan | cut -c 22-33 |sed '$d'")




if entrada is 0:
    ips.append(ip)
    ips.append(gateway)
    lineas =scaneo.split('\n')
    print gateway + " Router"
    print ip +" Mi dispositivo"
    numeros=0
    for numero in lineas:
    	numeros += 1

    	if not numero in ips:

    		print numero



    print "dispositivos conectados a la red "+ str(numeros)
elif entrada is 1:


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
