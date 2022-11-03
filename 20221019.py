
##양수 음수 구별
# def b(a):
#     if(a>0):
#         print(f'{a}는 양수 입니다')
#     elif(a<0):
#         print(f'{a}는 음수 입니다')


# while 1:
#     a=int(input('숫자를 입력해주세요 : '))
#     b(a)












##입력한 2개의 수 비교
# def C(a,b):
#     if(a==b):
#         print('두 수가 같습니다')
#     elif(a<b):
#         print(f'{a}가 {b}보다 작습니다')
#     elif(a>b):
#         print(f'{a}가 {b}보다 큽니다')


# print('숫자를 2개 입력하세요 : ')
# a=int(input(''))
# b=int(input(''))

# C(a,b)










# ##Q 14.2 모름
# def ABC():
    










##코드 15-2 선택지가 한가지 뿐인 모험
# do = input(":: ")
# if do == "LOOK":
#         print("모래 둑이 있는 도랑에 갇혔습니다.")
#         print("왼쪽(LEFT)이나 오른쪽(RIGHT)으로 엉금엄금 기어갑니다.")


#         do = input(":: ")
#         if do == "LEFT":
#             print("도랑 밖으로 기어 나왔습니다. 배가 있네요!")
#             print("살아 남았습니다!")
#         elif do =="RIGHT":
#             print("아! 둑으로 올라갈 수가 업습니다. 오른쪽 둑은 아주 미끄럽습니다.")
#             print("멀리 미끄러져 내려가 이상한 동굴로 떨어졌습니다.")
#             print("살아남지 못했습니다 :(")
# else:
#     print("대문자로 표시된 동작만 입력해 주십시오.")
#     print("다시 도전해 보십시오!") 












# a = int (input('')) ##입력한 수만큼 안녕 반복 

# for n in range(a):
#     print("안녕")










# ##1부터 100까지의 짝수에 대해 6으로 나누어 떨어지는 수의 갯수
# a=0

# for i in range(1,101):
#     if(i%2==0):
#         if(i%6==0):
#             a+=1
            
# print(a)







# n=int(input())   ##반복 예제

# for i in range(n,0,-1):
#     print(f"파이썬 책 {i}권이 들어 있는 책장에 파이썬 책이 {i}권")
#     print(f"책을 한 권 꺼내 돌려고보 나니 {i-1}권이 남았네.")








# a, b, c=input("입력:: ").split() ##split()=문자열 나누기

# print(f'안녕 {a}')
# print(f'안녕 {b}')
# print(f'안녕 {c}')







##리스트 예제

# array = [273, 32, 103, "문자열", True, False]
# print(array)
# print(array[0])
# print(array[5])
# print(array[-1])








##파이썬 책 144p
# list_a = [1,2,3]
# list_b = [4,5,6]

# print("# 리스트")
# print("list_a=",list_a)
# print("list_b=",list_b)
# print()


# print("# 리스트 기본 연산자")
# print("list_a+list_b=", list_a + list_b)
# print("list_a * 3 =", list_a * 3)
# print()




# print("# 길이 구하기")
# print("len(list_a) =",len(list_a))








# List_a=[1,2,3]

# print("#리스트 뒤에 요소 추가하기")
# List_a.append(4)
# List_b.append(5)
# print(List_a)
# print()

# print("#리스트 중간에 요소 추가하기")
# List_a.insert(0,10)
# print(List_a)








##문제2

# numbers = [273,103,5,32,65,9,72,800,99]

# for number in numbers:
#     if(number>100):
#         print("-100이상의 수:", number)






#문제3

# numbers = [273,103,5,32,65,9,72,800,99]
# for number in numbers:
#     if(number%2==1):
#         print(f'{number}은 홀수 입니다.')
#     elif(number%2==0):
#         print(f'{number}은 짝수 입니다.')

# numbers = ["273","103","5","32","65","9","72","800","99"]
# for x in numbers:
#     print(x,"는",len(x),"자릿수 입니다")    







##문제4 리스트 중첩 해제
# List_of_List =[[1,2,3],[4,5,6,7],[8,9],]
# for a in List_of_List:
#     for b in a:
#         print(b)



 






# dict_b
# {'director': ['안소니 루소','조 루소'],'cast': ['아이언맨','타노스','토르','닥터스트레인지','헐크']}
# dict_b["director"]
# ['안소니 루소','조 루소']




##173p 문제 4 리스트,딕셔너리 혼합

# character = {
#     "name":"기사",
#     "level":"12",
#     "items":{
#         "sword":"불꽃의검",
#         "armor":"풀플레이트"
#         },
#     "skill":["베기","세게 베기","아주 세게 베기"]
#     }
    
# for key in character:
#     if type(character[key]) is dict:
#         for k in character[key]:
#             print('{} : {}'.format(k, character[key][k]) )
#     elif type(character[key]) is list:
#         for item in character[key]:
#             print('{} : {}'.format(key,item))
#     else:
#         print('{} : {}'.format(key,character[key]))

   


























##예제
# dit_a={"a":"엉망진창","b":"장난하누","c":"나가리네"}

# print("dictionary item : ",type(dit_a),len(dit_a),dit_a)
# print("+++++++++++++++++++++++++++++++++++++++++")

# for i in dit_a.items():
#     print("dictionary item : ",type(i),i)
# print("+++++++++++++++++++++++++++++++++++++++++")








##함수 예제
# def a(i,j):

#     sum=i+j
#     num=i*j
#     ddd=i-j
#     return sum,num,ddd

# print(a(3,4))









##253P 해볼것
# def power(item):
#     return item*item
# def under_3(item):
#     return item<3



# List_input_a = [1,2,3,4,5]



# output_a=map(power,List_input_a)
# print("#map() 함수의 실행결과")
# print("map(power,List_input_a):",output_a)
# print("map(power,List_input_a):", list(output_a))
# print()




# output_b=filter(under_3,List_input_a)
# print("#filter() 함수의 실행결과")
# print("filter(under_3,List_input_a):",output_b)
# print("filter(under_3,List_input_a):",list(output_b))





# file = open("bssic.txt","w")
# file.write("Hello python programming...!")
# file.close()