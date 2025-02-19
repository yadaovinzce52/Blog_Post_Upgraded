import requests
from flask import Flask, render_template

app = Flask(__name__)

blog_url = 'https://api.npoint.io/48ad364697c49e97590d'
response = requests.get(url=blog_url)
all_posts = response.json()

@app.route("/")
def go_home():
    return render_template('index.html', posts=all_posts)


@app.route("/about")
def go_about():
    return render_template('about.html')


@app.route("/contact")
def go_contact():
    return render_template('contact.html')

@app.route("/blog/<int:num>")
def get_blog(num):
    requested_post = None
    for post in all_posts:
        if post['id'] == num:
            requested_post = post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
