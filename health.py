import random
health = 50
difficulty = random.randint(1,3)
portion_health = int(random.randint(25,50)/difficulty)
health = health+portion_health
print(health)

