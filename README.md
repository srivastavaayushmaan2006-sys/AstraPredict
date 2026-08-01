# 🚀 AstraPredict

<p align="center">

<img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit">
<img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi">
<img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?style=for-the-badge">

</p>

> **An end-to-end Machine Learning platform for analyzing historical rocket launches and predicting launch success.**

AstraPredict combines historical launch records, machine learning, FastAPI, and Streamlit into an interactive analytics platform for exploring space missions and estimating launch success probabilities.

---

# 📸 Dashboard
https://astrapredict-ck94jmzyxihyxb57xjndg2.streamlit.app/

---

# ✨ Features

- 🚀 Explore **4,196 historical rocket launches**
- 🤖 Predict launch success using Machine Learning
- 📊 Interactive analytics dashboard
- 🌍 Launch Explorer with advanced filters
- 🛰 Mission Control
- ⚔️ Provider Comparison
- 🧪 Model Lab
- 📈 Historical Intelligence
- ⚡ FastAPI REST API
- 📉 Model evaluation metrics
- 📥 Download filtered launch data

---

# 📊 Dataset

AstraPredict uses a cleaned historical launch dataset containing:

- **4,196 launches**
- **55 launch providers**
- **341 rocket variants**
- **8 mission categories**
- Historical launch records dating back to the beginning of the Space Age

---

# 🏗 Architecture

```
Historical Launch Dataset
          │
          ▼
Data Preprocessing
          │
          ▼
Feature Engineering
          │
          ▼
Machine Learning Model
(Logistic Regression)
          │
          ▼
FastAPI Backend
          │
          ▼
Streamlit Dashboard
```

---

# 🤖 Machine Learning

Current Production Model

- Logistic Regression

Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- Classification Report
- ROC Curve

---

# 📁 Project Structure

```text
AstraPredict/
│
├── api/
├── dashboard/
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── src/
├── requirements.txt
├── LICENSE
└── README.md
```

---

# ⚙️ Installation

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

# 🚀 Train the Model

```bash
python -m src.train_model
```

---

# 🌐 Start the FastAPI Server

```bash
uvicorn api.app:app --reload
```

Swagger Documentation

```
https://astrapredict-1.onrender.com/docs
```

---

# 📊 Run the Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 🛠 Tech Stack

### Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Joblib

### Backend

- FastAPI
- Uvicorn

### Frontend

- Streamlit
- Plotly

### Data Engineering

- Pandas
- Custom preprocessing pipeline

### Development

- Python
- Git
- GitHub


---

# 👨‍💻 Author

**Ayushmaan Srivastava**

GitHub

https://github.com/srivastavaayushmaan2006-sys

---

# 📄 License

This project is licensed under the MIT License.

---

⭐ If you found AstraPredict interesting, consider starring the repository.