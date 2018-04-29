#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import requests
import json




def precire(documenttext):
	headers = {
		'Ocp-Apim-Subscription-Key': '63b604a62acb4f11a11b675e8ef312c7',
		'Content-Type': 'application/json',
		'Content-Language': 'de',
	}
	body = {
		'document': {
			'text': (documenttext),
			'type': 'default',
		},
		'results': ["activating", "ambitious", "appreciative", "approving", "attentive", "authoritative", "autonomous", "balanced", "committed", "emotional", "evaluative", "exaggerating", "friendly", "goal_oriented", "informative", "intellectual", "open_minded", "optimistic", "personal", "positive", "pragmatic", "responsibly", "self_disclosing", "sociable", "structured", "supportive", "visionary"],
		'patterns': True,
	}
	response = requests.post('https://api.precire.ai/v0.9/',
							json=body,
							headers=headers)
	assert response.status_code == 200
	print(response.json())
	print('fooooooobar /n/n/n')
	print(parseprecire(response.json()))

def parseprecire(injson):
	data = injson
	outdata = []
	for date in data['results']:
		#print(date)
		#print(data['results'][date]['score'])
		outdata.append({'marker': date, 'score': data['results'][date]['score']})
		#outdata.append(date = date['score'])
	outjson = json.dumps(outdata)
	return(outjson)


if __name__ == "__main__":
	precire('dies ist ein mega langer demo text um mal precire darauf zu testen, was wir so für Ergebnisse erhalten')
