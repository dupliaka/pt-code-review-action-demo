def talking_cat():
   print("Meow! I am a magical talking cat.")
   name = input("What's your name? ")
   print(f"Nice to meet you, {name}! I can talk and even tell jokes.")

   favorite_food = input("What's your favorite food? ")
   if favorite_food.lower() in ["fish", "tuna", "salmon"]:
       print("Meow! That's my favorite too! Are you a cat secretly?")
   else:
       print(f"Interesting... I've never tried {favorite_food}. Do you recommend it to cats?")

   joke_permission = input("Want to hear a cat joke? (yes/no) ")
   if joke_permission.lower() == "yes":
       print("What do you call a pile of kittens? A meowtain. 😹")
   else:
       print("You're missing out on some purr-fect humor!")

   print("It was nice chatting! Time for my catnap. Bye!")

if __name__ == "__main__":
   talking_cat()
