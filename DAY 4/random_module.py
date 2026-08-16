import random
import my_module
print(f"My favourite number is: {my_module.my_favourite_number}") 
  
random_number = random.randint(1, 100)
print(f"The random number generated is: {random_number}")

random_number_0_to_1 = random.random() * 10
print(f"The random number between 0 and 1 is: {random_number_0_to_1}")

random_float = random.uniform(1, 10)
print(f"The random float between 1 and 10 is: {random_float}")

random_heads_or_tails = random.choice(['Heads', 'Tails'])
print(f"The coin flip result is: {random_heads_or_tails}")

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("The coin flip result is: Heads")
else:    
    print("The coin flip result is: Tails")