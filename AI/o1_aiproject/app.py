from flask import Flask, request, jsonify
from data_modeling import train_model
from data_loading import load_data

app = Flask(__name__)
df = load_data("data.csv")
model = train_model(df, "target_column")

@app.route("/predict", methods=["POST"])
def predict():
    data_input = request.json
    prediction = model.predict([data_input])
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)