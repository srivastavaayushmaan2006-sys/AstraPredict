# 🚀 AstraPredict

> **AI-powered rocket launch prediction platform built with Machine Learning, FastAPI, and Streamlit.**

AstraPredict combines historical rocket launch data with a machine learning model to estimate the probability of launch success while providing live launch tracking and interactive analytics through a modern dashboard.

---

## 🌟 Features

- 🚀 Live rocket launch tracking
- 🤖 AI-powered launch success prediction
- 📊 Interactive analytics dashboard
- 🌍 Launch site map visualization
- ⏳ Real-time launch countdown
- 🛰 Historical launch explorer
- 📈 Provider and rocket performance insights
- 🧪 Machine Learning Model Lab
- ⚡ FastAPI REST API
- 📉 Model evaluation metrics

---

# 📸 Screenshots

> *(Replace these with your own screenshots once you've taken them.)*

## Mission Control

![Mission Control](assets/mission_control.png)

---

## Launch Explorer

![Launch Explorer](assets/launch_explorer.png)

---

## Analytics Dashboard

![Analytics](assets/analytics.png)

---

## Model Lab

![Model Lab](assets/model_lab.png)

---

# 🏗 System Architecture

```
                     Launch Library 2 API
                              │
                              ▼
                      FastAPI Backend
                ┌────────────────────────┐
                │   /next-launch         │
                │   /predict             │
                │   /health              │
                └────────────────────────┘
                              │
                              ▼
                   Logistic Regression Model
                              │
                              ▼
                  Streamlit Dashboard
        ┌────────────────────────────────────┐
        │ Mission Control                    │
        │ Launch Explorer                    │
        │ Analytics                          │
        │ Model Lab                          │
        └────────────────────────────────────┘
```

---

# 🤖 Machine Learning Pipeline

```
Historical Launch Data
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Categorical Encoding
        │
        ▼
Train/Test Split
        │
        ▼
Logistic Regression
        │
        ▼
Probability Prediction
        │
        ▼
FastAPI Prediction Endpoint
        │
        ▼
Streamlit Dashboard
```

---

# 📊 Model Performance

The current production model uses **Logistic Regression**.

Metrics generated during training include:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- ROC Curve
- Classification Report

These are automatically generated inside the `models/` directory.

---



# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/srivastavaayushmaan2006-sys/AstraPredict.git

cd AstraPredict
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Train the Machine Learning Model

```bash
python src/train_model.py
```

---

# 🌐 Run the FastAPI Backend

```bash
uvicorn api.app:app --reload
```

API Documentation

```
http://127.0.0.1:8000/docs
```

---

# 📊 Run the Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 🔌 API Endpoints

## Get Next Launch

```
GET /next-launch
```

Returns information about the next scheduled rocket launch.

---

## Predict Launch Success

```
POST /predict
```

Returns

- Success probability
- Predicted outcome

---

## Health Check

```
GET /health
```

Returns API status.

---

# 🛠 Tech Stack

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy

### Backend

- FastAPI
- Uvicorn

### Frontend

- Streamlit
- Plotly

### Data

- Launch Library 2 API

### Development

- Python
- Git
- GitHub

---

# 📈 Future Improvements

- Random Forest Model
- Gradient Boosting
- XGBoost
- SHAP Explainability
- Docker Deployment
- Cloud Deployment
- CI/CD Pipeline

---

# 👨‍💻 Author

**Ayushmaan Srivastava**

GitHub

https://github.com/srivastavaayushmaan2006-sys

---

# ⭐ Support

If you found this project interesting, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.

---

## License

This project is licensed under the MIT License.