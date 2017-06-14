import model
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Router for prediction using model developed off full featureset
# Pros: Better at generalizing
# Cons: Subject to high bias internal to data
@app.route('/predict_full', methods=['POST'])
def full_model_handler():
    if request.method == 'POST':
        # Print JSON data
        input_data = request.get_json(force=True)
        # Read the test key from received JSON
        print input_data['test']
        # JSON to Index or pd.df
        new_patient = model.df_transform(input_data)
        # Run model on input data here
        prediction = model.full_predict(new_patient)
        data = {    'LOS > 3': prediction
                    'confidence_score': score
                    }
        return jsonify(data)

        except Exception, e:
            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print 'train first'
        return 'no model here'

# Router for prediction using model developed off sparse featureset
# Pros: Incorporates additional features with high skew variance
# Cons: Subject to overestimating impact of low-occurence features
@app.route('/predict_sparse', methods=['POST'])
def sparse_model_handler():
    if request.method == 'POST':
        # Print JSON data
        input_data = request.get_json(force=True)
        # Read the test key from received JSON
        print input_data['test']
        # JSON to Index or pd.df
        new_patient = model.df_transform(input_data)
        # Run model on input data here
        prediction = model.sparse_predict(new_patient)
        data = { 'LOS > 3': prediction}
        return jsonify(data)

        except Exception, e:

            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print 'train first'
        return 'no model here'

# Router for prediction using hybrid model
# Pros: Tries to work in trade-off between sparse and full model predictions
# Cons: Trying to do both may lead to being good at neither
@app.route('/predict_hybrid', methods=['POST'])
def hybrid_model_handler():
    if request.method == 'POST':
        # Print JSON data
        input_data = request.get_json(force=True)
        # Read the test key from received JSON
        print input_data['test']
        # JSON to Index or pd.df
        new_patient = model.df_transform(input_data)
        # Run model on input data here
        prediction = model.hybrid_predict(new_patient)
        data = { 'LOS > 3': prediction}
        return jsonify(data)

        except Exception, e:

            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print 'train first'
        return 'no model here'

# Router for prediction using neural network
# Pros: Will likely outperform other models at high data throughput
# Cons: Unlikely that sufficient high throughput will occur
@app.route('/predict_nn', methods=['POST'])
def full_model_handler():
    if request.method == 'POST':
        # Print JSON data
        input_data = request.get_json(force=True)
        # Read the test key from received JSON
        print input_data['test']
        # JSON to Index or pd.df
        new_patient = model.df_transform(input_data)
        # Run model on input data here
        prediction = model.predict_nn(new_patient)
        data = { 'LOS > 3': prediction}
        return jsonify(data)

        except Exception, e:

            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print 'train first'
        return 'no model here'
# Router for prediction using neural network
# Pros: Will likely outperform other models at high data throughput
# Cons: Unlikely that sufficient high throughput will occur
@app.route('/predict_best_model', methods=['POST'])
def best_model_handler():
    if request.method == 'POST':
        # Print JSON data
        input_data = request.get_json(force=True)
        # Read the test key from received JSON
        print input_data['test']
        # JSON to Index or pd.df
        new_patient = model.df_transform(input_data)
        # Run model on input data here
        prediction = model.predict_nn(new_patient)
        data = { 'LOS > 3': prediction}
        return jsonify(data)

        except Exception, e:

            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print 'train first'
        return 'no model here'

# Router for command to retrain a given model
# Expects JSON with:
# { model_to_retrain: "", data:"" }
# retrains selected model with provided dataset
@app.route('/retrain', methods=['POST'])
def retrain(model,data):

    model.df_transform(data)

    if(model == "full"):
        model.generate_full_model(data)

    else if(model == "sparse"):
        model.generate_sparse_model(data)

    else if(model == "hybrid"):
        model.generate_hybrid_model(data)

    else if(model == "nn"):
        model.generate_nn(data)

    else:
        print 'please make sure selection was a serviceable model'
        return 'error in model retraining'


@app.route('/create_best_model', methods=['POST'])
def best_model(data,perf_metrics):
    data = model.df_transform(data)
    model.create_best_model(data,perf_metrics)

# Runner function
if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception, e:
        port = 80

    try:
        clf = joblib.load(model_file_name)
        print 'model loaded'
        model_columns = joblib.load(model_columns_file_name)
        print 'model columns loaded'

    except Exception, e:
        print 'No model here'
        print 'Train first'
        print str(e)
        clf = None

    app.run(host='0.0.0.0', port=port, debug=True)
