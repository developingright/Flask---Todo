from flask import Blueprint, render_template , request  ,redirect,url_for,jsonify
from flask.helpers import flash
from flask_login import login_required , current_user
from sites.auth import login
from .models import Task,User
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
            new_task = Task(title=title)
            current_user.tasks.append(new_task)
            db.session.add(new_task)
            db.session.commit()
    return render_template("index.html",user = current_user)


@views.route('/update/<int:id>',methods= ['POST','GET'])
@login_required
def update(id):
    users = User.query.all()
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
        collaborate = request.form.get("collaborate")
  
        flag = False
        for i in task.users:
            if i.email == collaborate:
                flag = True
                print("the email was found")
                break
        print(flag)
        if flag == False:
            for x in users:
                f = x.email
                print("collaborate and user  is ",collaborate,f)
                if f==collaborate:
                    m = User.query.get(x.id)
                    task.users.append(m)
                else:
                    print("no result found")
        
        db.session.commit()

    if task.users.count()>1:
        return redirect('/collaboration')
    else:
        return redirect('/')

@views.route('/delete/<int:id>')
@login_required
def delete_note(id):
    task = Task.query.get(id)
    print(id)
    for user in task.users:
      
        user.tasks.remove(task)
        db.session.commit()
    return redirect('/')

@views.route('/collaboration/')
@login_required
def collab_task():

    return render_template("collab.html",user = current_user)

@views.route('/collaborate/<int:id>', methods=['GET', 'POST'])
def taskusers(id):
    task = Task.query.get(id)
    # GET request
    l = []
    if request.method == 'GET':
        for users in task.users:
            l.append(users.email)

        print(l)
        return jsonify(l)  # serialize and use JSON headers
 