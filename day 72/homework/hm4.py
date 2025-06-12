# Categorize New Member

def open_or_senior(data):
    result = []
    for age, i in data:
        if age >= 55 and i > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result