#!/usr/bin/python
import urllib.request
import json


# Function used to open the link of the raw json data, storing it and passing it
def OpeningLink():
	# Opens the link and stores the result in the variable
	request = urllib.request.urlopen('https://raw.githubusercontent.com/silverwind/port-numbers/master/ports.json')
	data = request.read()
	data = json.loads(data)
	return data
	

# Function used to get proper values of the atributes based on the tag of port number and protocol type
def GettingJSONValues(port_num, tcp_udp):
	try:
		# Gets the whole value of the raw json data of the webpage
		json_data = OpeningLink()
		# Creates a tag based on the user inputted port number and protocol type
		tag = str(port_num) + "/" + str(tcp_udp)
		# Returns the JSON object with that specific tag
		return json_data[tag]
	# Used when there are no JSON object with that port number and that protocol type
	except KeyError:
		print("The port " + port_num + " has no correlation with protocol " + tcp_udp + "...")
		print("\n")
		# Returns the failed message
		return "Failed"