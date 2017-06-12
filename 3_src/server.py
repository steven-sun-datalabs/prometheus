from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Print JSON data
        input_data = request.get_json(force=True)
        # Read the test key from received JSON
        print input_data['test']
        # Run model on input data here
    # Send result back
    data = { 'days_of_stay': 8 }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
