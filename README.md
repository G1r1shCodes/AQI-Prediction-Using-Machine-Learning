
# 🌍 AQI Prediction Web App

An interactive **Air Quality Index (AQI) prediction** app using **Machine Learning** (Random Forest, AdaBoost, and Linear Regression) and built with **Streamlit**. Users can input air quality features and receive real-time AQI predictions.

🔗 **Deployed App:** [https://aqipredictbygirish.streamlit.app/](https://aqipredictbygirish.streamlit.app/)

---

## 📊 Features

* Predict AQI from environmental parameters
* User-friendly web interface using **Streamlit**
* Trained on 3 models:

  * **RandomForestRegressor**
  * **AdaBoostRegressor**
  * **LinearRegression**
* Visualization and metric comparison across models
* Modular and scalable project structure

---

## 📁 Project Structure

```
AQI-Prediction-Using-Machine-Learning/
│
├── app.py               # Streamlit frontend
├── utils.py             # Helper functions for input
├── aqi_model.pkl        # Saved ML model (Random Forest by default)
├── Air Quality Prediction Using ML.ipynb  # Model training & evaluation notebook
├── requirements.txt     # Required Python libraries
└── AirQualityUCI.csv    # UCI dataset
```

---

## 🧠 How It Works

AQI is predicted based on input features using a trained regression model:

```python
AQI = (NO2 + CO + O3) / 3  # Simplified placeholder
```

The actual AQI model can be replaced with CPCB-compliant calculations for higher accuracy.

---

## 📊 Model Comparison

The models were evaluated using standard metrics:

| Model             | R² Score | Mean Absolute Error (MAE) | Root Mean Squared Error (RMSE) |
| ----------------- | -------- | ------------------------- | ------------------------------ |
| Linear Regression | 0.877    | 2.72                      | 3.28                           |
| Random Forest     | 0.999    | 1.29                      | 1.84                           |
| AdaBoost          | 0.991    | 1.41                      | 2.13                           |

📈 **Visual graphs** comparing actual vs predicted values and error plots are included in the notebook for better understanding.

---

## 📌 Abstract

This project aims to estimate the **Air Quality Index (AQI)** using environmental features like CO, NO₂, O₃, temperature, and humidity. We trained three regression models on the **UCI Air Quality dataset** and compared their predictive performance. The model is deployed using Streamlit to make it accessible and interactive.

---

## 🧪 Methodology

1. **Data Collection**: The `AirQualityUCI.csv` dataset from UCI repository was used.
2. **Preprocessing**:

   * Removed null and invalid values
   * Selected relevant pollutant and meteorological features
3. **Feature Engineering**:

   * AQI approximated using mean of pollutants (NO₂, CO, O₃)
4. **Model Training**:

   * Trained Linear Regression, Random Forest, and AdaBoost regressors
5. **Evaluation**:

   * Compared R², MAE, RMSE on test data
   * Visualized predictions vs ground truth
6. **Deployment**:

   * Developed an interactive app using Streamlit

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/G1r1shCodes/AQI-Prediction-Using-Machine-Learning.git
cd AQI-Prediction-Using-Machine-Learning
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 📥 Example Inputs

| Feature               | Sample Value |
| --------------------- | ------------ |
| CO (mg/m³)            | 2.5          |
| NO₂ (µg/m³)           | 40.0         |
| O₃ (µg/m³)            | 20.0         |
| Temperature (°C)      | 25.0         |
| Relative Humidity (%) | 50.0         |
| Absolute Humidity     | 1.2          |

---

## 🛠 Future Work

* Implement official AQI formulas (e.g., CPCB standard)
* Integrate real-time IoT sensor data
* Improve UI with model selection and live charts
* Add database backend for historical trends

---

## 🌐 Deployed Version

▶️ **Live App:** [https://aqipredictbygirish.streamlit.app/](https://aqipredictbygirish.streamlit.app/)

You can access it from any device—no setup needed.

---

## 🙌 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---
