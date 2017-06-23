#! /usr/bin/env python

"""
	Complete the code below to modify the dialog threshold value.
	- Look through API documentation online
	- Find the functions you need
	- 

	Usage : python threshold.py --ip <ip_of_my_robot> --threshold 0.4

	Example output :
	Starting threshold modification script
	Threshold is: 0.499999988079
	Threshold is now: 0.5
	Enter a new value between 0 and 1 (ctrl+C to exit): 0.4
	Threshold is now: 0.40000000596
	Enter a new value between 0 and 1 (ctrl+C to exit):

"""

import qi
import argparse
import sys
import time
    

def main(session, threshold):
	"""
	Example : modification of threshold
	"""
	# 1/ Get the services 
	service_conn = session.service("ALDialog")

	# 2/ get current value
	th = service_conn.getConfidenceThreshold("BNF", "enu")
	print "Threshold is: " + str(th)

	# 3/ set new value
	set_threshold(service_conn, threshold)
	
	# 4/ get current value
	th = service_conn.getConfidenceThreshold("BNF", "enu")
	print "Threshold is now: " + str(th)

	"""
	Loop on, wait until manual interruption.
	"""
	try:
		while True:
			th = float(raw_input("Enter a new value between 0 and 1 (ctrl+C to exit): "))
			set_threshold(service_conn, th)

	except KeyboardInterrupt:
		print "Interrupted by user, stopping script"
		# unsubscribe what is needed here if necessary
		
		#stop
		sys.exit(0)

def set_threshold(service_conn, threshold):
	# set new value
	service_conn.setConfidenceThreshold("BNF", threshold ,"enu")
	# get current value
	th = service_conn.getConfidenceThreshold("BNF", "enu")
	print "Threshold is now: " + str(th)

if __name__ == "__main__":

	print "Starting threshold modification script"
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
	parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
	parser.add_argument("--threshold", type=float, default=0.5,
                        help="Threshold value")

	args = parser.parse_args()
	session = qi.Session()
	try:
		session.connect("tcp://" + args.ip + ":" + str(args.port))
	except RuntimeError:
		print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
		sys.exit(1)

	# run script
	main(session, args.threshold)
