from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

collab = db.Table('collab',
        db.Column('user_id',db.Integer , db.ForeignKey('user.id')),
        db.Column('task_id',db.Integer, db.ForeignKey('task.id')))

class Task(db.Model):
 
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(1000))
    completed = db.Column(db.Boolean, default = False)
    
    # user_id  = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email= db.Column(db.String(150),unique= True)
    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    tasks = db.relationship('Task',secondary=collab,backref=db.backref('users',lazy='dynamic'))
    # tasks = db.relationship('Task')
    