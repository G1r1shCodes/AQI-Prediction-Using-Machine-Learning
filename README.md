# 🌍 AQI Prediction Web App

A simple and interactive **Air Quality Index (AQI) prediction** app built with **Machine Learning** (Random Forest & AdaBoost) and **Streamlit**. Users can input environmental features like CO, NO₂, O₃, temperature, and humidity, and get real-time AQI predictions.

---

## 📊 Features

- Predict AQI based on environmental parameters  
- User-friendly interface powered by **Streamlit**
- Trained using **RandomForestRegressor** and **AdaBoostRegressor**
- Modular and scalable project structure
- Exported model with `joblib` for easy reuse

---

## 📁 Project Structure

```
AQI-Prediction-Using-Machine-Learning/
│
├── app.py               # Streamlit frontend application
├── utils.py             # Helper function to format user input
├── aqi_model.pkl        # Trained RandomForestRegressor model
├── requirements.txt     # Required Python libraries
└── AirQualityUCI.csv    # Dataset (optional for reference)
```

---

## 🧠 How It Works

The model predicts AQI using a simple formula:

```python
AQI = (NO2 + CO + O3) / 3  # Used as a placeholder for real AQI
```

You can customize this by replacing it with **official AQI computation formulas** later.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/aqi-predictor-app.git
cd aqi-predictor-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

Your browser will open at `http://localhost:8501` where you can interact with the app.

---

## 📥 Example Inputs

| Feature                | Sample Value |
|------------------------|--------------|
| CO (mg/m³)             | 2.5          |
| NO₂ (µg/m³)            | 40.0         |
| O₃ (µg/m³)             | 20.0         |
| Temperature (°C)       | 25.0         |
| Relative Humidity (%)  | 50.0         |
| Absolute Humidity      | 1.2          |

---

## 📈 Model Performance

Trained on cleaned UCI Air Quality Dataset using:

- **RandomForestRegressor**  
- **AdaBoostRegressor**

Sample R² Score: `~0.95` (on test set)

---

## 📦 Requirements

- Python 3.7+
- Streamlit
- pandas
- numpy
- scikit-learn
- joblib

---

## 🛠 Future Improvements

- Use official AQI calculation method (e.g., CPCB formula)
- Add model comparison toggle in UI
- Store past predictions
- Integrate live sensor data (IoT support)

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---
