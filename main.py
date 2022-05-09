import time
class User:
    '''simulating a real user'''
    def __init__(self,first_name,last_name,age,city,salary,occupation):
        '''setting the initial attribtes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.salary = salary
        self.occupation = occupation
        self.login_attempts = 0
    def describe_user(self):
        '''describing the user'''
        print(f'Mr {self.first_name}, whose surname is {self.last_name}, works in {self.city} as a {self.occupation} and his salary is {self.salary}\n')
        
    def greet_user(self):
        '''greeting the user'''
        print(f' It was nice working with you Mr {self.first_name} {self.last_name}, \n\t\t\t Do have a nice day!')

    def increment_login_attempts(self):
        '''to increment the login value attempts by 1'''
        if self.login_attempts <=2:
            self.login_attempts +=1
            print(f'the login attempts is {self.login_attempts}')
        else:
            print('please wait for 10secs before you login again')
            time.sleep(10)
            self.reset_login_attempts()

    def reset_login_attempts(self):
        '''to reset login attmpt to 0'''
        self.login_attempts = 0
        print(f'the login attempts is now {self.login_attempts}')
patrick = User('Patrick','Ebong',40,'Lagos',200000,'Programmer')
patrick.increment_login_attempts()
patrick.increment_login_attempts()
patrick.increment_login_attempts()
patrick.increment_login_attempts()
patrick.increment_login_attempts()
patrick.increment_login_attempts()
#creating instances
my_first_User = User('patrick', 'Ebong', 30, 'Lagos', 100000, 'lecturer')
my_second_User = User('Jacob', 'Mabu', 25, 'Maiduguri', 50000, 'Soldier')
my_third_User = User('Steven', 'Jobs', 19, 'Anambra', 20000, 'POS attendant')
my_fourth_User = User('John', 'Shonibare', 17, 'kano', 10000, 'Teacher')
my_fifth_User = User('Peter', 'Oguns', 35, 'Enugu', 1000000, 'Programmer')

#calling the method
my_first_User.describe_user()
my_first_User.greet_user()
my_second_User.describe_user()
my_second_User.greet_user()
my_third_User.describe_user()
my_third_User.greet_user()
my_fourth_User.describe_user()
my_fourth_User.greet_user()
        