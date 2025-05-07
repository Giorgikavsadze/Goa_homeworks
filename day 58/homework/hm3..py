# 5) Use a lambda function to convert a list of temperatures from Celsius to Fahrenheit.


celsius_temps = [0, 10, 20, 30, 40]
celsi_to_fahre=lambda celsius: (celsius*9/5)+32

print(list(map(celsi_to_fahre,celsius_temps)))