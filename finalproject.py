# Define the first recipe name, ingredients, and steps
recipe_1_name = "Spaghetti Bolognese"
recipe_1_ingredients = ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic", "salt", "pepper"]
recipe_1_steps = [
    "boil the spaghetti according to the insructions on the package.",
    "while spaghetti is boiling, chop the oinion and garlic.",
    "heat some olive oil in a pan.",
    "add the oinion and garlic to the pan and the sauce untill the oinion is translucent.",
    "add the ground beef to the pain and cook untill browned.",
    "add tomato sauce to the pan and season with salt and pepper.",
    "simmer the sauce for 15 minutes.",
    "serve the sauce over the cooked spaghetti."]

    # Define the second recpie name, ingredients and steps
recipe_2_name = "Chicken Tikka Masala"
recipe_2_ingredients = ["chicken breast", "tikka masala sauce", "rice", "yogurt", "cilantro", "salt", "pepper"]
recipe_2_steps = [
        "cook the rice according to the instructions on the package.",
        "while the rice is cooking, cut the chicken breast into cubes.",
        "heat some oil and butter in a pan.",
        "add the chicken to the pan and cook until browned.",
        "add the tikka masala sauce to the pan and season with salt and pepper.",
        "add yogurt to the pan and mix."
        "simmer the sauce for 15 minutes and stir occasionally.",
        "once done, garnish with chopped cilantro." 
        
        
]
def user_input():
    print("enter ingredients below")
    print("enter done when finished")
    ingredients = []
    while True:
        name = input("ingredient name: ")
        if name == "done":
            break
        ingredients.append(name)
    return ingredients

def main():
    ingredients = user_input()

main()
