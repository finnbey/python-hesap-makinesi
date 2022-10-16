import os
from time import sleep
temizle =lambda:os.system('cls')
class degıskenler():
    sayi1 = int(0)
    sayi2 = int(0)
    

       
def main():
    temizle()
    print(" işlemnizi seçiniz")
    print("1 toplama")
    print("2 çıkarma")
    print("3 çarpma")
    print("4 bölme")

    print("sayılarıları giriniz")

    degıskenler.sayi1 = int(input("i.sayı  "))
    degıskenler.sayi2 = int(input("2.sayı  "))
    
    seçim = int(input(" işlem seçiminiz  "))
    
    
    
    if int(seçim) ==int(1):
       return toplama()
    if int(seçim) ==int(2):
       return çıkarma()
    if int(seçim) ==int(3):
       return çarpma()
    if int(seçim) ==int(4):
       return bölme()
    if int(seçim) >=int(5):
        print("geçersiz seçenek")
        sleep(3)
        return main()
      
def toplama():
    
    print("sonucunuz ",int(degıskenler.sayi1)+int(degıskenler.sayi2))
    seçim = input("yeniden hesaplamak istermisniz  1 evet 2 hayır")
    
    if int(seçim) == 1:
        return main()
    if int(seçim) == 2:
        temizle()
        exit()
    
def çıkarma():
    
    print("sonucunuz ",int(degıskenler.sayi1)-int(degıskenler.sayi2))
    seçim = input("yeniden hesaplamak istermisniz  1 evet 2 hayır")
    
    if int(seçim) == 1:
        return main()
    if int(seçim) == 2:
        temizle()
        exit()

def çarpma():
    
    print("sonucunuz ",int(degıskenler.sayi1)*int(degıskenler.sayi2))
    seçim = input("yeniden hesaplamak istermisniz  1 evet 2 hayır")
    
    if int(seçim) == 1:
        return main()
    if int(seçim) == 2:
        temizle()
        exit()

def bölme():
    
    print("sonucunuz ",int(degıskenler.sayi1)/int(degıskenler.sayi2))
    seçim = input("yeniden hesaplamak istermisniz  1 evet 2 hayır")
    
    if int(seçim) == 1:
        return main()
    if int(seçim) == 2:
        temizle()
        exit()
        
        
main()
  
  
