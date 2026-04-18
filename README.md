# Book-Recommendation-System-Association-Rules
A Flask-based Book Recommendation System using Association Rule Mining (Apriori Algorithm) to identify customer buying patterns and improve cross-selling strategies.
# 📚 Book Recommendation System using Association Rules

## 🔍 Problem Statement

Kitabi Duniya, a traditional bookstore, is facing declining sales due to the rise of online platforms.
The goal is to analyze customer purchase patterns and improve sales by **25%** using data-driven strategies.

---

## 🎯 Objective

* Identify frequently bought book combinations
* Generate association rules using Apriori Algorithm
* Improve cross-selling and customer engagement
* Increase store footfall and revenue

---

## 🧠 Approach

This project uses **Association Rule Mining** to discover hidden patterns in customer purchases.

### Steps:

1. Data Preprocessing (Binary dataset of book categories)
2. Frequent Itemset Generation (Apriori Algorithm)
3. Rule Generation (Support, Confidence, Lift)
4. Remove redundant rules
5. Extract top 10 high-value rules

---

## ⚙️ Tech Stack

* Python
* Pandas
* MLxtend (Apriori Algorithm)
* Flask (Web App)
* MySQL (Database)

---

## 📊 Key Concepts

* **Support** → Frequency of itemset
* **Confidence** → Probability of buying Y given X
* **Lift** → Strength of association (>1 means strong rule)

---

## 🚀 Features

* Upload dataset (CSV/Excel)
* Generate association rules automatically
* Store results in MySQL database
* Display results in web interface

---

## 🏗️ Project Structure

```
├── app.py                  # Flask application
├── association_rules.py    # ML logic (Apriori + Rules)
├── book.csv                # Dataset
├── requirements.txt        # Dependencies
```

---

## ▶️ How to Run

### 1. Install Dependencies

```
pip install -r requirements.txt
```

### 2. Set Environment Variables (Optional but Recommended)

```
export DB_USER=root
export DB_PASSWORD=yourpassword
export DB_NAME=ds
```

### 3. Run Application

```
python app.py
```

### 4. Upload Dataset

Use Postman or browser to send file to:

```
http://127.0.0.1:5000/upload
```

---

## 📈 Business Insights

Based on association rules, we can:

* 📦 Bundle related books (e.g., Cooking + Youth Books)
* 🏪 Optimize store layout (place related books together)
* 💡 Recommend books (like Amazon suggestions)
* 🎯 Offer combo discounts

---

## 💼 Business Impact

* Increased cross-selling opportunities
* Better customer experience
* Data-driven decision making
* Target: **25% increase in sales & footfall**

---

## 🔮 Future Improvements

* Add recommendation UI
* Deploy on cloud (AWS/Render)
* Real-time recommendation system
* Add user login & personalization

