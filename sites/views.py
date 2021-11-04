from flask import Blueprint, render_template , request,jsonify,redirect,url_for
from flask.helpers import flash
from flask_login import login_required , current_user
from sites.auth import login
from .models import Task
import json
from . import db
views = Blueprint('views',__name__)

@views.route('/',methods = ['GET','POST'])
@login_required
def index():
    if request.method == "POST":
        title = request.form.get("title")
        print(title)
        if len(title)<4:
            flash("The title is too short! ",category="error")
        else:
            new_task = Task(title=title,user_id=current_user.id)
            db.session.add(new_task)
            db.session.commit()
    return render_template("index.html",user = current_user)


@views.route('/update/<int:id>',methods= ['POST','GET'])
@login_required
def update(id):
    task  = Task.query.get(id)
    if request.method=="POST":
        title = request.form.get("title")
        task.title = title 
        completed = request.form.get("check")
        task.title = title 
        if completed == 'on':
            task.completed = True
        else:
            task.completed = False
        db.session.commit()
    return redirect('/')

@views.route('/delete-task',methods = ['POST'])
@login_required
def delete_note():
    task = json.loads(request.data)
    taskId = task['taskId']
    task = Task.query.get(taskId)
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()
    return jsonify({})