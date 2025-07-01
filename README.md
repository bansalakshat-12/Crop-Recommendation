# 🌾 Crop Recommendation System using Machine Learning

This project uses machine learning to recommend the most suitable crop to grow based on environmental conditions like soil nutrients, temperature, humidity, pH, and rainfall.

## 📌 Features

- Predicts the best crop to grow
- Based on soil nutrients (N, P, K) and weather data
- Interactive user interface using Streamlit
- Deployed online (optional)

## 🧠 Model Details

- **Algorithm**: Random Forest Classifier  
- **Accuracy**: 99.09% on training dataset  
- **Input Features**:  
  - Nitrogen (N)  
  - Phosphorus (P)  
  - Potassium (K)  
  - Temperature (°C)  
  - Humidity (%)  
  - pH level  
  - Rainfall (mm)

## 🖥️ Tech Stack

- Python
- Scikit-learn
- Pandas & NumPy
- Streamlit
- Git & GitHub

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/bansalakshat-12/Crop-Recommendation.git

# Change directory
cd Crop-Recommendation

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
