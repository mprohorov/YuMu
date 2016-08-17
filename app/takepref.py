from app import models

def enterPrefs(minb, maxb, activity, radius, location):
    prefs = models.preferences(min_budget = minb, max_budget = maxb,
                               activity = activity, radius = radius, location = location)
    return prefs