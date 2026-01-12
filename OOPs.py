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
# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print(f"This {self.animal} is eating")
#     def sleep(self):
#         print(f"This {self.name} is sleeping")

# class Prey(Animal):
 
#     def flee(self):
#         print(f"This {self.name} is fleeing")
# class Predator(Animal):
#     def hunt(self):
#         print(f"This {self.name} is hunting")
# class Rabbit(Prey):
#     pass
# class Hawk(Predator):
#     pass
# class Fish(Prey,Predator):
#     pass

# rabbit = Rabbit("mona")
# hawk= Hawk("tony")
# fish = Fish("nimo")

# fish.hunt()
# fish.flee()
# rabbit.flee()
# rabbit.eat()


#Abstract class
# from abc import ABC,abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
    
# class Car(Vehicle):
#     def go(self):
#         print("You drive the car")
#     def stop(self):
#         print("You stop the car") 
        
# class Motocycle(Vehicle):
    
#     def go (self):
#         print("You ride the motorcycle")
        
#     def stop(self):
#         print("You stop the motorcycle")

# class Boat(Vehicle):
#     def go (self):
#         print("You sail the boat")
    
#     def stop(self):
#         print("You anchor the boat")
        
# boat = Boat() 
# boat.go()
# boat.stop()           
              
              
# super() function
# class Shape:
#     def __init__(self,color,is_filled):
#         self.color = color
#         self.is_filled = is_filled
        
#     def describe(self):
#         print(f"it is {self.color} and {'filled' if self.is_filled else 'not filled'}")    
# class Circle(Shape):
#     def __init__(self,color,is_filled,radius):
#         super().__init__(color,is_filled)
#         self.radius = radius
        
#     def describe(self):
#         super().describe()
#         print(f"Its is a circle with an area of {3.14 * self.radius*self.radius}cm^2")
        
        

# class Square(Shape):
#     def __init__(self,color,is_filled,width):
#         super().__init__(color,is_filled)
#         self.width = width
        
       
    
# class Triangle(Shape):
#     def __init__(self,color,is_filled,width,height):
#         super().__init__(color,is_filled)
#         self.width = width
#         self.height = height                          
       
# circle = Circle("red",True,5)
# square = Square("blue",False,6)
# triangle = Triangle("yesllow",True,7,8)
# print(circle.radius) 
# print(f"the radius of circle is {circle.radius}")    
# print(f"{triangle.height}")
# print(square.color)

# circle.describe()
# square.describe()
# triangle.describe()
# circle.describe()
         



#Polymorphism

# from abc import ABC , abstractmethod
# class Shape:
#     def area(self):
#         pass
        

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
        
    
#     def area(self):
#       return 3.14*self.radius**2      

# class Square(Shape):
#      def __init__(self,side):
#         self.side= side
   

#      def area(self):
#         return self.side **2        

# class Triangle(Shape):
#      def __init__(self, base, height):
#         self.base = base
#         self.height = height
#      def area(self):
#         return self.base * self.height* 0.5 
    
# class Pizza(Circle):
#     def __init__(self,topping,radius):
#         super().__init__(radius)
#         self.topping = topping
             
        
        
# shapes = [Circle(4),Square(5),Triangle(6,7),  Pizza("Oregano",15)]

# for shape in shapes:
#     print(f"{shape.area()}cm2")
       
         
# Duck Typing

# class Animal:
#     alive = True  
    
# class Dog(Animal):
#     def speak(self):
#         print("Woof")
        
# class Cat(Animal):
#     def speak(self):
#         print("Meaow")
        
# class Car:
#     alive = False
#     def speak(self):
#         print("honk")
               

# animals = [Dog(),Cat(), Car()] 

# for animal in animals:
#     animal.speak()
#     print(animal.alive)


#Aggregation

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
        
    def add_book(self,book):
        self.books.append(book)  
        
    def list_books(self): 
        return [f"{book.title} by {book.author}" for book in self.books]    

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
library = Library("New york times")
book1 = Book("mili ghosh","kankana")
book2 = Book("ABCD","eGFn")
book3 = Book("hello","hey") 

library.add_book(book1)  
library.add_book(book2)   
library.add_book(book3)  

print(library.name)   

for book in library.list_books():
    print(book)  
    
                       