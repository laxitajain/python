#transpose of a matrix:----
matrix=[ [1,2,3],[4,5,6],[7,8,9],[0,1,2]]
a=[[row[i] for row in matrix] for i in range(3)] #in nested comp, the inner loop is written first, an outer later
print(a)
b=[[column[i] for column in a] for i in range(4)]
print(b)
#equiv to: 
x=[ [1,2,3],[4,5,6],[7,8,9],[0,1,2]]
t=[]
for i in range(3):
    t.append([r[i] for r in x])
print(t)
#equiv to:
x=[ [1,2,3],[4,5,6],[7,8,9],[0,1,2]]
t=[]
for i in range(3):
    transp_row=[]
    for r in x:
        transp_row.append(r[i])
    t.append(transp_row)
print(t)
#another way:
a=list(zip(*x))
print(a)

