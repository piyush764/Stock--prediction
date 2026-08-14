import { useState } from 'react';
import './App.css';

function App() {
  const [prevClose, setPrevClose] = useState('');
  const [ma5, setMa5] = useState('');
  const [ma10, setMa10] = useState('');
  const [pctChange, setPctChange] = useState('');
  const [prediction, setPrediction] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: `Prev_Close=${prevClose}&MA5=${ma5}&MA10=${ma10}&Pct_Change=${pctChange}`
    });

    const data = await response.json();
    setPrediction(data.predicted_price);
  };

  return (
    <div className="App">
      <h2>Adani Power Price Predictor</h2>
      <form onSubmit={handleSubmit}>
        <input value={prevClose} onChange={(e) => setPrevClose(e.target.value)} placeholder="Previous Close" /><br />
        <input value={ma5} onChange={(e) => setMa5(e.target.value)} placeholder="5-Day MA" /><br />
        <input value={ma10} onChange={(e) => setMa10(e.target.value)} placeholder="10-Day MA" /><br />
        <input value={pctChange} onChange={(e) => setPctChange(e.target.value)} placeholder="% Change" /><br />
        <button type="submit">Predict</button>
      </form>

      {prediction !== null && <h3>Predicted Price: ₹{prediction.toFixed(2)}</h3>}
    </div>
  );
}

export default App;
