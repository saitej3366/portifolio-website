from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template("index.html")

# Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        return f"Thanks {name}, your message has been received!"
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
