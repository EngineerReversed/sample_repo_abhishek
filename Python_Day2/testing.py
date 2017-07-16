house = ['TV', 'Fridge', 'Oven', 'AC', 6]

class quantiphi():
    """Making a difference"""
    def __init__(self,name):
        self.name=name
    def work(self):
        print(self.name+" is rocking")

class SearchDog():
    """dog search"""
    def __init__(self,name):
        self.name=name
    def search(self):
        print(self.name+' is searching')
company = SearchDog('Tomy')
print(company.name+' is a search dog')   
company.search()

company=quantiphi('Quantiphi')
print(company.name+' is my company')
company.work()