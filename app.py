import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'task_manager'
app.config['MONGO_URI'] = 'mongodb+srv://daniel:r00tUser@myfirstcluster-ggk14.mongodb.net/task_manager?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template('tasks.html', tasks=mongo.db.tasks.find())

@app.route('/add_task')
def add_task():
    return render_template('addtask.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
                                port=int(os.environ.get('PORT')),
                                debug=True)
