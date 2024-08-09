import flet as ft
from calories_app import get_calories

def main(page: ft.Page):
    page.title = "Calorie Counter"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    food_input = ft.TextField(label="Enter food item", width=200)
    add_button = ft.ElevatedButton(text="Add", on_click=lambda e: add_food(page, food_input))
    total_calories_text = ft.Text("Total Calories: 0", size=20)

    page.add(
        food_input,
        add_button,
        total_calories_text
    )

def add_food(page: ft.Page, food_input: ft.TextField):
    food_item = food_input.value
    calories = get_calories(food_item)
    if calories:
        total_calories = int(page.controls[2].value.split(": ")[1])
        total_calories += calories
        page.controls[2].value = f"Total Calories: {total_calories}"
        food_input.value = ""
        page.update()
    else:
        ft.SnackBar(ft.Text("Food not found or error occurred.")).open = True
        page.snack_bar = ft.SnackBar(ft.Text("Food not found or error occurred."))
        page.update()

ft.app(target=main)