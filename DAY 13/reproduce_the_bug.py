from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])

# list index out of range error because the list index starts from 0 and ends at 5, but we are trying to access index 6 which does not exist. To fix this, we should change the line to: