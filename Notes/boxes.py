###
# A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. Write a Python program named boxes.py that asks the user for two integers: the number of manufactured items the number of items that the user will pack per box Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.
###

import math

n_items = int(input("Please enter the number of manufactured items: "))
items_per_box = int(input("Please enter the number of items you will pack per box: "))

boxes = math.ceil(n_items / items_per_box)
print(f"The number of boxes you will need is {boxes}.")

