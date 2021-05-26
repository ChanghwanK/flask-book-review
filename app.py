from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    title = request.form['title']
    author = request.form['author']
    review = request.form['review']

    print(title, author, review)

    doc = {
        'title': title,
        'author': author,
        'review': review
    }

    db.bookReview.insert_one(doc)

    return jsonify({'msg': '등록 되었습니다.'})


@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.bookReview.find({}, {'_id': False}))
    print(reviews)
    return jsonify({'data': reviews})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
