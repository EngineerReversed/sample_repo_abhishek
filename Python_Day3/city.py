city = {'alwar':'rajasthan','mainpuri':'uttar pradesh','kolkata':'west bengal'}
print(city[raw_input("Enter city")])
print(city.keys()[city.values().index(raw_input("Enter state"))])
