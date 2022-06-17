from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from Option import *
from BinaryTree import BinaryTree

Base = declarative_base()
bot_users = BinaryTree()
communications = {}

in_users = [0] * 10000
out_users = [0] * 10000

class User(Base): #module mate
    __tablename__ = "User"

    id = Column(Integer, primary_key = True)
    option = Column(String, nullable = False)
    username = Column(String, nullable=False)
    like = Column(Boolean, nullable=False)
    status = Column(Integer, nullable=False)

class Contact(Base):
    __tablename__ = "Contact"

    userID = Column(Integer, primary_key=True)
    userToID = Column(Integer, nullable=False)


engine = create_engine("sqlite:///Data.db")
Base.metadata.create_all(bind = engine)
session = sessionmaker(bind = engine)

def add_users(user_id, user_name, opt):
    global bot_users
    global in_users
    global out_users
    opt_index = option_dict[opt]

    if user_id in bot_users:
        print("alr in list")
        return
   
    if in_users[opt_index] >= out_users[opt_index]:
        bot_users[user_id] = {"state": 0, "ID": user_id, "Username": user_name, "Option": opt}
        out_users[opt_index] = out_users[opt_index] + 1
        print(user_name + " 0 " + opt)
    elif in_users[opt_index] < out_users[opt_index]:
        bot_users[user_id] = {"state": 1, "ID": user_id, "Username": user_name, "Option": opt}
        in_users[opt_index] = in_users[opt_index] + 1
        print(user_name + " 1 " + opt)

    s = session()
    if len(s.query(User).filter(User.id == user_id).all()) > 0:
        s.query(User).filter(User.id == user_id).update({"status": 0, "option": opt})

        s.commit()
        s.close()
        return
    
    s.add(User(id = user_id, option = opt, username = user_name, like = False, status = 0))
    s.commit()
    s.close()

    print("added")

def find_user(opt):
    s = session()
    if len(s.query(User).filter(User.option == opt).all()) > 1:
        s.commit()
        s.close()
        return True
    else:
        s.commit()
        s.close()
        return False

def delete_user_from_db(user_id):
    if user_id in bot_users:
        bot_users.delete(user_id)

    s = session()

    s.query(User).filter(User.id == user_id).delete()

    s.commit()
    s.close()

def delete_info(user_id):
    global communications

    tmp_id = communications[user_id]["UserTo"]

    communications.pop(user_id)
    communications.pop(tmp_id)

    s = session()

    if len(s.query(Contact).filter(Contact.userID == user_id).all()) > 0:
        s.query(Contact).filter(Contact.userID == user_id).delete()
    else:
        s.query(Contact).filter(Contact.userID == tmp_id).delete()
    s.commit()

    s.query(User).filter(User.id == user_id).update({"status": 3, "like": False})
    s.query(User).filter(User.id == tmp_id).update({"status": 3, "like": False})

    s.commit()
    s.close()


def add_communications(user_id, user_to_id):
    global bot_users

    communications[user_id] = {
        "UserTo": user_to_id,
        "Username": bot_users[user_to_id]["Username"],
        "like": False,
    }
    communications[user_to_id] = {
        "UserTo": user_id,
        "Username": bot_users[user_id]["Username"],
        "like": False,
    }

    print(communications[user_id], " ", communications[user_to_id])

    bot_users.delete(user_id)
    bot_users.delete(user_to_id)

    s = session()

    s.query(User).filter(User.id == user_id).update({"status": 1})
    s.query(User).filter(User.id == user_to_id).update({"status": 1})

    s.add(Contact(userID = user_id, userToID = user_to_id))

    s.commit()
    s.close()


def recovery_data():
    global communications
    s = session()

    for i in s.query(Contact).all():
        first = s.query(User).filter(User.id == i.userID).first()
        second = s.query(User).filter(User.id == i.userToID).first()

        communications[i.userID] = {
            "UserTo": second.id,
            "UserName": second.username,
            "like": second.like,
        }
        communications[i.userToID] = {
            "UserTo": first.id,
            "UserName": first.username,
            "like": first.like,
        }

    for i in s.query(User).filter(User.status == 0).all():
        add_users(i.id, i.username, i.option)

    s.close()


def update_user_like(user_id):
    communications[user_id]["like"] = True

    s = session()
    s.query(User).filter(User.id == user_id).update({"like": True})
    s.commit()
    s.close()
