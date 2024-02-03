import json
import requests

with open('config.json') as json_file:
	config = json.load(json_file)

def sendNotification(type, title, message):
	if type.lower() == "error":
		print(message)
		requests.post(config["ntfy"]["error"],
			data=message,
			headers={
				"Title": title,
				"Tags": "x"
			})
		if config["debug"]:
			print("Sent error notification")
	elif type.lower() == "success":
		requests.post(config["ntfy"]["success"],
			data=message,
			headers={
				"Title": title,
				"Tags": "white_check_mark"
			})
		if config["debug"]:
			print("Sent success notification")
	elif type.lower() == "alert":
		requests.post(config["ntfy"]["alert"],
			data=message,
			headers={
				"Title": title,
				"Tags": "warning"
			})
		if config["debug"]:
			print("Sent alert notification")
	else:
			requests.post(config["ntfy"]["info"],
				data=message,
				headers={
					"Title": title,
					"Tags": "information_source"
				})
			if config["debug"]:
				print("Sent info notification")
