---

# 🌍 AQI Prediction Web App

An interactive **Air Quality Index (AQI) prediction** tool built with **Streamlit** and powered by **Machine Learning**. Predict AQI using environmental inputs and compare model performance in real-time.

🔗 **[Try the Live App Here](https://aqipredictbygirish.streamlit.app/)**

---

## 📽️ Live Demo

![AQI Prediction Demo](https://media.giphy.com/media/v1.YOUR-GIF-LINK-HERE/giphy.gif) <!-- Replace with actual GIF URL -->

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

The app predicts AQI using machine learning models trained on environmental data. A simplified AQI approximation formula is used (can be customized):

```python
AQI = (NO₂ + CO + O₃) / 3
```

> ℹ️ You can replace this with official AQI formulas like CPCB or EPA standards for real-world accuracy.

---

## 🧪 Methodology

1. **Data Collection**:
   Sourced from the [UCI Air Quality dataset](https://archive.ics.uci.edu/ml/datasets/Air+Quality).

2. **Preprocessing**:
   • Removed nulls and invalid rows
   • Selected key pollutants & meteorological features

3. **Feature Engineering**:
   • Created AQI using pollutant averages (NO₂, CO, O₃)

4. **Model Training**:
   • Linear Regression
   • Random Forest
   • AdaBoost

5. **Evaluation Metrics**:
   • R² Score
   • Mean Absolute Error (MAE)
   • Root Mean Squared Error (RMSE)

6. **Deployment**:
   • Deployed on Streamlit Cloud with real-time inputs

---

## 📊 Model Performance

| Model             | R² Score  | MAE      | RMSE     |
| ----------------- | --------- | -------- | -------- |
| Linear Regression | 0.877     | 2.72     | 3.28     |
| Random Forest     | **0.999** | **1.29** | **1.84** |
| AdaBoost          | 0.991     | 1.41     | 2.13     |

🧩 Includes graphs of predicted vs actual AQI for all models (in notebook).

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

### Clone the Repository

```bash
git clone https://github.com/G1r1shCodes/AQI-Prediction-Using-Machine-Learning.git
cd AQI-Prediction-Using-Machine-Learning
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
streamlit run app.py
```

---

## 🌟 Deployed Version

▶️ **Live App:** [aqipredictbygirish.streamlit.app](https://aqipredictbygirish.streamlit.app/)

You can use the app on any device with a browser—no installations needed!

---

## 🌱 Future Enhancements

* [ ] Integrate **official AQI standards** (e.g., CPCB, EPA)
* [ ] Add **real-time sensor/IoT data**
* [ ] UI enhancements (charts, filters, dark mode)
* [ ] Save predictions with **database backend**
* [ ] Deploy REST API for other applications

---

## 🙌 Contributing

Pull requests are welcome! For major changes, open an issue to discuss improvements or bugs first.

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

## 📸 More Visuals (Add GIFs Below)

* **Model Comparison**
  ![Model Comparison](https://media.giphy.com/media/v2.YOUR-GIF2/giphy.gif)

* **User Interaction**
  ![User Form Submission](https://media.giphy.com/media/v3.YOUR-GIF3/giphy.gif)

> 🎥 *You can create these GIFs using tools like [ScreenToGif](https://www.screentogif.com/) or [Loom](https://www.loom.com/). Upload to GitHub or Giphy and embed.*

---
