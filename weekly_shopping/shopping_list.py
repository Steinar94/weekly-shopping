import json
import tomli
import random


class DinnerPlanner:
    def __init__(
        self,
        recipe_file="dinner_recipes.json",
    ):
        self.recipe_file = recipe_file
        self.recipes = self.load_dinner_recipes()

    def save_html_to_file(self, filename, html_content):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(html_content)

    def load_dinner_recipes(self):
        try:
            with open(self.recipe_file, "r") as file:
                recipes = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            recipes = {}
        return recipes

    def load_email_credentials(self, config_file):
        with open(config_file, "r") as file:
            config_data = tomli.load(file)
        return config_data.get("email", {})

    def save_dinner_recipes(self):
        with open(self.recipe_file, "w") as file:
            json.dump(self.recipes, file, indent=2)

    def add_dinner(self, name, ingredients):
        self.recipes[name] = ingredients
        self.save_dinner_recipes()

    def generate_weekly_plan(self, num_days=7):
        if num_days > len(self.recipes):
            raise ValueError(
                "Number of days exceeds the available number of dinner recipes"
            )
        selected_dinners = random.sample(list(self.recipes.keys()), k=num_days)
        return selected_dinners

    def combine_ingredients(self, selected_dinners):
        combined_ingredients = {}
        for dinner in selected_dinners:
            ingredients = self.recipes[dinner]
            for ingredient, quantity in ingredients.items():
                combined_ingredients[ingredient] = (
                    combined_ingredients.get(ingredient, 0) + quantity
                )
        return combined_ingredients

    def create_dict_for_email(self):
        dinners = self.generate_weekly_plan()
        ingredients = self.combine_ingredients(dinners)

        return {
            "Middager": dinners,
            "Handleliste": ingredients,
        }


planner = DinnerPlanner()


planner.add_dinner("Lasagne", {"kjøttdeig": 1, "lasagne plater": 1, "tomat saus": 1})
planner.add_dinner(
    "Pizza", {"kjøttdeig": 1, "pizza bunn": 1, "pizza saus": 1, "ost": 1}
)
planner.add_dinner("pasta di parma", {"pasta di parma": 1, "bacon": 1, "parmesan": 1})
planner.add_dinner(
    "Taco",
    {"kjøttdeig": 1, "lefse": 1, "taco krydder": 1, "salat til taco": 1, "ost": 1},
)
planner.add_dinner("Blomkålsuppe", {"kjøtt buljong": 1, "blomkål": 1})
planner.add_dinner(
    "Flyvende Jakob",
    {"Kylling Filét": 3, "Fløte": 1, "Bacon Terninger": 1, "Chilli Saus": 1},
)
planner.add_dinner("Spaghetti", {"Spaghetti": 1, "Kjøttdeig": 1, "Spaghetti Saus": 1})

shopping_list = planner.create_dict_for_email()
