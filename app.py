from flask import Flask, render_template, request
import pickle

import numpy as np

# Load pickle file
most_popular_df = pickle.load(open('model/most_popular_books.pkl', 'rb'))
pt = pickle.load(open('model/pt.pkl','rb'))
books = pickle.load(open('model/books.pkl','rb'))
similarity_scores = pickle.load(open('model/similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(most_popular_df['Book-Title'].values),
        authors=list(most_popular_df['Book-Author'].values),
        image=list(most_popular_df['Image-URL-M'].values),
        votes=list(most_popular_df['rating_count'].values),
        rating = list(most_popular_df['avg_rating'].values),)

@app.route('/book_recommendor')
def book_recommendor_ui():
    print(type(similarity_scores))

    return render_template('book_recommendor.html')

@app.route('/book_recommendations', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    if user_input not in pt.index:
        return render_template('book_recommendor.html', 
                               error="Book not found in our database 😢")

    index = np.where(pt.index == user_input)[0][0]

    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    data = []

    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    return render_template('book_recommendor.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
