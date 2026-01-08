# #classes and objects
# #creating a class
# class Student:
#     name="kankana"
#     def __init__(self,fullname):
#         self.name = fullname
#         print("Adding new student in Database..")

# #creating an object (instance)
# s1 = Student("karan")
# print(s1.name) 

# s2 = Student()
# print(s2.name) 


# class Car:
#     color = "blue"
#     brand = "mercedes"
# car1 = Car()
# print(car1.color)    
  
# from car import Car         
# car1 = Car("BMW",2026,"red",False)
# car2 = Car("Audi",2025,"black",True)
# car3 = Car("Mercedes",2024,"yellow",False)

# print(car1.model)
# print(car2.year)
# print(car2.for_sale)
# print(car1.color)


#Methods
# car1.drive()
# car1.stop()
# car2.stop()
# car3.drive()
# car2.describe()


#class variables
# class Student:
#     class_year = 2024
#     num_students = 0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Student.num_students +=1
# stu1 = Student("kankana",30)
# stu2 = Student("mili",35) 
# stu3 = Student("kiran",19)
# stu4 = Student ("Tanu",78) 
# print(stu1.name)
# print(stu2.age) 
# print(stu1.class_year) 
# print(Student.class_year) 
# print(Student.num_students)   

# print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
# print(stu1.name)
# print(stu2.name)
# print(stu3.name)
# print(stu4.name)


#Inheritance

# class Animal:
#     def __init__(self,name):
#         self.name = name
#         self.is_alive = True
    
#     def eat(self):
#         print(f"{self.name} is eating")
    
#     def sleep (self):
#         print(f"{self.name} is sleeping")
        
# class Dog(Animal):
#     def speak(self):
#         print("woof!!")
# class Cat(Animal):
#     def speak(self):
#         print("meow!!")
# class Mouse(Animal):
#    def speak(self):
#         print("sqeeee!!")  

# dog = Dog("tommy")
# cat = Cat("tom")
# mouse = Mouse("micky") 

# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()

# cat.speak()


#Multiple inheritamce and Multilevel Inheritance
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"This {self.animal} is eating")
    def sleep(self):
        print(f"This {self.name} is sleeping")

class Prey(Animal):
 
    def flee(self):
        print(f"This {self.name} is fleeing")
class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit = Rabbit("mona")
hawk= Hawk("tony")
fish = Fish("nimo")

fish.hunt()
fish.flee()
rabbit.flee()
rabbit.eat()
        
         
         
                  