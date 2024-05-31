# Crop Prediction ML Model 

import numpy as np 
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow 
import config
import pickle

def evaluation_metrics(y_test,y_pred):
    acc = accuracy_score(y_test,y_pred)
    return acc

if __name__ == "__main__":

    test_size=config.test_size
    random_state=config.random_state

    
    data = pd.read_csv(config.TRAINING_PATH)
    # data = data['Crop'] = pd.factorize(data['Crop'])[0] + 1
    le=LabelEncoder()

    X = np.array(data.iloc[:, 0:7])
    y = np.array(data.iloc[:, 7:])
    y = le.fit_transform(y)
    
    X_train,X_test, y_train,y_test = train_test_split(X,y,test_size=test_size, random_state=random_state)

    with mlflow.start_run():
        n_estimators = config.n_estimators
        max_depth = config.max_depth
        rf = RandomForestClassifier(n_estimators=n_estimators,max_depth=max_depth)
        rf.fit(X_train,y_train)
        predictions = rf.predict(X_test)

        acc = evaluation_metrics(y_test,predictions)
        print(f"accuracy is {acc}")

        mlflow.log_param("n_estimators",n_estimators) 
        mlflow.log_param("max_depth",max_depth) 
    
        mlflow.log_metric("accuracy score",acc)

        mlflow.sklearn.log_model(rf,"modelrff")
        #mlflow.log_artifact("file.txt")

    with open('C:/Users/91704/Desktop/projects/Classification projects/Crop Prediction/model/modelrff.pkl', 'wb') as f:
        loaded_model = pickle.dump(rf,f)    

       

