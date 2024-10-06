#http://codeforces.com/contest/985/problem/B  Switches and Lamps
phone={1:'ij',    2: 'abc',3: 'def', 4: 'gh',    5: 'kl',    6: 'mn' ,7: 'prs' ,  8: 'tuv' ,  9: 'wxy' , 0 :'oqz'}
w={}
for i in phone:
    for g in range(0,len(phone[i])):
        w[phone[i][g]]=i
d=['dennis','it','your','reality','real','our']
d.sort(key = lambda s: len(s),reverse=True)

b='7325189087'
# print(b[0],phone[int(b[0])][1])
# for i in b:
#     for j in phone[int(i)]:
#         for k in d:
#             if k[0]==j:
#                 print (k,k[0],j,i)
#     print ("-------")
#
#     def find_values(c,a):
#         return (list(c.keys())[list(c.values()).index(a)])


for i in d:
    a=''
    for j in range(0,len(i)):
        a=a+str(w[i[j]])
    print ('r   ',a,len(a),b[len(a):])
    print ('x   ',i,b,b.find(a))

#
#
# for k in d:
#     for g in range(0,len(k)):
#         print (g,k[g])
#         # print(phone.keys()[phone.values().index('it')])
#     print("---------")



# while (call_no!="-1"):
#     call_no=input()
#     lines_of_data = int(input())
#     words=[]
#     for i in range(0,lines_of_data):
#         words.append(input())
#     print(call_no,lines_of_data,words)
