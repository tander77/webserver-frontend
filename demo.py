from flask import Flask, render_template, session, url_for, request, jsonify, redirect
import pymongo
from flask_bootstrap import Bootstrap
from forms import NameForm, DeleteForm
import socket
import os

word1 = os.getenv('FIRST_PAGE')
word2 = os.getenv('SECOND_PAGE')

envi = os.getenv('ENVI')


app = Flask(__name__)

bootstrap = Bootstrap(app)

client = pymongo.MongoClient("mongodb://mongo:27017/dev")
db = client["database"]
nameCol = db["names"]

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html', word=word1, envi=envi)

@app.route('/second')
def second():
    return render_template('second.html', word=word2)

@app.route('/names', methods=['GET', 'POST'])
def get_names():
    names = nameCol.find()
    data = []
    for name in names:
        item = {
            "id": str(name["_id"]),
            "name": name["name"]
        }
        data.append(item)
    deleteForm = DeleteForm()
    if deleteForm.validate_on_submit():
        nameCol.delete_many({})
        return redirect(url_for('get_names'))
    return render_template('names.html', names=data, delete=deleteForm)

@app.route('/add_name', methods=["GET", "POST"])
def add_name():
    form = NameForm()
    if form.validate_on_submit():
        nameCol.insert_one({"name" : form.name.data})
        return redirect(url_for('get_names'))
    return render_template('add_name.html', form = form)



if __name__ == '__main__':
    app.run(host='0.0.0.0')