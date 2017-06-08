@app.route('/flask/api/v1.0/tasks', methods=['GET'])
def get_tasks():
	try:
		var temp = "model return value : format TBD"
		return jsonify(temp)
	except Exception,e:
		print e
		return '{}'

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'})
