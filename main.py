from cloudflare import get_current, update_dns, get_current_ip
from notif import sendNotification
from colorama import Fore
from time import sleep
import json

try:
	with open('config.json') as json_file:
		config = json.load(json_file)
except:
	print(f"[{Fore.RED}+{Fore.RESET}] => Le fichier de configuration est introuvable")
	quit()

def main():
	print(f"[{Fore.BLUE}+{Fore.RESET}] => Le script de mise à jour de Cloudflare a été lancé")
	sendNotification("info","Information" , "Le script de mise à jour de Cloudflare a été lancé")
	sleep(5)
	count = 0
	old_ip = None
	old_table = {}

	current_ip = get_current_ip()
	current_ip = "120.130.134.148"
	response = get_current(config["email"], config["global_key"])

	if response is None:
		print(f"[{Fore.RED}+{Fore.RESET}] => La configuration de Cloudflare est None")
		sendNotification("error","Error" , "La configuration de Cloudflare est None. Check ASAP.")
		quit()

	if response["success"]:
		print(f"[{Fore.GREEN}+{Fore.RESET}] => La configuration de Cloudflare a bien été récupérée")
	else:
		print(f"[{Fore.RED}+{Fore.RESET}] => La configuration de Cloudflare n'a pas été récupérée")
		sendNotification("error","Error" , "La configuration de Cloudflare n'a pas été récupérée.")
		quit()

	for record in response["result"]:
		if record["type"] == 'A' and old_ip is None:
			old_ip = record['content']
			old_table = record
		if record["content"] == current_ip:
			count += 1

	if old_ip is None:
		print(f"[{Fore.RED}+{Fore.RESET}] => L'ancienne IP est NULL")
		sendNotification("error","Error" , "L'ancienne IP est NULL. Check ASAP.")
		quit()

	if old_table == {}:
		print(f"[{Fore.RED}+{Fore.RESET}] => La table de l'ancienne IP est vide")
		sendNotification("error","Error" , "La table de l'ancienne IP est vide. Check ASAP.")
		quit()

	if count > 0:
		print(f"[{Fore.GREEN}+{Fore.RESET}] => La configuration de Cloudflare était déjà à jour")
		sendNotification("success","Success" , "La configuration de Cloudflare était déjà à jour. Aucune modification à eu lieu")
		quit()
	else:
		print(f"[{Fore.RED}+{Fore.RESET}] => La configuration de Cloudflare n'était pas à jour. Mise à jour en cours")
		sendNotification("info","Information" , "La configuration de Cloudflare n'était pas à jour. Tentative de mise à jour en cours...")
		sleep(5)
		update_result = update_dns(config["email"], config["global_key"], old_table["name"],current_ip, f"{old_ip} -> {current_ip}", config["is_proxied"])
		if update_result is None:
			print(f"[{Fore.RED}+{Fore.RESET}] => L'Update de Cloudflare est None. Check ASAP")
			sendNotification("error","Error" , "L'Update de Cloudflare est None. Check ASAP")
			quit()
		if update_result["success"]:
			print(f"[{Fore.GREEN}+{Fore.RESET}] => La configuration de Cloudflare a bien été mise à jour")
			sendNotification("success","Success" , "La configuration de Cloudflare a bien été mise à jour.")
		else:
			print(f"[{Fore.RED}+{Fore.RESET}] => La configuration de Cloudflare n'a pas été mise à jour")
			sendNotification("error","Error" , "La configuration de Cloudflare n'a pas été mise à jour.")

if __name__ == '__main__':
	main()
