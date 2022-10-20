#379p 클래스 내부에 함수 선언하기

# class Student:
#     def __init__(self,name,korean,math,english,science):
#         self.name=name
#         self.korean=korean
#         self.math=math
#         self.english=english
#         self.science=science

    
#     def get_sum(self):
#         return self.korean + self.math +\
#             self.english + self.science

#     def get_average(self):
#         return self.get_sum() / 4
    

#     def to_string(self):
#         return "{}\t{}\t{}".format(\
#             self.name,\
#             self.get_sum(),\
#             self.get_average())





# student = [
#     Student("윤인선",87,98,88,95),
#     Student("연하진",92,98,96,98),
#     Student("구지연",76,96,94,90),
#     Student("나선주",98,92,96,92),
#     Student("윤아린",95,98,98,98),
#     Student("윤명원",64,88,92,92)
# ]


# print("이름","총점","평균",sep="\t")
# for student in student:
#     print(student.to_string())











##
# class Rectangle:
#     count = 0
#     def __int__(self, width, height):
#         self.width = width
#         self.height = height
#         Rectangle.count += 1 
#     def calcArea(self):
#         area = self.width * self.height 
#         return area

    
# sqare = Rectangle(5,5)
# print(sqare)









