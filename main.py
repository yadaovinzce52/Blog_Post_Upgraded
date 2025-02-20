import smtplib
import requests
from flask import Flask, render_template, request

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


@app.route("/contact", methods=["POST", "GET"])
def go_contact():
    if request.method == "GET":
        return render_template('contact.html', h1_message="Contact Me")
    else:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        my_email = "yadaovinzce@gmail.com"
        my_password = "qzvl xykm rgni afqm"

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=email,
                to_addrs=my_email,
                msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            )

        return render_template('contact.html', h1_message="Successfully sent your message")



@app.route("/blog/<int:num>")
def get_blog(num):
    requested_post = None
    for post in all_posts:
        if post['id'] == num:
            requested_post = post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
