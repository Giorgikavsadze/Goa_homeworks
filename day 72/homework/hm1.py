# Regex validate PIN code

def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for i in pin:
            if i < '0' or i > '9':
                return False
        return True
    else:
        return False
    
    