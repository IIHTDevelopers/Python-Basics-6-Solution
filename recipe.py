import pandas as pd

# ✅ Function to read recipe data from a text file
def read_recipe_file(filename):
    """
    Args:
        filename (str): Path to the recipe text file

    Returns:
        pd.DataFrame: DataFrame with columns ['Recipe', 'Calories', 'Ingredients']
    """
    data = []
    with open(filename, 'r') as file:
        for line in file:
            name, calories, ingredients = line.strip().split(",", 2)
            data.append({
                "Recipe": name,
                "Calories": int(calories),
                "Ingredients": ingredients.replace(";", ", ")
            })
    return pd.DataFrame(data)

def get_high_calorie_recipes(df, threshold=500):
    return df[df['Calories'] > threshold]

def get_ingredients(df, recipe_name):
    match = df[df['Recipe'] == recipe_name]
    if not match.empty:
        return match['Ingredients'].values[0]
    return "Recipe not found."

# 🔍 Example Usage
if __name__ == "__main__":
    df = read_recipe_file("recipes.txt")
    print("All Recipes:")
    print(df)

    print("\nHigh Calorie Recipes (>500):")
    print(get_high_calorie_recipes(df))

    print("\nIngredients for 'Pizza':")
    print(get_ingredients(df, "Pizza"))
