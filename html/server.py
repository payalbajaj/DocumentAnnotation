from bottle import route, run, request, response
import json
import urllib
import argparse

@route ('/saveBox', method='POST')
def saveBox():
	response.content_type = 'application/json'
	body = request.body.read()
	parsedBody = urllib.unquote(body).decode('utf8')
	f = open(args.filename, "a")
	f.write(parsedBody[:-1]+"\n")
	f.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="""Script to annotate bounding boxes from PDF files. Use --filename to specify where to save the annotations.""")
	parser.add_argument('--filename', type=str, default='new_annotations')
	args = parser.parse_args()
	run(host='0.0.0.0', port=8080)