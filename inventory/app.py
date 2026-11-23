
from flask import Flask, render_template, request
from knapsack import fractional_knapsack, zero_one_knapsack

app = Flask(__name__)

# Sample inventory products
products = [
    {"name": "Laptop", "weight": 5, "profit": 500},
    {"name": "Mobile", "weight": 3, "profit": 300},
    {"name": "Headphones", "weight": 2, "profit": 150},
    {"name": "Keyboard", "weight": 4, "profit": 200},
    {"name": "Monitor", "weight": 6, "profit": 450},
    {"name": "Mouse", "weight": 1, "profit": 80},
    {"name": "Printer", "weight": 7, "profit": 400}
]


@app.route("/", methods=["GET", "POST"])
def home():

    capacity = 10
    fractional_items = []
    zero_one_items = []

    fractional_profit = None
    zero_one_profit = None

    if request.method == "POST":

        try:
            capacity = int(request.form.get("capacity"))

            if capacity <= 0 or capacity > 100:
                raise ValueError

            # Run Fractional Knapsack
            fractional_items, fractional_profit = fractional_knapsack(
                products, capacity
            )

            # Run 0/1 Knapsack
            zero_one_items, zero_one_profit = zero_one_knapsack(
                products, capacity
            )

        except (ValueError, TypeError):
            capacity = 10

    return render_template(
        "index.html",
        products=products,
        capacity=capacity,
        fractional_items=fractional_items,
        zero_one_items=zero_one_items,
        fractional_profit=fractional_profit,
        zero_one_profit=zero_one_profit
    )


if __name__ == "__main__":
    app.run(debug=True)
