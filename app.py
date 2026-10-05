from flask import Flask, render_template , request , jsonify

app = Flask(__name__)
books = [
    {"id": 1, "title": "Data Pipelines with Python", "price": 120},
    {"id": 2, "title": "SQL for Smarties", "price": 90},
    {"id": 3, "title": "Designing Data-Intensive Applications", "price": 200},
    {"id": 4, "title": "Learning Flask", "price": 75}
]
@app.route('/')
def HELLO():
    return 'Server is running'

@app.route('/books')
def get_books():
    min_price = request.args.get('min_price', type=float)
    
    if min_price is None:
        return jsonify(books)
        
    filtered_books = [book for book in books if book['price'] >= min_price]
    return jsonify(filtered_books)

@app.route('/books/<int:book_id>')
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        return jsonify({'error': 'Book not found'})
    return jsonify(book[0])


if __name__ == '__main__':
    app.run(debug=True)