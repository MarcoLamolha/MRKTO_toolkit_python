from flask import Flask, request, jsonify
from src.model import train_model
from src.data_processing import load_data, preprocess_data

app = Flask(__name__)

# Load and preprocess data
data = load_data('data/data.csv')
data = preprocess_data(data)

# Train model
model = train_model(data, 'target_column')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    # Process input_data as needed
    prediction = model.predict([input_data])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)