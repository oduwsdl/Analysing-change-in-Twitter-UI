import sys
import json
from haralyzer import HarParser, HarPage
from collections import Counter
import dateutil, datetime
import numpy as np

with open(sys.argv[1], 'rb') as f:
	har_parser = HarParser(json.loads(f.read()))

### ACCESSING FILES ###
f=open(sys.argv[2], 'w')

timelist=[]
entries = []

for har_page in har_parser.pages:
	# print("Sizes:")
	# print(har_page.page_size)
	# print(har_page.image_size)
	# print(har_page.text_size)
	# print(har_page.css_size)
	# print(har_page.js_size)
	# print(har_page.audio_size)
	# print(har_page.video_size)
	# print("Size Transferred:")
	# print(har_page.page_size_trans)
	# print(har_page.image_size_trans)
	# print(har_page.text_size_trans)
	# print(har_page.css_size_trans)
	# print(har_page.js_size_trans)
	# print(har_page.audio_size_trans)
	# print(har_page.video_size_trans)
	# print("Load Time")
	# print(har_page.initial_load_time)
	# print(har_page.page_load_time)
	# l = ['image', 'html', 'css', 'javascript', 'text']
	# for item in l:
	# 	print(f'browser load time for {item}: {har_page.get_load_time(content_type=item)}')
	# 	print(f'total load time for {item}: {har_page.get_load_time(content_type=item, asynchronous=False)}')
	for entry in har_page.entries:
		#entries.append(entry)
		date=entry['startedDateTime']
		#timelist.append(dateutil.parser.parse(date))
		url=entry['request']['url']
		status=entry['response']['status']
		method=entry['request']['method']
		mtype=entry['response']['content']['mimeType']
		out=f"{date}\t{url}\t{status}\t{method}\t{mtype}\n"
		f.write(out)

f.close()
