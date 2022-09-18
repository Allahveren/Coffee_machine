class coffee_machine:
    
    
    def __init__(self):
        self.resources = {'water':300 , 'milk':200 , 'coffee':100}
        self.profit = 0
        self.menu = {'espresso':{'cost':1.5 ,'inqredients':{'water':50 , 'coffee':18}},
        'latte':{'cost':2.5 ,'inqredients':{'water':200 , 'coffee':24 , 'milk':150}},
            'cappucino':{'cost':3 ,'inqredients':{'water':250 , 'coffee':24, 'milk':100}}}

    
    def info(self):
        '''resours haqqinda melumat verir'''
        print(f"Water:{self.resources['water']} ml")
        print(f"Milk:{self.resources['milk']} ml")
        print(f"Coffee:{self.resources['coffee']}g")
        print(f'Profit:$ {self.profit}')

    def check_resources(self):
        '''resourslari yoxlayir'''
        for x in self.menu[self.user]['inqredients']:
            if self.menu[self.user]['inqredients'][x] > self.resources[x]:
                print(f'There is no enough {x}')
                return False
                break
        return True
                    

    def process_coins(self):
        '''odenis prosessi gedir, musteriden odenis meblegi isteyir'''
        self.fifty = int(input('How many fifty coins? '))
        self.twenty = int(input('How many twenty coins? '))
        self.ten = int(input('How many ten coins? '))

        print(f'Total: {(self.fifty*50 + self.twenty*20 + self.ten*10)/100} azn')
        return (self.fifty*50 + self.twenty*20 + self.ten*10)/100

            

    def check_transaction_succesfull(self):
        ''' verilen meblegi yoxlayir'''
        if self.amount < self.menu[self.user]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            return  False
        else:
            self.change = round(self.amount - self.menu[self.user]['cost'],2)
            print(f"Here's your change : {self.change}")
            self.profit += self.menu[self.user]['cost']
            return  True


        
    def make_coffee(self):
        '''coffee hazirlanir ve ingredientler yoxlanilir'''
        for x in self.menu[self.user]['inqredients']:
            self.resources[x] -= self.menu[self.user]['inqredients'][x]
        print(f'Here"s your {self.user}')


    def add_resources(self):
        self.resources['water'] = 300
        self.resources['milk'] = 200
        self.resources['coffee'] = 100


    def main_function(self):
        ''' bu funksiya daxilinde her bir emeliyyat icra olunur, odenis meblegi
        ve resours kifayet qederdirse, kofe hazirlanib size sunulur.'''
        while True:
            self.user = input('What would you like? (espresso/ latte / cappucino): ').lower()
            if self.user == 'off':
                print('Thank for choosing us')
                break
            elif self.user == 'fill':
                self.add_resources()
                print('Succesfull filled')
            elif self.user == 'report':
                self.info()
            elif self.user == 'latte' or self.user == 'cappucino' or self.user == 'espresso':
                self.have_enough = self.check_resources()
                if self.have_enough:
                    self.amount = self.process_coins()
                    if self.check_transaction_succesfull():
                        self.make_coffee()