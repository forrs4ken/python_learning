

word=input("Lütfen bir kelime giriniz: ")
x=input("aramak istediğiniz harfi giriniz: ")

for i in word:
 

 if i==x:
  print("kelime aradiginiz harfi icerir.")
  break
else:
  print("kelime aradiginiz harfi icermez.")

input("Çıkmak için Enter'a bas...")
