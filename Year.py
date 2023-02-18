while True:
    number = int(input("=======================================\n=======================================\nВведите год для проверки: "))
    c=0
    def moth(ddMM):
        b=0
        for i in range(1,ddMM+1):
            b+=i%10+i//10
        return b
    c+=moth(31)*7
    c+=moth(30)*4
    if(number %4 == 0 and number %100 != 0)or number % 400 == 0:
        c+=moth(29)
        print("Високосный год")
    else:
        c+=moth(28)
        print("Невисокосный год") 
    print("Ержансих дней в этом году:", + c)     
    
    