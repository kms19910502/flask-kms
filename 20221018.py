# for i in range(3):
#     for j in range(i+1):
#         print('*',end=' ')
#     print(' ')






# for i in range(0,3): #좌 반쪽 마름모
#     for j in range(0,i+1):
#         print('*',end=' ')
#     print(' ')
# for a in range(0,2):
#     for b in range(0,2-a):
#         print('*',end=' ')
#     print(' ')









# for i in range(0,3): #피라미드
#     for j in range(0,2-i):
#        print(' ',end='')
#     for k in range(2-i,i+3):
#         print('*',end='')
#     print(' ')







# for i in range(0,3): #다이아몬드
#     for j in range(0,2-i):
#        print(' ',end='')
#     for j in range(2-i,i+3):
#         print('*',end='')
#     print(' ')
# for i in range(0,2):
#     for j in range(0,i+1):
#         print(' ',end='')
#     for j in range(i+1,4-i):
#         print('*',end='')
#     print(' ')







# for i in range(0,3): #오른쪽이 직각인 삼각형
#     for j in range(0,2-i):
#         print(' ',end='')
#     for j in range(2-i,3):
#         print('*',end='')
#     print(' ')








# for i in range(0,3): #반쪽 마름모(좌)
#     for j in range(0,2-i):
#         print(' ',end='')
#     for j in range(2-i,3):
#         print('*',end='')
#     print(' ')

# for i in range(0,3):
#     for j in range(0,i+1):
#         print(' ',end='')
#     for j in range(i+1,3):
#         print('*',end='')
#     print(' ')






# for i in range(0,3):    #역피라미드
#     for j in range(0,i):
#         print(' ',end='')
#     for j in range(i,5-i):
#         print('*',end='')
#     print(' ')




# for i in range(0,5):    #역피라미드2
#     for j in range(0,i):
#         print(' ',end='')
#     for j in range(i,9-i):
#         print('*',end='')
#     print(' ')



# for i in range(0,4): #*찍기 사각형
#     for j in range(0,4):
#         print('*',end='')
#     print('')




# for a in range(2,10): #1~9단 세로 출력
#     for b in range(1,10):
#         print(f'{a} X {b} = {a*b}')
#     print(' ')




# print('1.콜라=300원 2.사이다=400원 3.녹차=100원') #자판기
# while 1:

#     a=int (input('입력해 주세요 : '))

#     if a==300:
#         print('콜라 입니다.')
#     elif a==400:
#         print('사이다 입니다.')
#     elif a==100:
#         print('녹차 입니다')
#     print(' ')






# a =[2,3,4,5,6,7,8,9]
# b=[1,2,3,4,5,6,7,8,9]

# for i in b:
#     for j in a:
#         print(f'{i}X{j}={i*j}')
# print(' ')






# print("before")
# a = [[1, 2, 3],[4, 5, 6]]

# for b in range(0,6):
#     print(f'{a[b]}')








# a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] #2차원 뒤집기
# print('before')
# print(' ')

# for i in range (0,4):
#     for j in range(0,4):
#         print('%3d'%(a[i][j]),end='')
#     print(' ')
# print(' ')
# print('after')
# print(' ')
# for i in range (4,0,-1):
#     for j in range(4,0,-1):
#         print('%3d'%(a[i-1][j-1]),end='')
#     print(' ')











##분을 시간으로 변환하는 예제

# a=int (input('분을 입력하세요 : ')) 
# print(f'{a//60}시간 {a%60}분입니다.')










##화씨 섭씨 변환

# a=75

# print(f'{(a-32)/1.8}입니다.')










#마일을 킬로미터와 미터로 변환

# a=5

# print(f'{a}')
# print('마일')

# print(f'{a/0.62137:.5f}')
# print('킬로미터')
# print(f'{(a/0.62137)*1000:.5f}')
# print('미터')










##replace 문자열 변환 예제

# s='Eat Work Play Sleep repeat'
# s=s.replace('Eat ','')
# s=s.replace('Work','Working')
# s=s.replace('Play','Playing')
# s=s.replace('Sleep','')
# s=s.replace(' repeat','')
# print(s)


# ##replace 문자열 변환 예제(정답)
# A=('Eat work play sleep repeat')
# B=A.replace(A,'working playing')
# print(B)





