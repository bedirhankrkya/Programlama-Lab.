
def my_f_1(inList=[4, -3, 5, -2, -1, 2, 6, -2]):
    maxsum = 0
    n = len(inList)
    for i in range(n):
        for j in range(i+1, n):
            t = 0
            for k in range(i, j+1):
                t = t + inList[k]
                if(t > maxsum):
                    maxsum = t
    return maxsum

def m_f_2(list1=[4,-3,2,1,-2,6,-2]):
    n=len(list1)
    maxsum=0
    for i in range (n):
        t=0
        for j in range(i,n):
            #print(i,j)
            t=t+list1[j]
            if(t>maxsum):
                maxsum=t
    return maxsum

print(m_f_2(list1=[4,-3,5,-2,-1,2,6,-2,4,-3,5,-2,-1,2,6,-2])) 



#Diziyi her seferinde ikiye bölerek daha hızlı arama yapmamıza yarayan fonskiyon.


def my_f_3(list1=[4,-3,5,-2,-1,2,6,-12]):
    n=len(list1)
    if(n==1):
        return list1[0]
    left_i=0
    left_j=n//2
    
    right_i=n//2
    right_j=n    
    left_sum=my_f_3(list1[left_i:left_j])
    right_sum=my_f_3(list1[right_i:right_j])  
    temp_left_sum=0
    t=0
    for i in range(left_j-1,left_i-1,-1):
        t=t+list1[i]
        if(t>temp_left_sum):
            temp_left_sum=t
    temp_right_sum=0
    t=0
    for i in range(right_i-1,right_j-1,-1):
        t=t+list1[i]
        if(t>temp_right_sum):
            temp_right_sum=t
    center_sum=temp_left_sum+temp_right_sum
    return max_of_three(left_sum,right_sum,center_sum)    
def max_of_two(a,b):
    if(a>b):
        return a
    else:
        return b
def max_of_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))