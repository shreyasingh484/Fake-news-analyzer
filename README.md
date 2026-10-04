# 📰 Fake News Detection using Machine Learning

A machine learning-based application that detects whether a news article is **Fake** or **Real** using Natural Language Processing (NLP) and Logistic Regression.

## 📌 Project Overview

The Fake News Detection system analyzes the **title and content of a news article** and predicts whether the news is:

* 🔴 **Fake News**
* 🟢 **Real News**

The project uses **TF-IDF (Term Frequency-Inverse Document Frequency)** for converting text into numerical features and **Logistic Regression** for classification.

## 🚀 Features

* Detects fake and real news
* Uses Natural Language Processing
* TF-IDF text vectorization
* Logistic Regression machine learning model
* Simple graphical user interface
* Easy to use and run locally

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**
* **Requests**
* **Tkinter**
* **TF-IDF**
* **Logistic Regression**

## 📂 Project Structure

```text
Fake-News-Detection/
│
├── fake_news.py
├── Fake.csv
├── True.csv
└── README.md
```

> **Note:** The dataset files `Fake.csv` and `True.csv` are not included in this repository because of their large file size.

## 📊 Dataset

The project requires two CSV files:

* `Fake.csv` — Fake news articles
* `True.csv` — Real news articles

Download/obtain the datasets and place them in the same folder as `fake_news.py`.

The program expects the following filenames:

```text
Fake.csv
True.csv
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Fake-News-Detection.git
```

### 2. Open the project folder

```bash
cd Fake-News-Detection
```

### 3. Install required libraries

```bash
pip install pandas requests scikit-learn
```

### 4. Add the datasets

Place:

```text
Fake.csv
True.csv
```

inside the project folder.

### 5. Run the project

```bash
python fake_news.py
```

## 🔍 How It Works

The system follows these steps:

```text
News Article
     ↓
Text Preprocessing
     ↓
TF-IDF Vectorization
     ↓
Logistic Regression
     ↓
Prediction
     ↓
Fake / Real
```

### Machine Learning Algorithm

**Logistic Regression** is used as the classification algorithm.

TF-IDF converts the news text into numerical features that the machine learning model can understand.

## 💡 Future Improvements

* Add more machine learning algorithms
* Improve prediction accuracy
* Add deep learning models
* Add a web-based interface
* Add URL-based news analysis
* Add multilingual fake news detection
* Deploy the application online

## 👩‍💻 Author

**Shreya Khagta**

BTech Student

## ⭐ Project Purpose

This project was developed as a **BTech major project** to demonstrate practical knowledge of:

* Machine Learning
* Natural Language Processing
* Python
* Data Processing
* Text Classification
* GUI Development
