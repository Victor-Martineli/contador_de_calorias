import flet as ft
from calories_app import get_calories
from record import add_to_record, get_record

def main(page: ft.Page):
    page.title = "Calorie Counter"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    food_input = ft.TextField(label="Enter food item", width=200)
    add_button = ft.ElevatedButton(text="Add", on_click=lambda e: add_food(page, food_input))
    total_calories_text = ft.Text("Total Calories: 0", size=20)
    record_text = ft.Text("Food Record:\n", size=16)

    page.add(
        food_input,
        add_button,
        total_calories_text,
        record_text
    )

    update_record_display(page)

def add_food(page: ft.Page, food_input: ft.TextField):
    food_item = food_input.value
    calories = get_calories(food_item)
    if calories:
        total_calories = int(page.controls[2].value.split(": ")[1])
        total_calories += calories
        page.controls[2].value = f"Total Calories: {total_calories}"
        add_to_record(food_item, calories)  # Add to record
        food_input.value = ""
        update_record_display(page)  # Update record display
        page.update()
    else:
        page.overlay.append(ft.SnackBar(ft.Text("Food not found or error occurred.")))
        page.update()

def update_record_display(page: ft.Page):
    record = get_record()
    record_text = page.controls[3]  # Get the record_text widget
    record_text.value = "Food Record:\n"

    record_text.controls.clear()
    
    for food, calories in record.items():
        record_text.value += f"{food}: {calories} calories\n"
    page.update()

ft.app(target=main)
