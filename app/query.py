from . import models

def getPrefsbyEventId(eventId):
    prefs = models.preferences.query(models.preferences).\
        filter(models.preferences.eventID == eventId)
    return prefs
