git clone https://github.com/Hult-CM3/hultagram.git

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)
    

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        content = request.form['content']
        new_post = Post(content=content)
        image_file = db.Column(db.String(100), nullable=False)
        like_count = db.Column(db.Integer, default=0)

print(f"File received: {file.filename}, allowed: {allowed_file(file.filename)}")
with app.app_context():
    posts = Post.query.all()
    for post in posts:
        print(f"Post {post.id}: {post.caption}, Likes: {post.likes}, Comments: {len(post.comments)}")

if __name__ == '__main__':
    app.run(debug=True)