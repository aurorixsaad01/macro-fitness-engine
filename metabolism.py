def calculate_bmr(weight, height, age, gender): #metabolism engine
    if gender.lower() == "male":
        return (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender.lower == "female":
        return (10 * weight) + (6.25 * height) - (5 * age) - 161
    else:
        raise ValueError("Invalid gender")
    
def calculate_tdee(bmr, activity_level): #tdee(energy budget of body)
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "athlete": 1.9
    }

    return bmr * activity_multipliers[activity_level]

    