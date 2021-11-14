def convert(temperature,n):
    if(n=="1"):
        temperature = (temperature - 32)/1.8
    elif(n=="2"):
        temperature = 32 + 1.8 * temperature
    elif(n==""):
        temperature = 32 + 1.8 * temperature
    return(temperature)

n = input("conversion température :\nmethode 1 :°F --> °C\nmethode 2 : °C --> °F (choisir 1/2) : ")
temp = float(input("la temperature à convertir : "))
print(convert(temp,n))