from django.db import models

# Create your models here.
class Recipe(models.Model):
    dishe_name = models.CharField(max_length=255)
    autor = models.CharField(max_length=255) 
    # ingredients = ... # Chave estrangeira pra uma tabela de ingredientes.

"""
CREATE TABLE Recipes (
    recipe_id INT PRIMARY KEY AUTO_INCREMENT,
    recipe_name VARCHAR(255) NOT NULL,
    description TEXT,
    instructions TEXT NOT NULL,
    prep_time INT,  -- in minutes
    cook_time INT,  -- in minutes
    total_time INT, -- in minutes
    servings INT
);

CREATE TABLE Ingredients (
    ingredient_id INT PRIMARY KEY AUTO_INCREMENT,
    ingredient_name VARCHAR(255) NOT NULL
);

CREATE TABLE RecipeIngredients (
    recipe_ingredient_id INT PRIMARY KEY AUTO_INCREMENT,
    recipe_id INT,
    ingredient_id INT,
    quantity DECIMAL(10, 2),  -- Adjust precision as needed
    unit VARCHAR(50),
    FOREIGN KEY (recipe_id) REFERENCES Recipes(recipe_id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id)
);
"""