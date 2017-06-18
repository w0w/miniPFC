import requests
import json


def bulkStore(docs):
	json_data = json.dumps({"docs":docs})
	print json_data
	print type(json_data)
	headers = {'content-type': 'application/json'}
	r = requests.post('http://localhost:5984/test/_bulk_docs', data = json_data, headers=headers)
	print r.json()

