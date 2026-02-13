def adjust_calories(tdee, goal): #Macro Strategy Engine
    goals = {
        "cut": 0.8,
        "recomp": 1.0,
        "lean_bulk": 1.1,
        "bulk": 1.2
    }

    return tdee * goals[goal]

def calculate_macros(calories, strategy):
    macro_strategies = {
        "cut": {"protein": 0.35, "carbs": 0.40, "fat": 0.25},
        "bulk": {"protein": 0.30, "carbs": 0.50, "fat": 0.20},
        "recomp": {"protein": 0.35, "carbs": 0.40, "fat": 0.25}
    }

    distribution = macro_strategies[strategy]

    protein_cal = calories * distribution["protein"]
    carbs_cal = calories * distribution["carbs"]
    fat_cal = calories * distribution["fat"]

    return {
        "protein_g": protein_cal / 4,
        "carbs_g": carbs_cal / 4,
        "fat_g": fat_cal / 9
    }

