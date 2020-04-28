#parametre olarak alınan index ile  çocuklarını karşılaştırıp 
#aralarından en küçüğünü bulan ve bunları sıralayan recursive işlem.
#parametre olarak bir dizi alır
def min_heapify(array,i):
    left=2*i+1
    right=2*i+2
    length=len(array)-1
    smallest=i
    if left <= length and array[i]>array[left]:
        smallest=left
    if right <= length and array[smallest]>array[right]:
        smallest=right
    if smallest != i:
        array[i],array[smallest]=array[smallest],array[i]
        min_heapify(array,smallest)

#sırayla, parametre olarak gönderilen dizideki tüm elemanlar
#min_heapify fonksiyonuna gönderilir ve en sondan o diziyi heap haline getirir.
def build_min_heap(array):
    #tersten başlamak için reversed ü kullandık
    for i in reversed(range(len(array)//2)):
        min_heapify(array,i)

my_array_1=[8,10,3,4,7,15,1,2,16]
build_min_heap(my_array_1)
print(my_array_1)
#heapsort algoritması, heapify ve build_heap ile dizi sıralamak için kullanılır
#gönderilen dizideki kök ile son elemanın yeri değişir.
#son eleman yeni listeye ekleniyor. Eski listeden siliniyor ve heapify'e yollanıyor.
#Böylece liste küçükten büyüğe sıralanıyor fonksiyondan döndürülüyor
def heapsort(array):
    array=array.copy()
    build_min_heap(array)
    
    sorted_array=[]
    for _ in range (len(array)):
        array[0],array[-1]=array[-1],array[0]
        sorted_array.append(array.pop())
        min_heapify(array,0)
    return sorted_array

my_array_2=heapsort(my_array_1)
print("Sıralanmış heap : ",heapsort(my_array_2))

#Fonksiyona gönderdiğimiz diziye yine gönderdiğimiz değeri eklemeye yarayan fonksiyon.
#eğer ekleme yapıldıysa dizi yeniden heap haline getirilip geri döndürülecek
def insertItemToHeap(myheap_1,item):
    for i in range (len(myheap_1)):
        if myheap_1[i]==item:
            #gönderdiğimiz eleman zaten listede olduğu için ekleme yapmaz.
            #Listeyi olduğu gibi geri döndürürüz.
            print("eklemek isediğiniz eleman zaten heapte var!")
            return myheap_1
    #Eğer eklemek istediğimiz eleman listede yoksa listeye ekliyoruz ve heap haline getirip 
    #geri döndürüyoruz.
    myheap_1.append(item)
    build_min_heap(myheap_1)
    return myheap_1
eklenecek_sayi=int(input("Eklemek İstediğiniz Sayiyi Giriniz."))
print("Sayı Eklendikten sonra Heap : ",insertItemToHeap(my_array_1,eklenecek_sayi))

"""
#Heap i aynı zamanda sıralayan fonksiyon
def insertItemToHeap_sorted(myheap_1,item):
    for i in range (len(myheap_1)):
        if myheap_1[i]==item:
            print("eklemek isediğiniz eleman zaten heapte var!")
            return myheap_1
    myheap_1.append(item)
    build_min_heap(myheap_1)
    myheap_1=heapsort(myheap_1)
    return myheap_1

print("Sayı Eklendikten ve sıralandıktan sonra Heap : ",insertItemToHeap_sorted(my_array_1,eklenecek_sayi))
""" 

#Gönderdiğimiz dizinin en küçük elemanını silmeye yarayan fonksiyon.
def removeItemFrom(myheap_1):
    myheap_1=heapsort(myheap_1)#İlk olarak diziyi sıralarız.
    myheap_1[0],myheap_1[-1]=myheap_1[-1],myheap_1[0]#kök ve en son elemanın yerini değiştirir. 
    myheap_1.pop()#En küçük elemanı sileriz
    build_min_heap(myheap_1)#diziyi tekrar heap haline getiririz.
    return myheap_1

print("İlk elemanı çıkarılmış heap : ",removeItemFrom(my_array_1))
"""
#En küçük sayıyı çıkardıktan sonra sıralayan fonksiyon
def removeItemFrom_sorted(myheap_1):
    myheap_1=heapsort(myheap_1)
    myheap_1[0],myheap_1[-1]=myheap_1[-1],myheap_1[0]
    myheap_1.pop()
    myheap_1=heapsort(myheap_1)
    return myheap_1

print("İlk elemanı çıkarılmış ve sıralanmış heap : ",removeItemFrom_sorted(my_array_1))
"""