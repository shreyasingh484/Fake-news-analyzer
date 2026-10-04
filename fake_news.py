import random
import pandas as pd
import requests
import tkinter as tk
from tkinter import scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

print("Loading dataset...")

fake = pd.read_csv("Fake.csv")
real = pd.read_csv("True.csv")

fake["Label"] = 0
real["Label"] = 1

df = pd.concat([fake, real])
df = df[["title", "Label"]]
df["title"] = df["title"].str.lower()

print("Training model...")

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["title"])
y = df["Label"]

model = LogisticRegression()
model.fit(X, y)

print("Model trained successfully!")

API_KEY = "c39a3358f75b4290a95ecd146eeb8241"   

def get_live_news():
    output_box.delete(1.0, tk.END)

    print("Live News button clicked")  

    topics = ["india", "technology", "sports", "business", "politics"]
    query = random.choice(topics)

    url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&apiKey={API_KEY}"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        print(data)  

    except Exception as e:
        output_box.insert(tk.END, f"❌ Error fetching news:\n{e}")
        return

    if data.get("status") != "ok":
        output_box.insert(tk.END, f"❌ API Error:\n{data}")
        return

    articles = data.get("articles", [])
    random.shuffle(articles)
    
    if not articles:
        output_box.insert(tk.END, "⚠️ No news articles found.")
        return

    output_box.insert(tk.END, "🔴 Live News Analysis:\n\n")

    for i, article in enumerate(articles[:5]):
        title = article.get("title")

        if not title:
            continue

        transformed = vectorizer.transform([title.lower()])
        prediction = model.predict(transformed)[0]

        result = "🟢 Real News" if prediction == 1 else "🔴 Fake News"

        output_box.insert(tk.END, f"{i+1}. {title}\n")
        output_box.insert(tk.END, f"   Prediction: {result}\n\n")
def check_custom_news():
    output_box.delete(1.0, tk.END)

    user_input = entry.get()

    if user_input.strip() == "":
        output_box.insert(tk.END, "⚠️ Please enter a news headline!")
        return

    transformed = vectorizer.transform([user_input.lower()])
    prediction = model.predict(transformed)[0]

    if prediction == 1:
        result = "🟢 This looks like REAL news."
    else:
        result = "🔴 This looks like FAKE news."

    output_box.insert(tk.END, f"News: {user_input}\n\n{result}")

root = tk.Tk()
root.title("Fake News Detector AI")
root.geometry("650x500")

frame = tk.Frame(root, bg="white")
frame.pack(fill="both", expand=True, padx=10, pady=10)

title = tk.Label(frame, text="Fake News Detector", font=("Arial", 18, "bold"), bg="white")
title.pack(pady=10)

entry = tk.Entry(frame, width=70)
entry.pack(pady=10)

btn_frame = tk.Frame(frame, bg="white")
btn_frame.pack(pady=5)

check_btn = tk.Button(btn_frame, text="Check News", command=check_custom_news, bg="lightblue", width=15)
check_btn.grid(row=0, column=0, padx=10)

live_btn = tk.Button(btn_frame, text="Live News", command=get_live_news, bg="lightgreen", width=15)
live_btn.grid(row=0, column=1, padx=10)

output_box = scrolledtext.ScrolledText(frame, width=75, height=20)
output_box.pack(pady=10)

root.mainloop()