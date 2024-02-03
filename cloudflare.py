from colorama import Fore
import requests
import json

with open('config.json') as json_file:
	config = json.load(json_file)

def get_current(email, global_api):
	url = f'https://api.cloudflare.com/client/v4/zones/{config["zone_id"]}/dns_records'

	headers = {
		'Content-Type': 'application/json',
		'X-Auth-Email': email,
		'X-Auth-Key': global_api,
	}

	response = requests.request("GET", url, headers=headers)
	return response.json()

def update_dns(email, global_api, name, new_ip, desc = "New IP has been set.", proxied = True):
	url = f'https://api.cloudflare.com/client/v4/zones/{config["zone_id"]}/dns_records/{config["record_id"]}'

	headers = {
		'Content-Type': 'application/json',
		'X-Auth-Email': email,
		'X-Auth-Key': global_api,
	}

	data = {
		"content": new_ip,
		"name": name,
		"proxied": proxied,
		"type": "A",
		"comment": desc
	}

	response = requests.put(url, headers=headers, data=json.dumps(data))

	return response.json()

def get_current_ip():
	return requests.get("https://api.ipify.org").text
