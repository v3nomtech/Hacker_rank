def check_sum(x,y,z,n):
     new_list= [[i,j,k]for i in range(x+1) for j in range(y+1) for k in range (z+1) if i+j+k != n ]
     print(new_list)


    



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    check_sum(x,y,z,n)
