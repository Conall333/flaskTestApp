from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

# create an instance of a flask app
app = Flask(__name__)


# connect to db
client = MongoClient("mongodb://my_db:27017")
db = client.my_db
collection = db.contact_collection


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
    if request.method == 'POST':
        try:
            #collection.delete_many({})
            data = request.form.to_dict()
            print(data)
            collection.insert(data)
            cursor = collection.find()
            all_docs = ""
            for document in cursor:
                all_docs += " " + str(document)
            return all_docs
            #return redirect(current_docs)
        except UnboundLocalError as err:
            return err
    else:
        return 'try again'



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)