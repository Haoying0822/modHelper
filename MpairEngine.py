from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from BinaryTree import BinaryTree

Base = declarative_base()
communications = {}

in_module_users = 0
out_module_users = 0

class MUser(Base): #module mate
    __tablename__ = "MUser"

    id = Column(Integer, primary_key = True)
    module = Column(String, nullable = False)
    username = Column(String, nullable=False)
    like = Column(Boolean, nullable=False)
    status = Column(Integer, nullable=False)

class Contact(Base):
    __tablename__ = "Contact"

    userID = Column(Integer, primary_key=True)
    userToID = Column(Integer, nullable=False)

module_users = BinaryTree()


engine = create_engine("sqlite:///Module_Data.db")
Base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)

def add_module_users(chat, mod):
    global module_users
    global in_module_users
    global out_module_users
    user_id = chat.id
    user_name = chat.username

    if user_id in module_users:
        return
   
    if in_module_users >= out_module_users:
        module_users[user_id] = {"state": 0, "ID": user_id, "Username": user_name, "Module": mod}
        out_module_users = out_module_users + 1
    elif in_module_users < out_module_users:
        module_users[user_id] = {"state": 1, "ID": user_id, "Username": user_name, "Module": mod}
        in_module_users = in_module_users + 1

    s = session()
    if len(s.query(MUser).filter(MUser.id == user_id).all()) > 0:
        s.query(MUser).filter(MUser.id == user_id).update({"status": 0})

        s.commit()
        s.close()
        return
    
    s.add(MUser(id = user_id, module = mod, username = chat.username, like = False, status = 0))
    s.commit()
    s.close()

def find_module_user(mod):
    s = session()
    if len(s.query(MUser).filter(MUser.module == mod).all()) > 1:
        s.commit()
        s.close()
        return True
    else:
        s.commit()
        s.close()
        return False

def delete_Muser_from_db(user_id):
    if user_id in module_users:
        module_users.delete(user_id)

    s = session()

    s.query(MUser).filter(MUser.id == user_id).delete()

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

    s.query(MUser).filter(MUser.id == user_id).update({"status": 3, "like": False})
    s.query(MUser).filter(MUser.id == tmp_id).update({"status": 3, "like": False})

    s.commit()
    s.close()


def add_communications(user_id, user_to_id):
    global module_users

    communications[user_id] = {
        "UserTo": user_to_id,
        "Username": module_users[user_to_id]["Username"],
        "like": False,
    }
    communications[user_to_id] = {
        "UserTo": user_id,
        "Username": module_users[user_id]["Username"],
        "like": False,
    }

    print(communications[user_id], " ", communications[user_to_id])

    module_users.delete(user_id)
    module_users.delete(user_to_id)

    s = session()

    s.query(MUser).filter(MUser.id == user_id).update({"status": 1})
    s.query(MUser).filter(MUser.id == user_to_id).update({"status": 1})

    s.add(Contact(userID=user_id, userToID=user_to_id))

    s.commit()
    s.close()


def recovery_data():
    global communications
    s = session()

    for i in s.query(Contact).all():
        first = s.query(MUser).filter(MUser.id == i.userID).first()
        second = s.query(MUser).filter(MUser.id == i.userToID).first()

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

    for i in s.query(MUser).filter(MUser.status == 0).all():
        add_module_users(user_chat_id=i.id, username=i.username)

    s.close()


def update_user_like(user_id):
    communications[user_id]["like"] = True

    s = session()
    s.query(MUser).filter(MUser.id == user_id).update({"like": True})
    s.commit()
    s.close()
