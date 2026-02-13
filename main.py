from metabolism import calculate_bmr, calculate_tdee
from macros import adjust_calories, calculate_macros
from tracker import add_entry
from visualizer import plot_progress
from prediction import predict_future
from datetime import datetime


def get_user_data():
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (cm): "))
    age = int(input("Enter age: "))
    gender = input("Enter gender (male/female): ")
    activity = input("Activity level (sedentary/light/moderate/active/athlete): ")
    goal = input("Goal (cut/recomp/lean_bulk/bulk): ")

    return weight, height, age, gender, activity, goal


def run_macro_calculator():
    weight, height, age, gender, activity, goal = get_user_data()

    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity)
    target_calories = adjust_calories(tdee, goal)
    macros = calculate_macros(target_calories, goal)

    print("\n--- RESULTS ---")
    print(f"BMR: {bmr:.2f} kcal")
    print(f"TDEE: {tdee:.2f} kcal")
    print(f"Target Calories: {target_calories:.2f} kcal")
    print(f"Protein: {macros['protein_g']:.2f} g")
    print(f"Carbs: {macros['carbs_g']:.2f} g")
    print(f"Fat: {macros['fat_g']:.2f} g")


def log_weight():
    weight = float(input("Enter today's weight (kg): "))
    today = datetime.today().strftime('%Y-%m-%d')
    add_entry(today, weight)
    print("Weight logged successfully.")


def show_prediction():
    days = int(input("Predict how many days ahead? "))
    predicted = predict_future(days)
    print(f"Predicted weight after {days} days: {predicted:.2f} kg")

def main():
    while True:
        print("\n==== Macro & Fitness Engine ====")
        print("1. Calculate Macros")
        print("2. Log Weight")
        print("3. Show Weight Graph")
        print("4. Predict Future Weight")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            run_macro_calculator()
        elif choice == "2":
            log_weight()
        elif choice == "3":
            plot_progress()
        elif choice == "4":
            show_prediction()
        elif choice == "5":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

