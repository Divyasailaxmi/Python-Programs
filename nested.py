list1 = [[1,2,3],[3,4,5],[2,4,1]]
list2 = [[1,2,3],[3,4,1],[1,4,3]]

for ( l1, l2 ) in zip(list1, list2):
    for ( i1, i2 ) in zip(l1, l2):
        if i1!=i2:
            print("Rejected", i1, i2)


# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if j > i :
#             break
#         else:
#             for k in range(len(list1[i])):
#                 for l in range(len(list2[j])):
#                     if k == l:
#                         print("accepted", list1[i][k] ,"&", list1[j][l])
#                         break
#                     else:
#                         print("rejected",list1[i][k] ,"&", list1[j][l])
#                         break
                    
    # print(i)
#     for k in range(len(list1[i])):
#         print("***********************", list1[i][k])
#     # print(i,list1[i],"\n")
# for j in  range(len(list2)):
#     # print(j,list2[j],"\n")
#     for k in range(len(list1[i])):
#         print("***********************", list1[j][k]) 
#         if list2[j][k] == list1[i][k]:
#             print(j,"accepted",list2[j][k])
#         else:
#             print(j,"rejected",list2[j][k])
#             break             

# list1 = [[1,2,3],[3,4,5],[2,4,1]]
# list2 = [[1,2,3],[3,4,1]]
# k = list1[1][2]
# k2 = list2[1][2]
# if k == k2:
#     print("Correct")
# else:
#     print("Wrong")                




