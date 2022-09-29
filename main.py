#!/usr/bin/python
import modules


# Main function
def main():
	# Variable used to store the user input of port number
	port_num = input("Input the number of a port: ")
	
	# Used to check if the user input is of int type, if not throws a valueerror
	try:
		int(port_num)
		it_is = True
	except ValueError:
		it_is = False

	# If it threw valueerror this if catches it and restarts the process of inputting
	if not it_is:
		print("Please input a number.")
		main()

	# Variable used to stores the user input either of tcp or udp, other are not allowed
	tcp_udp = input("Is it used in UDP or TCP protocol? (udp/tcp): ").lower()

	# Checks if the input is something else than tcp or udp, if it restarts the whole process of inputting
	if str(tcp_udp) != 'udp' and str(tcp_udp) != 'tcp':
		print("Please input a valid option.")
		main()

	# Variable used to store the JSON object retrived through the function inside modules.py
	data = modules.GettingJSONValues(port_num, tcp_udp)

	# Checks if something went wrong with the GettingJSONValues function process
	if str(data) == "Failed":
		main()

	# Used to check if the JSON atribute name of the current object has no value then shows proper message, if it has show that value
	try:
		if str(data['name']) == "":
			print("Name: Unassigned")
		else: 
			print("Name: " + str(data['name']))	
	except KeyError:
		# If the object does not have that JSON atribute
		print("Name: Unavailable")
	
	# Used to check if the JSON object doesn't have the value appended to that atribute
	try:
		if str(data['description']) == "":
			print("Description: Unassigned")
		else:
			print("Description: " + str(data['description']))
	except KeyError:
		# If the object does not have that JSON atribute
		print("Description: Unavailable")

	# Used to store the user choice if they want to quit or not
	again = input("Do you wish to exit? (yes/no): ").lower()

	print("\n")
	# Exits if yes
	if again == "yes":
		print("Goodbye!")
		exit()

	# Restarts the process if not
	if again == "no":
		main()


if __name__ == "__main__":
	main()