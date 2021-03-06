import urllib2
import time
from datetime import datetime

TEST_URI = "http://www.google.com"
TIMEOUT = 2
MAX_BUFFER_LEN = 100
WAIT_TIME = 30
file_num = 1
results = []

def ping_google_dns():
	try:
		response = urllib2.urlopen(TEST_URI, timeout = TIMEOUT)
		return True
	except urllib2.URLError as err: pass
	return False

def flush_results():
	global file_num
	global results
	
	filename = "internet_status_" + str(file_num) + ".csv"
	file_num = file_num + 1
	file_handle = open(filename, "w")
	for line in results:
		file_handle.write(line + "\n")
	file_handle.close()
	results = []

def check_internet():
	global results

	is_connected = ping_google_dns()
	timestamp = str(datetime.now())
	status = "connected" if is_connected else "disconnected"
	
	result_str = status + "," + timestamp
	print result_str
	results.append(result_str)

	if len(results) >= MAX_BUFFER_LEN:
		flush_results()

def loop():
	check_internet()
	time.sleep(WAIT_TIME)

while True:
	loop()
		
