arr1 = [
    1,2,
    3,4
]

arr2 = [
    5,6,
    7,8
]


tArr = []
# i repite el numero posicionado la misma cantidad de veces de lo que el arreglo es de largo
# x repite el patron de la matriz la misma cantidad de veces de lo que el arreglo es de largo  
for i in arr1:
    for x in arr1:
            tArr.append(arr1[x] + arr2[x])
            print(i, x, "|", arr1[x],"+", arr2[x],"=", tArr)