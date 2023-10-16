def predict():
    import numpy as np
    import requests
    import json
    import pandas as pd
    import random

    X_test = pd.read_csv("src/X_test.csv")
    Y_test = pd.read_csv("src/Y_test.csv")

    random_indexes = np.random.choice(X_test.index, size=100, replace=False)
    X_test = X_test.loc[random_indexes]
    Y_test = Y_test.loc[random_indexes]

    # X_test = X_test[:50]
    # Y_test = Y_test[:50]

    del X_test["Unnamed: 0"]
    del Y_test["Unnamed: 0"]
    
    # Define url and headers
    # url = 'http://localhost:5006/predict'
    # url = 'http://localhost:5000/predict'
    url = "http://52.66.238.144/predict"

    y_pred = []
    
    # url = 'https://13.127.227.174:5006/predict'
    headers = {
        'Content-type': "application/json"
    }

    cols = list(X_test.columns)
    for i in range(len(X_test)):

        dic = {}

        # print(list(X_test.iloc[i]))

        i = 0
        for v in list(X_test.iloc[i]):
            dic[cols[i]] = v
            i += 1

        # print(dic)
            

    # Package data as JSON to pass in POST HTTP request.
        data = json.dumps(dic)
        # print("Request sending")
        response = requests.post(url, headers=headers, data=data)
        # print("Request sent")
        # Parse response as JSON and return predictions
        predictions = np.array(json.loads(response.text))
        # print(predictions)
        y_pred.append(predictions[0])

    y_test = list(Y_test["Class"])
    tot_match = 0
    for i in range(len(y_pred)):
        if y_pred[i] == y_test[i]:
            tot_match += 1

    # print()
    print("Accuracy = ", tot_match/len(y_pred))

if __name__ == '__main__':
    predict()