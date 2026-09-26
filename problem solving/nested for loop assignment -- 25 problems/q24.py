num = int(input("enter a number :"))
# for i in range(num,0,-1):
#     for j in range(0,i):
#         if j==1:
#             print("5",end="")
#         elif j==2:
#             print("4",end="")
#         elif j==3:
#             print("3",end="")
#         elif j==4:
#             print("2",end="")
#         elif j==5:
#             print("1",end="")
#     print()


for i in range(num):
    for j in range(num,i,-1):
        print(j,end=" ")
    print()