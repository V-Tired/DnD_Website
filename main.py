from flask import Flask, render_template, request


posts_list = []
app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template('index.html')


@app.route("/about")
def get_about():
    return render_template('about.html')


@app.route("/story")
def get_story():
    return render_template('story.html')

@app.route("/contact")
def get_contact():
    return render_template('contact.html')


@app.route("/login", methods=["GET", "POST"])
def receive_data():
    # name = request.form['name']
    # email = request.form['email']
    # phone = request.form['phone']
    # message = request.form['message']
    # if request.method == "POST":
    #     message = f"Name: {name} \nEmail: {email}\nPhone: {phone}\nMessage: \n{message}\n\n"
    #     with open(file='input.txt', mode="a") as file:
    #         file.writelines(message)
    #     print(message)
    return render_template('form-submitted.html')
    # return "Try again", render_template('contact.html')



if __name__ == "__main__":
    app.run(debug=True)
