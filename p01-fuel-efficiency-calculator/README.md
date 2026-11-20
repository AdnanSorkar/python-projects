# Fuel Efficiency Calculator

A command-line program that turns trip metrics into a clear fuel efficiency report with a rating.

## Features
* Ask for distance, fuel used, and fuel price.
* Show km/L, L/100 km, and cost per km.
* Rate performance: 15+ km/L is Efficient, 10+ is Average, and anything else is High use.
* Show a friendly message if fuel used is 0 without crashing.

## How to Run
Run the program from your terminal using:
python main.py

## Sample Input and Output
Enter distance driven (km): 450
Enter fuel used (liters): 30
Enter fuel price per liter: 120

--- Fuel Report ---
Distance: 450.0 km
Fuel Used: 30.0 L
Fuel Efficiency: 15.00 km/L
Fuel Consumption: 6.67 L/100 km
Cost per km: 8.00 /km
Rating: Efficient

## What I Learned
* Taking user inputs and converting them using `float()`.
* Formatting outputs cleanly using Python f-strings.
* Implementing conditional logic (`if / elif / else`) to assign ratings and handle edge cases like zero fuel.

## Future Improvements
* Add support for multiple trip logs.
* Save the output report directly to a file.