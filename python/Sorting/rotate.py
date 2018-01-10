import pprint

image = [
          [1,2,3],
          [1,0,1],
          [1,2,3]
          ]

pprint.pprint(image)

for i in range(3):
    for j in range(3):
        if i==0 and j ==2:
            break
        print i, j
        a= image[i][j]
        image[i][j], image[j][2-i] = image[j][2-i], image[i][j]
        image[j][2-i], image[2-i][2-j] =  image[2-i][2-j], image[j][2-i]
        image[2-i][2-j],  image[2-j][i] = image[2-j][i], image[2-i][2-j]
        image[2-j][i] = a

        pprint.pprint(image)


    if i ==0 and j == 2:
        break;

pprint.pprint(image)
