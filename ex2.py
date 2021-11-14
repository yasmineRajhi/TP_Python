def count(str):
    lower =0
    upper =0
    for i in range(len(str)):
        # to lower case letter
        if (str[i] >= 'a' and str[i] <= 'z'):
            lower += 1
        # to upper case letter
        elif (str[i] >= 'A' and str[i] <= 'Z'):
            upper += 1
        else:
            continue
    print(f"lower {lower} & upper {upper}")

chaine=input("saisir une chaine de caractére : ")
print(count(chaine))