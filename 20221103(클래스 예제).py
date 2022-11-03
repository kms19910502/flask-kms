# class Human:
#     def _init_(self,name,age,sex):
#         self.name =name
#         self.age =age
#         self.sex =sex
    
#     areum = Human('아무개',40,'남자')

#     print(areum.age)
    #클래스 안에서 출력이나 어떤 동작을 하려면 메서드(인스턴스)가 필요하다

   




# class Human:
#     def _init_(self,name,age,sex):
#         self.name =name
#         self.age =age
#         self.sex =sex

        

#     def zzz(self):
#         print("이름: {}, 나이 {}, 성별 , {}",fomat(self.name,self.age,self.sex))









# class Student():
#     def start(self):
#         print('안녕하세요')
#     def printName(self,name):
#         print('이름은 {0}입니다'.format(name))



# stu=Student
# Student.start(stu)
# stu.printName('홍길동')














# class Student():
#     schoolName = '단원고등학교'
#     schoolName2 = '양지고등학교'
#     schoolName3 = '초지고등학교'
# stu1 =Student()
# stu2 =Student()

# print('stu1의 주소 : {0}'.format(id(stu1)))
# print('stu2의 주소 : {0}'.format(id(stu2)))

# # Student.schoolName='seoul'

# print("\nStuedent의 학교: ",Student.schoolName)
# print("\nstu1의 학교: ",stu1.schoolName2)
# print("\nstu2의 학교: ",stu2.schoolName3)











# #try_except

# x=1
# try:
#     print(x)
# except:
#     print("error")















# a=['1','2','3','4','5']

# try:
#     for i in a:
#         print(int(i))

# except:
#     print("error")






# a = 10

# if a== 10:
#     pass
# else:
#     print('틀림')





# #클래스 구구단 호출
# class kkk:
#     def abc():
#          for i in range(2,10):
#             for j in range(1,10):
#                 print(f'{i} X {j} = {i*j}')
#             print(" ")


# aaa = kkk.abc()
# print(aaa)

        








# class Gugudan:

#     def printAll(self):

#         for i in range(2, 10):

#             for j in range(1, 10):

#                 print(f"{i} X {j} = {i*j}")

#             print(" ")

 

# gu = Gugudan()

# gu.printAll()


















##예제

class kms:
    def aaa(self):
        a=int(input('숫자를 입력하세요: '))
        if (a%2==0):
            print("짝수입니다")
        else:
            print("홀수 입니다.")

    def bbb(self):
        f=int(input(''))
        b=int(input(''))
        c=int(input(''))
        d=int(input(''))

    
        print(f'평균은 {(f+b+c+d)/4} 입니다.')


    def ccc(self):
        for i in range(4):
            for j in range(4):
                print("*", end="")
            print(" ")


ddd = kms()

print('홀수 짝수 구별')
print(" ")
ddd.aaa()

print(" ")
print(" ")

print("평균구하기")
ddd.bbb()
print(" ")
print(" ")

print("*사각형")
ddd.ccc()
print(" ")


