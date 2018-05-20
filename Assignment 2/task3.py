

matrix= [[1,2,3,4,5,6,7,8],   #hardcore 8x8 matrix
        [9,10,11,12,13,14,15,16],
        [17,18,19,20,21,22,23,24],
        [25,26,27,28,29,30,31,32],
        [33, 34, 35, 36, 37, 38, 39, 40],
        [41, 42, 43, 44, 45, 46, 47, 48],
        [49, 50, 51, 52, 53, 54, 55, 56],
        [57, 58, 59, 60, 61, 62, 63, 64]]



sub_matrix=[[None,None], # 2x2 matrix to store input
            [None,None]]

input = raw_input("Enter values of 2 x 2 submatrix (SPACE SEPERATED) ")
input=input.split(' ')
sub_matrix[0][0]=int(input[0]);
sub_matrix[0][1]=int(input[1]);
sub_matrix[1][0]=int(input[2]);
sub_matrix[1][1]=int(input[3]);

first_element=sub_matrix[0][0]

col_matrix=[] #ith co-ordinates    both work together
row_matrix=[] #yith co-oridnates
dup_index=0;

for row in matrix: #to get all the locations of the first element of submatrix in the original matrix
    for element in row :
        if first_element == element:
          row_matrix.append(matrix.index(row))
          col_matrix.append(dup_index)
        dup_index+=1 #incase of  multiple entries per row
    dup_index=0

i=0

# calculate limits
below_limit=8-2
right_limit=8-2

counter=0#to iterate through col matrix list

flag=False

starting_i=None # will store result
starting_y=-None

for i in row_matrix:
    y=col_matrix[counter] # the first co-ordinate
    if i<=below_limit and y<=right_limit:
        #calculate adjacents
        right_value=matrix[i][y+1]
        below_value=matrix[i+1][y]
        below_right_value=matrix[i+1][y+1]
        if right_value==sub_matrix[0][1] and below_value== sub_matrix[1][0] and below_right_value==sub_matrix[1][1]:#if a valid co-ordinate
            flag=True
            starting_i=i
            starting_y=y
            break
    counter+=1

print "\nMatrix : " #display results
for row in (matrix):
    print row
print "\nSubmatrix : "
for row in (sub_matrix):
    print row
if flag==True:
    print "\n\nStarting point is : ( {i} , {y} )".format(i=starting_i,y=starting_y)
else:
    print  "\n\nSorry it seems that the provided matrix isn't a sub matrix"










