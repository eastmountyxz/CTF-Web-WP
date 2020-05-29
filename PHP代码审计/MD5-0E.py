import hashlib
import re
import random
import requests

def md5():
	global dict_az
	dict_az = 'abcdefghijklmnopqrstuvwxyz'
	i = 0
	while True:
		result = ''
		result += str(i)
		i = i + 1
		hashed_s = hashlib.md5(result.encode('utf-8')).hexdigest()
		r = re.match('^0e[0-9pggnb]{30}', hashed_s)
		if r:
			print("[+] found! md5( {} ) ---> {}".format(result, hashed_s))
			exit(0)

		if i % 1000000 == 0:
			print("[+] current value: {}       {} iterations, continue...".format(result, str(i)))

md5()
#11230178 md5值0e732639146814822596b49bb6939b97
