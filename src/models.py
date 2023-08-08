import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'   
    ID = Column(Integer, primary_key=True)
    userName = Column(String(50))
    firstName = Column(String(50))
    lastName = Column(String(50))
    email = Column(String(50), unique=True)
    
class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.ID'))


class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key=True)
    type= Column(Enum)
    url = Column(String(70))
    post_id = Column(Integer, ForeignKey('post.ID'))
    
class Comment(Base):
    __tablename__= 'comment'  
    ID =  Column(Integer, primary_key=True)
    comment_text = Column(String(150))
    author_id = Column(Integer, ForeignKey('user.ID'))
    post_id = Column(Integer, ForeignKey('post.ID'))
    
    
class Follower(Base):
    __tablename__ = 'follower'  
    user_from_id = Column(Integer, ForeignKey('user.ID'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.ID'))
    


    
    






    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
