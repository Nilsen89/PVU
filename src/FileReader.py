# Written By: Christoffer A. Nilsen
# Date: 23/02/2016
# Purpose: Read in data from blackbox/file

import json
import time

first = True

def main():
	url = "../data/test.json"
	open_file(url)

def open_file(url):
	
	data = []
	json_data = []
	old_timestamp = 0
	
	with open(url) as f:
		data.extend(f.readlines())
		f.close()
	for i in range(len(data)):
		json_data = json.loads(data[i])
		old_timestamp = sleeper(json_data["timestamp"], old_timestamp)
		
		print json_data["name"]
		print json_data["value"]
		print json_data["timestamp"]
		
def sleeper(cur_timestamp, old_timestamp):
	global first
	if not first:
		if cur_timestamp > old_timestamp:
			time.sleep(cur_timestamp-old_timestamp)
	else:
		first = not first
		old_timestamp = cur_timestamp
	return old_timestamp
	
main()