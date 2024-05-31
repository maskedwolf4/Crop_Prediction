## Crop Prediction ML Model with Flask, Docker, and CI/CD

This repository contains the code for a machine learning model that predicts crop yield based on soil health parameters. This project is designed to be a practical tool for real-world agricultural practices, leveraging the power of machine learning, web deployment, containerization, and continuous integration/delivery.

### Project Overview

This project tackles crop prediction using a Random Forest Classifier, aiming to:

* **Predict Crop Yield:** Estimate suitable crop yield based on soil health data (nitrogen, phosphorus, potassium, temperature, humidity, pH value, rainfall).
* **Real-world Applicability:** Integrate the model with IoT sensors to collect real-time soil data for on-the-fly predictions.
* **Deployment and Scalability:** Deploy the model as a Flask API for easy access and containerize it using Docker for efficient scaling.
* **Continuous Integration and Delivery (CI/CD):** Utilize GitHub Actions to automate testing, building, and deployment, ensuring consistent and reliable updates.
* **Modular Programming:** Organize the code into well-defined folders (data, model, api, config) for maintainability and clarity.

### Model Details

* **Model Type:** Random Forest Classifier
* **Hyperparameters:** Specific hyperparameters optimized for performance are defined in the `config.py` file (**Accuracy: 99.7%**).

### Using the Model in Real-world Agriculture

1. **IoT Sensor Integration:** Integrate IoT sensors that measure soil health parameters (nitrogen, phosphorus, potassium, temperature, humidity, etc.).
2. **Data Collection:** Sensors collect real-time data and transmit it to the system.
3. **API Call:** Send a POST request with the collected data as JSON to the deployed Flask API endpoint.
4. **Prediction Generation:** The API utilizes the trained model to predict the suitable crop yield based on the received data.
5. **Decision Making:** Farmers can leverage the predictions to make informed decisions about crop selection, resource allocation, and potential optimizations.

### Project Structure

This project follows a modular programming approach with separate folders for each functionality:

* `Input data`: Contains data.
* `model`: Saved model in pkl format.
* `CPapp.py`: Implements the Flask API for receiving requests, processing data, and returning predictions.
* `config`: Stores configuration parameters, including hyperparameters, API details, and MLflow tracking information.
* `Notebooks`: Contains all .ipynb files used for data exploration

**Dataset Link:** 

[Kaggle](https://www.kaggle.com/datasets/varshitanalluri/crop-recommendation-dataset)

### MLflow Tracking (Optional)

This project optionally integrates MLflow for tracking model runs, experiments, and parameters. You can leverage MLflow to visualize the model's performance and compare different training runs. Refer to the provided code for specific MLflow configuration and usage.

### Running the Project Locally

**Prerequisites:**

* Python 3.11 with required libraries (specified in `requirements.txt`)
* Docker installed

**Steps:**

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Build the Docker image: `docker build -t crop_prediction .`
4. Run the container (detached mode): `docker run -d -p 5000:5000 crop_prediction`
5. Access the API endpoint: Send a POST request with soil health data as JSON to `http://localhost:5000/predict`
6. The API will respond with the predicted crop yield.

**Note:** This is a basic outline. Refer to the provided code for specific API interaction details.

### Contributing

We welcome contributions to improve this project! Please follow these steps:

1. Fork this repository.
2. Create a new branch for your changes.
3. Make your modifications and commit them with clear messages.
4. Submit a pull request to the "main" branch of this repository.

This README provides a high-level overview. Refer to the code for further details on individual components and functionalities.
