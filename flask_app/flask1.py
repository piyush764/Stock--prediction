from flask import Flask ,request,render_template
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)
model = pickle.load(open('stock_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('stock_form.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [
        float(request.form['Prev_Close']),
        float(request.form['MA5']),
        float(request.form['MA10']),
        float(request.form['Pct_Change'])
    ]
    prediction = model.predict([features])
    '''print(prediction)
    print(type(prediction))
    print(prediction.shape)'''
    return {"predicted_price": float(prediction[0][0])}

if __name__ == "__main__":
    app.run(debug=True)



