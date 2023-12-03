################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
print()

# Local Scope
print("Local Scope")
def drink_potion():
    potion_strength = 2 # Local
    print(potion_strength)
drink_potion()
print()


# Global Scope
print("Global Scope")
player_health = 10 # Global
def drink_potion_health():
    potion_strength = 3
    print(potion_strength)
    print(player_health)
drink_potion_health()
print()


# Local vs Global
print("Local vs Global")
player_health = 10 # Global
def game():
    def drink_potion9(): # Local to game function
        potion_strength = 9
        print(potion_strength)
        print(player_health)
    drink_potion9()
# drink_potion9() # won't work as we calling outside of the game function
game()
print()

# Python has no Block Scope
print("Python has no Block Scope")
game_level = 3
def create_enemy():
    enemies_list = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies_list[0]
    print(new_enemy)
create_enemy()
print()


# Modify a Global Scope?
print("Modify a Global Scope")
enemies = 1
# # You can modify the global scope but it is not recommended to do so
# def increase_enemies_global():
#   global enemies
#   enemies += 1
#   print(f"enemies inside function: {enemies}")
# increase_enemies_global()
# print(f"enemies outside function: {enemies}")

# The Recommend way is to use return functions
def increase_enemies_global():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies_global()
print(f"enemies outside function: {enemies}")
print()

# Python Constants & Global Scope
# Global Constants
print("Python Constants & Global Scope\nGlobal Constants")
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"
def print_pi():
    print(f"PI = {PI}")
print_pi()
print()
