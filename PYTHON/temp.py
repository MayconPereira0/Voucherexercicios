###Identificar como está o tempo###

t = float(input("Qual a temperatura atual:"))
if(t > 30):
    print("Está calor")
elif(t <= 30 and t >= 14):
    print("Está agradavel") 
else:
    print("Está frio")      
