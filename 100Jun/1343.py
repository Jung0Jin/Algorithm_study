# # https://www.acmicpc.net/problem/1343

# import sys
# input=sys.stdin.readline

# n=input()

# arr=[]
# count=0
# for i in n:
#     if i=='X':
#         count+=1
#         continue
#     else:
#         if count!=0:
#             arr.append(count)
#             arr.append(0)
#             count=0
#         else:
#             arr.append(0)
# arr.pop()

# for i in arr:
#     if i%2==1:
#         print(-1)
#         exit(0)

# new_arr=[]
# A_count=0
# word=''
# for i in arr:
#     if i==0:
#         word='.'

#     if i>=4:
#         word='AAAA'*(i//4)
#         i=i-len(word)
    
#     if i==2:
#         word=word+'BB'
    
#     new_arr.append(word)
#     word=''

# #print(arr)
# #print(new_arr)
# print(''.join(new_arr))

board = input()

board = board.replace('XXXX','AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)