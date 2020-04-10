import csv,sys
ayDeger=[]
sayisalAyDegerleri=[]
degerler=[]
histogram={}
with open(sys.argv[1]) as dosya:#with open(sys.argv[1]+"input_hw_2.csv") as dosya:
    okur = csv.reader(dosya,delimiter=";")
    for satir in okur:
        ayDeger.append(satir)
    for index in ayDeger:
        sayisalAyDegerleri.append(int(index[3].split("-")[1]))          
    for counter in sayisalAyDegerleri:
        if (counter in histogram.keys()):
            histogram[counter]=histogram[counter]+1
        else:
            histogram[counter]=1
    
    for k in histogram:
        degerler.append(histogram[k])
#mod bulma

def ortalama(degerler):
    counter=0
    toplam=0
    for i in range (len(degerler)):
        toplam=toplam+degerler[i]
        counter=counter+1
    ortalama=toplam/counter
    return ortalama

#Sıralama
def bubble_sort(my_list):
    n=len(my_list)
    for i in range(n-1,-1,-1):
        for j in range (0,i):
            if not(my_list[j]<my_list[j+1]):
                #print("swap işlemi")
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp    

    return my_list

#median
def my_median(my_list):
    my_list_2=bubble_sort(degerler)
    n=len(my_list_2)
    if n%2==1:
        middle=int(n/2)
        median=my_list_2[middle]
    else:
        middle_1=my_list_2[int(n/2)-1]
        middle_2=my_list_2[int(n/2)]
        median=(middle_1+middle_2)/2
    return median

with open(sys.argv[2], mode='w') as f:#with open(sys.argv[2]+'180401057_hw_2_output.txt', mode='w') as f:
    employee_writer = csv.writer(f, delimiter='=', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(["Median", my_median(degerler)])
    employee_writer.writerow(["Ortalama", ortalama(degerler)])
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            