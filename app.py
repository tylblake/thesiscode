from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder="static")

def get_outfit(occasion, weather, preferences, size):
    outfit_suggestions = {
        "work": {
            "sunny": {"formal": "Blazer with dress shirt", "casual": "Button-down shirt", "comfortable": "Polo shirt"},
            "rainy": {"formal": "Waterproof suit", "casual": "Sweater and jeans", "comfortable": "Hoodie and joggers"},
            "cold": {"formal": "Wool suit", "casual": "Jacket and chinos", "comfortable": "Sweater and thermal pants"},
        },
        "casual": {
            "sunny": {"formal": "Dress shirt and chinos", "casual": "T-shirt and jeans", "comfortable": "Shorts and sneakers"},
            "rainy": {"formal": "Trench coat with dress shoes", "casual": "Denim jacket and sneakers", "comfortable": "Waterproof hoodie"},
            "cold": {"formal": "Long coat with scarf", "casual": "Sweater and jeans", "comfortable": "Thermal hoodie"},
        },
        "party": {
            "sunny": {"formal": "Slim-fit suit", "casual": "Fitted shirt and jeans", "comfortable": "Loose shirt and sneakers"},
            "rainy": {"formal": "Stylish coat with boots", "casual": "Leather jacket and jeans", "comfortable": "Warm hoodie"},
            "cold": {"formal": "Velvet blazer with pants", "casual": "Knitted sweater and chinos", "comfortable": "Puffer jacket"},
        }
    }

    outfit = outfit_suggestions.get(occasion, {}).get(weather, {}).get(preferences, "Outfit not found")
    return f"{outfit} (Size: {size})"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_outfit', methods=['POST'])
def recommend_outfit():
    data = request.json
    occasion = data.get("occasion")
    weather = data.get("weather")
    preferences = data.get("preferences")
    size = data.get("size")

    outfit = get_outfit(occasion, weather, preferences, size)
    return jsonify({"outfit": outfit})

if __name__ == '__main__':
    app.run(debug=True)
