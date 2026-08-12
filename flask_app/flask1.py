from flask import Flask ,request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('stock_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('stock_form.html')

if __name__ == "__main__":
    app.run(debug=True)



