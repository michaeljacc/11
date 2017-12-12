import time

from . import ModelMixin
from . import db


class Blog(db.Model, ModelMixin):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    created_time = db.Column(db.Integer)
    updated_time = db.Column(db.Integer)
    # 这是一个外键
    # user_id = db.Column(db.Integer, db.ForeignKey('stb_users.id'))
    # # relationship
    # reviews = db.relationship('Review', backref='chest')

    def __init__(self, form):
        print('chest init', form)
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.created_time = int(time.time())

    def update(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.save()
