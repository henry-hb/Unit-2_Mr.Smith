"""A general class that represents a student
"""
import random

class Student:
    
    def __init__(self,name:str,grade:int,id:str='000000'):
        """Creates a instance of a student with a name and grade
        """
        self.name = name
        self.grade = grade
        self.ID = id
        self.classes = []
        
    def add_class(self,class_:str)->None:
        self.classes.append(class_)
    
    ''' 
    def __repr__(self)->str:
        """Debugging info about the instance

        Returns:
            str: Student(name,grade)
        """
        
        pass
    
    def __str__(self)->str:
        """Descriptive info about the instance

        Returns:
            str: student name,ID, and grade on separate lines
        """
        pass
    
    def __eq__(self,student_two)->bool:
        """Determines if two students objects are the same

        Returns:
            bool: true if the name and id are the same, 
            false otherwise
        """
        pass
    '''
   

def main():
    student_one = Student("Noelle",11,'451234')
    student_two = Student("Ricky",12,'123456')
    student_three = Student("Brendan",10)
    student_four = Student("Brendan",10)
    
    
    print(student_one)
    print(student_two)
    print(student_three)
    print(student_four)

if __name__ == '__main__':
    main()