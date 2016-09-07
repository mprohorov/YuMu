from app import models
from app import dbconnect

# Take inputs form frontend, write them into the Database
def createAccount(email, phone, fname, lname, pw):
    act = models.account(email = email, phone_number = phone, first_name = fname, last_name = lname, password = pw)
    dbconnect.session.add(act)
    dbconnect.session.commit()

def createEvent(user_id, date, deadline, title):
    event = models.event(user_id=user_id, ymdh=date, deadline=deadline, title=title)
    dbconnect.session.add(event)
    dbconnect.session.commit()
def addFriends(pn1, pn2, pn3):
    friend1 = models.friendsInvited(phone_number=pn1)
    dbconnect.session.add(friend1)
    friend2 = models.friendsInvited(phone_number=pn2)
    dbconnect.session.add(friend2)
    friend3 = models.friendsInvited(phone_number=pn3)
    dbconnect.session.add(friend3)
    dbconnect.session.commit()
def enterPrefs1(lat, long, cat):
    prefs = models.preferences(latitude=lat, longitude=long, category=cat)
    dbconnect.session.add(prefs)
    dbconnect.session.commit()

def enterPrefs2(minb, maxb, startTime, endTime):
    prefs = models.preferences(min_budget=minb, max_budget=maxb)
    dbconnect.session.add(prefs)
    times = models.times(start_time = startTime, end_time = endTime)
    dbconnect.session.add(times)
    dbconnect.session.commit()




