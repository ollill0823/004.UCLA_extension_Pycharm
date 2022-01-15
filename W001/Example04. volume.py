def rectPrismVol (height, length, width):
       volume = height * length * width
       return volume

prism1vol = rectPrismVol ( 4 , 6 , 10)
prism2vol = rectPrismVol ( 5.5 , 10 , 1)

print("Prism 1: ", prism1vol, "cu. ft. ")
print("Prism 2: ", prism2vol, "cu. ft. ")

print(type(prism1vol)) ## int =整數 ; float = 小數
print(type(prism2vol))

print("Is Prism 1 smaller ? The answer is ", prism1vol < prism2vol )