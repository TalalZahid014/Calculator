from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        room_type = request.form['room_type']
        occupancy = int(request.form['occupancy'])
        
        start_date = pd.to_datetime(request.form['start-date'])
        end_date = pd.to_datetime(request.form['end-date'])
        num_nights = (end_date - start_date).days - 1
        
        distance_cost = 911  # Assuming this is a constant distance cost
        total_cost = calculate_cost(num_nights, distance_cost, room_type, occupancy)
        return render_template('result.html', num_nights=num_nights, total_cost=total_cost)

def calculate_cost(num_nights, distance_cost, room_type, occupancy):
    # Placeholder logic for calculating total cost based on inputs
    # You can replace this with your actual calculation logic
    travel_cost = 34 + (30 * num_nights)
    food_cost = 25
    room_cost = {'double': 211, 'triple': 311, 'quad': 411}
    occupancy_cost = room_cost[room_type] * occupancy
    total_cost = distance_cost + (occupancy_cost * num_nights) + (food_cost * num_nights) + travel_cost
    return total_cost

if __name__ == '__main__':
    app.run(debug=True)