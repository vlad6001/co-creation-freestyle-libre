from requests_toolbelt import MultipartEncoder
import requests
import json
import time
import datetime
import math

url = "https://api3.gamebus.eu/v2/activities?dryrun=false&fields=personalPoints.value"

import csv

first = 1
files = []

first_part = """{
				"gameDescriptor":"61",
				"dataProvider":"1",
				"date":""" 
added_part1 = """,
				"propertyInstances":[
				 {
					"property":"87",
					"value":"""
added_part2 = """},
				 {
					"property":"88",
					"value":"""
				



second_part = """},
				 {
					"property":"89",
					"value":"""
third_part = """}
			  ],
			  "players":[
				 "339"
			  ]
		    }"""


with open('glucose-test-data2.csv') as file:
	r = csv.reader(file)
	for row in r:
		if row[2] != "" and first > 2:
			#print(row[2])
			
			date_time_obj = datetime.datetime.strptime(row[2], '%m/%d/%Y %H:%M')
			
			time_tuple = date_time_obj.timetuple()
			#print(time_tuple)
			
			timestamp = int(time.mktime(time_tuple))
			hours = (timestamp% 86400) / 3600
			minutes = timestamp%3600
			#print(str(timestamp))
			print(hours)
			
			
			my_string = first_part+str(timestamp)+"000"+added_part1
			#print(str(time_tuple[3])+":"+str(time_tuple[4]))
			my_string = my_string + '"2020-05-20 11:10"' + added_part2
			#+str(timestamp)+"000"
			
			
			if row[4] == "":
				my_string = my_string+"0"
			else:
				my_string = my_string+row[4]
				
			my_string = my_string + second_part
			
			if row[5] == "":
				my_string = my_string+"0"
			else:
				my_string = my_string+row[5]
				
			my_string = my_string + third_part
			
			payload = MultipartEncoder(fields={
				"activity":my_string
			})
			
			headers = {
			   'Authorization': 'Bearer 8b4b3e37-9581-4ea3-abe9-d0090e40b52e',
			   #'Content-Type': 'multipart/form-data; boundary=---WebKitFormBoundary7MA4YWxkTrZu0gW'
			   'Content-Type': payload.content_type
			}

			#print("ceva6")
			
			#print(payload)

			response = requests.request("POST", url, headers=headers, data = payload)
			print(response.text.encode('utf8'))
			
		else:
			first = first+1








