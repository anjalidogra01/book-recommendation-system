# 📚 Book Recommendation System

A web-based Book Recommendation System built with Flask and Machine Learning that suggests books based on popularity and collaborative filtering.

---

## 🌟 Features

- **Popularity-Based Recommendations** — Shows top 50 most popular books on the homepage based on ratings and vote count
- **Collaborative Filtering** — Recommends 5 similar books based on user input using cosine similarity
- **Interactive Web UI** — Clean and responsive interface built with HTML/CSS/Bootstrap

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **ML Libraries:** NumPy, Pandas, Scikit-learn
- **Frontend:** HTML, CSS, Bootstrap, Jinja2
- **Model Serialization:** Pickle

---

## 📁 Project Structure

```
book-recommendation-system/
│
├── dataset/
│   ├── Books.csv               # Book metadata
│   ├── books_data.csv          # Processed book data
│   ├── Ratings.csv             # User ratings
│   ├── Users.csv               # User data
│   └── Books_rating.csv        # ⚠️ Not included (too large - see Dataset section)
│
├── model/
│   ├── books.pkl               # Processed books dataframe
│   ├── most_popular_books.pkl  # Top 50 popular books
│   ├── pt.pkl                  # Pivot table (user-book matrix)
│   ├── similarity_scores.pkl   # Cosine similarity matrix
│   └── requirements.txt        # Python dependencies
│
├── templates/
│   ├── index.html              # Homepage (popular books)
│   ├── book_recommendor.html   # Recommendation page
│   └── navbar.html             # Navigation bar
│
├── app.py                      # Flask application
├── model.zip                   # Compressed model files
├── .gitignore
└── README.md
```

---

## 📊 Dataset

This project uses two datasets:

### 1. Book Recommendation Dataset (Kaggle)
> Contains Books, Users, and Ratings data

👉 [Download from Kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)

Files needed:
- `Books.csv`
- `Ratings.csv`
- `Users.csv`

### 2. Amazon Books Dataset
> Contains additional book metadata and reviews (`Books_rating.csv`)

👉 Search for **"Amazon Books Reviews"** on Kaggle or Google Dataset Search

> ⚠️ **Note:** `Books_rating.csv` is ~2.7GB and is NOT included in this repo. Download it separately and place it in the `dataset/` folder.

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/anjalidogra01/book-recommendation-system.git
cd book-recommendation-system
```

**2. Create a virtual environment**
```bash
python -m venv venv
```

**3. Activate virtual environment**

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

**4. Install dependencies**
```bash
pip install -r model/requirements.txt
```

**5. Download the datasets** (see Dataset section above) and place them in the `dataset/` folder

---

## 🚀 How to Run

```bash
python app.py
```

Open your browser and go to:
```
http://127.0.0.1:5000
```

---

## 🤖 How It Works

### Popularity-Based Filtering
- Filters books with at least 250 ratings
- Calculates average rating and vote count
- Displays top 50 most popular books on the homepage

### Collaborative Filtering
- Creates a User-Book pivot table
- Computes cosine similarity between books
- Given a book title, returns top 5 most similar books

---

## 📌 Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Homepage — shows popular books |
| `/book_recommendor` | GET | Recommendation input page |
| `/book_recommendations` | POST | Returns 5 recommended books |

---

## 🙋‍♀️ Author

**Anjali Dogra**
- GitHub: [@anjalidogra01](https://github.com/anjalidogra01)
- Email: anjalidogra1806@gmail.com

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!
