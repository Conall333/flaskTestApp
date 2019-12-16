from flask import Flask, render_template

# create an instance of a flask app
app = Flask(__name__)




@app.route("/")
def home():
    return render_template('index.html')

# use variable rules to write one function for server a requested page
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/<username>/<int:post_id>')
def username(username=None,post_id=None):
    return render_template('index.html', name=username,post_id = post_id)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return 'form submitted'