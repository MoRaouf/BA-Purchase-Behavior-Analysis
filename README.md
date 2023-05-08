# British Airways Purchase Behavior Analysis

\>>>>>>>> **Check the application: [Here](https://ba-purchase-analysis.onrender.com/)** <<<<<<<<

🚩 Problem Statement
---
British Airways (BA) is the flag carrier airline of the United Kingdom (UK). Customers who book a flight with BA will experience many interaction points with the BA brand. Understanding a customer's feelings, needs, and feedback is crucial for any business, including BA.

BA wants to understand their customers behavior to act proactively in order to acquire more customers before they embark on their holiday. Therefore, they want to build a predictive model that can help them know if their customers will be purchasing flights through them, & understand the key factors behind their decisions.

🗂️ Dataset
---
For customer sentiment analysis, a web-scarped data from [Skytrax](https://www.airlinequality.com/) is used to analyze customers feedback about the company.
For the predicitve model, the dataset is provided by British Airways. It contains historical customer booking data.

📥 Installation
---
* Clone this repository:
    ```
    git clone https://github.com/MoRaouf/BA-Purchase-Behavior-Analysis.git
    ```
* Set up the virtual environment and all required dependencies by:
  * Setting up a `python=3.8` virtual environment
  * run: `pip install -r requirements.txt`

* Change directory & run Flask app:
    ```
    cd BA-Purchase-Behavior-Analysis
    python app.py
    ```
* Open a web browser and go to http://localhost:5000 to access the application.

* Enter the required input data and click on the "Predicted Booking Status" button to get the predicted booking status for the selected parameters.
    * If the result is 0, then booking will not be submitted.
    * If the result is 1, then booking will succeed.

🔗 Deployment to Render
---
The application was deployed to Render. [Access it here](https://ba-purchase-analysis.onrender.com/).


📁 Project Structure
---

    ├── artifacts          <- Contains different artifacts for model training
    ├── data               <- Datasets used and collected for this project
    ├── logs               <- Logs of the project
    ├── models             <- Serialized trained models
    ├── notebooks          <- Jupyter Notebooks for different steps in the project
    ├── templates          <- Templates folder contains HTML code for the Flask application
    ├── README.md          <- The top-level README for developers/collaborators using this project.
    │   
    ├── src                <- Source code folder for this project
        │   
        └── pipeline       <- Piepline folder for training & prediction pipelines

--------

✳️ Requirements
---
This project used the following libraries:
```
numpy
pandas
matplotlib
seaborn
sklearn
xgboost
catboost
nltk
wordcloud
requests
re
pathlib
pyyaml
```

🫶 Contributing
---
If you would like to contribute to this project, please open an issue or submit a pull request.