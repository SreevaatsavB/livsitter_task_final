# MLOPs Task
This is a simple MLOPS pipeline for detecting the credit card fraudlant cases. Dataset link :- https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023

Due to storage limitations in github, the training was done on a part of the data.

### Directory Structure :- 
1. **data** :- This directory contains the data required to model the data

2. **models** :- Contains the models (in pickle files) trained and the scalar.

3. **notebooks** :- Contains the analysis done in jupyter notebooks

4. **src** :- The source code for the application to run
    - **app.py**:- The python script which returns the prediction for a data sample provided. Preprocessing and the prediction is done and the the output is returned in JSON format. We use port 5000 for this purpose.

    - **get_preds.py**:- This python script is used in the unit testing phase of the cycle. Will be executed whenever there is a commit to the repository.

    - **X_test.csv / Y_test.csv** :- Testing data for the unit testing.


5. **Dockerfile**:- This is the docker file which is used to create an image. 

6. **requirements.txt**:-  Contains all the dependancies for the application to run. 

7. **requirements_unittest.txt**:-  Contains all the dependancies for the unit test to run in the GitHub container. 

8. **predictions_log.txt**:- The latest accuracy of the model is logged into this file.

8. **.github/workflows**:- This directory is used for the CI-CD of this project, **actions.yml** is the YAML file containing the rules and structure to perform automated testing.


### Docker Containerization

The image for this app wa sbuild and then tagged and pushed to the dockerhub. Lateron, it was run in the EC2 instance to provide an end point.

- **Docker image from the hub** :- vaatsav6/mlops_taskf

##### NOTE:-
The docker image was developed in the intial stages of the project, thus contains less files tha the ones present now







### ML_Model Endpoint (Cloud Deployment)
The trained ML model is deployed in a flask application on the AWS EC2 instance within a docker container.

#### The process goes as follows:- 
1. Create an AWS EC2 instace and allow traffic to connect on http protocol.
(Chosen host OS:- Amazon Linux)

2. Now, using ssh, login into the newly formed instance and install docker in the host and then pull the docker image from the hub.

3. Run the image with this command:- **docker run -d -p 80:5000 vaatsav6/mlops_taskf** 
    Which maps the containe's 5000 port to the EC2 machine's 80 port.



**Endpoint URL :- http://52.66.238.144**
This is the entrypoint of the application, 
**http://52.66.238.144/predict** is the endpoint for getting the JSON reponse from the EC2 instance.

This endpoint is used in the unit testing phase.



### Automated testing 

The automated testing is performed whenever there is a commit made on the repository. 

This is done using the GitLab CI as mentioned above. The **actions.yml** contains the set of actions to set up the github containers, install dependanices and executing the unit tests. 

**The accuracy of the model is logged to predictions_log.txt after every commit**


##### NOTE:- 
1. The read/write permissions should be given for the actions in the repository settings. 

2. Every time during the unit test, 100 random samples will be evaluated. 





