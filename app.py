from flask import Flask, render_template, request

app = Flask(__name__)

base_drinks = ["Citrus Burst", "Berry Delight", "Minty Fresh", "Spicy Surprise", "Sweet Dream", "Tropical Punch"]
add_ins = ["Lemon", "Mint Leaves", "Ginger", "Honey", "Coconut Milk"]
toppings = ["Whipped Cream", "Chocolate Syrup", "Sprinkles", "Cherries", "Cinnamon"]

@app.route("/", methods=["GET", "POST"])
def index():
    selected_drink = None
    selected_add_ins = []
    selected_toppings = []

    if request.method == "POST":
        selected_drink = request.form.get("drink")
        selected_add_ins = request.form.getlist("add_in")
        selected_toppings = request.form.getlist("topping")

    return render_template("index.html", base_drinks=base_drinks, add_ins=add_ins, toppings=toppings,
                           selected_drink=selected_drink, selected_add_ins=selected_add_ins, selected_toppings=selected_toppings)

if __name__ == "__main__":
    app.run(debug=True)
