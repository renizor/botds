from operator import truediv
import time
from xml.etree.ElementTree import Comment
i = 0
ii = 0
iii = 0
while True:
    time_user = int(input("Введите кол-во секунд: "))
    Comment = str(input("Введите коментарий "))
    for q in range(time_user):
        time.sleep(1)
        i+=1
        print("прошло секунд:", i)
        if(i % 60) == 0: 
            ii ++ 1
            print("прошло минут:",ii )
            if(i % 3600) == 0: 
                iii += 1
            print ("прошло часов:",iii)
        print("время оконченно") 
        print("ваш коментарий:" ,Comment)