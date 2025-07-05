# 🌍 AQI Prediction Web App

An interactive **Air Quality Index (AQI) prediction** tool built with **Streamlit** and powered by **Machine Learning**. Predict AQI using environmental inputs and compare model performance in real-time.

🔗 **[👉 Try the Live App](https://aqipredictbygirish.streamlit.app/)**

---

## 📽️ Live Demo

![AQI Prediction Demo](https://media.giphy.com/media/jp2Zt8oemStQ2/giphy.gif)

---

## 📊 Features

✅ Predict AQI from environmental parameters
✅ Select from 3 ML models:
    • Random Forest Regressor
    • AdaBoost Regressor
    • Linear Regression
✅ Clean, user-friendly web UI using **Streamlit**
✅ Visual comparisons of model performance
✅ Modular, reusable project structure

---

## 📁 Project Structure

```
AQI-Prediction-Using-Machine-Learning/
│
├── app.py                            # Streamlit web app
├── utils.py                          # Helper functions for input and formatting
├── aqi_model.pkl                     # Default ML model (Random Forest)
├── Air Quality Prediction Using ML.ipynb  # Jupyter notebook for training & analysis
├── requirements.txt                  # Required Python packages
└── AirQualityUCI.csv                 # Source dataset (UCI)
```

---

## 🧠 How It Works

The app predicts AQI using machine learning models trained on environmental data. A simplified AQI approximation formula is used:

```python
AQI = (NO₂ + CO + O₃) / 3
```

> ℹ️ You can replace this with official AQI formulas like CPCB or EPA standards for real-world accuracy.

---

## 🧪 Methodology

1. **Data Collection**

   * Sourced from the [UCI Air Quality dataset](https://archive.ics.uci.edu/ml/datasets/Air+Quality)

2. **Preprocessing**

   * Removed null and invalid rows
   * Selected key pollutant and weather features

3. **Feature Engineering**

   * Created AQI using pollutant averages (NO₂, CO, O₃)

4. **Model Training**

   * Linear Regression
   * Random Forest
   * AdaBoost

5. **Evaluation Metrics**

   * R² Score
   * Mean Absolute Error (MAE)
   * Root Mean Squared Error (RMSE)

6. **Deployment**

   * Interactive web UI using Streamlit

---

## 📊 Model Performance

| Model             | R² Score  | MAE      | RMSE     |
| ----------------- | --------- | -------- | -------- |
| Linear Regression | 0.877     | 2.72     | 3.28     |
| Random Forest     | **0.999** | **1.29** | **1.84** |
| AdaBoost          | 0.991     | 1.41     | 2.13     |

📈 Visualizations of predictions vs actual AQI and error metrics are available in the notebook.

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

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/G1r1shCodes/AQI-Prediction-Using-Machine-Learning.git
cd AQI-Prediction-Using-Machine-Learning
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 🌐 Deployed Version

▶️ **Live App:** [aqipredictbygirish.streamlit.app](https://aqipredictbygirish.streamlit.app/)

You can use the app on any device with a browser — no installations needed.

---

## 🛠️ Future Enhancements

* [ ] Integrate official AQI standards (e.g., CPCB, EPA)
* [ ] Real-time sensor/IoT data integration
* [ ] Enhanced UI with charts, filters, dark mode
* [ ] Add database backend for historical trends
* [ ] Create API for mobile or third-party use

---

## 🙌 Contributing

Pull requests are welcome!
For major changes, please open an issue to discuss improvements or features first.

---

## 📸 More Visuals

### 📈 Model Comparison

![Model Training](https://media.giphy.com/media/l0MYB8Ory7Hqefo9a/giphy.gif)

### 🧪 Prediction Concept

![Data Science Theme](https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif)


---
