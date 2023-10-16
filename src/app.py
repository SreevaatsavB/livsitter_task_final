from flask import Flask, jsonify, request
from pickle import load
import pandas as pd
from flask import Response
import json

#Used to create a Flask web application instance.
app = Flask(__name__)

# Load the above-saved model

# scaler  = load(open('models/standard_scaler.pkl', 'rb'))
# scaler  = load(open('models/standard_scalar.pkl', 'rb'))


# # xgb_model = load(open('models/RC_clf.pkl', 'rb'))
# xgb_model = load(open('models/XGB_clf.pkl', 'rb'))

# RC_clf = load(open('XGB_clf.pkl', 'rb'))
@app.route("/")
def home_endpoint():
    return "This is the end point"

@app.route('/predict', methods=['POST'])
def predict():

    scaler  = load(open('models/standard_scalar.pkl', 'rb'))
    xgb_model = load(open('models/XGB_clf.pkl', 'rb'))

    # Get the input data from the request
    data = request.get_json()

    
    x_test =  []

    for k in data:
        x_test.append(data[k])

    x_test_df = pd.DataFrame(x_test).T
    x_test_df.columns = [k for k in data.keys()]

    data_norm_test = x_test_df.copy()
    data_array_test = scaler.transform(data_norm_test)
    X_test_sc_df = pd.DataFrame(data_array_test,columns = data_norm_test.columns).set_index(data_norm_test.index)


    X_test_sc_df = X_test_sc_df.drop(['V17', 'V18'], axis=1)

    predictions = xgb_model.predict(X_test_sc_df)

    response = json.dumps(predictions.tolist())
    return Response(response, status=200, mimetype="application/json")

    # Return the predictions as JSON response
    # return jsonify({'predictions': predictions.tolist()})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)