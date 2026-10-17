# 🧠 NeuroVision AI — Brain MRI Classification

## 📌 Project Overview

NeuroVision AI is a Deep Learning project that uses Convolutional Neural Networks (CNNs) to classify brain MRI images into four categories: **Glioma, Meningioma, No Tumor, and Pituitary**.

The project covers image preprocessing, CNN model training, evaluation, prediction, and deployment through a Streamlit web application.

> **Disclaimer:** This project is for educational purposes only. It is not intended for medical diagnosis or clinical decision-making.

## 🎯 Objectives

- Explore and preprocess brain MRI images.
- Build and train a CNN image classification model.
- Evaluate model performance using accuracy, a confusion matrix, and a classification report.
- Save and reuse the trained model without retraining.
- Develop a web interface for image prediction.

## 🛠️ Technologies Used

- **Python** — Main programming language
- **TensorFlow / Keras** — Deep Learning and CNN
- **OpenCV** — Image preprocessing
- **NumPy** — Numerical operations
- **Matplotlib / Seaborn** — Data visualization and evaluation
- **Streamlit** — Web application
- **uv** — Python dependency and environment management
- **Jupyter Notebook** — Data exploration and model training

## 📂 Project Structure

```text
NeuroVision-AI-Deep-Learning/
├── app/
│   └── app.py
├── data/
│   └── raw/
├── models/
│   └── neurovision_cnn.keras
├── notebooks/
│   ├── eda.ipynb
│   └── model_training.ipynb
├── src/
│   ├── __init__.py
│   └── predict.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

_Note: The structure above represents the intended organization. Keep only files and folders that actually exist in your repository._

## 🧠 Dataset

The dataset contains **7,055 brain MRI images** across four classes.

| Class      | Number of Images |
| ---------- | ---------------: |
| Glioma     |            1,621 |
| Meningioma |            1,645 |
| No Tumor   |            2,016 |
| Pituitary  |            1,773 |
| **Total**  |        **7,055** |

Images are resized to **224 × 224 pixels** and preprocessed before being passed to the model.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ISMAILBENMEZI/NeuroVision-AI-Deep-Learning.git
cd NeuroVision-AI-Deep-Learning
```

### 2. Install dependencies

Install [uv](https://docs.astral.sh/uv/) if it is not already installed, then run:

```bash
uv sync
```

### 3. Add the trained model

Place the trained model file in the following location:

```text
models/neurovision_cnn.keras
```

The model file must be available locally before running predictions. It may need to be downloaded separately if it is not included in the repository.

## 🚀 Run the Application

Start the Streamlit application from the project root:

```bash
uv run streamlit run app/app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

Upload a supported MRI image and click **Predict** to display the predicted class and the model's confidence score.

## 📊 Model Evaluation

The model evaluation workflow includes:

- Training and validation learning curves
- Accuracy and loss monitoring
- Confusion matrix
- Classification report
- Analysis of incorrect predictions

Refer to `notebooks/model_training.ipynb` for the training and evaluation workflow, provided the notebook is included in the repository.

## 🔮 Future Improvements

- Improve model generalization and evaluate potential overfitting.
- Experiment with CNN architectures and hyperparameters.
- Add a more detailed prediction interface.
- Improve inference performance and input validation.
- Add automated testing and experiment tracking.

## 👨‍💻 Author

**Ismail Benmezi**

- GitHub: [ISMAILBENMEZI](https://github.com/ISMAILBENMEZI)
- Portfolio: [ismailbenmezi.github.io/Portfolio](https://ismailbenmezi.github.io/Portfolio/)

---

**Disclaimer:** NeuroVision AI is an educational Deep Learning project. Its predictions must not be used as a substitute for professional medical evaluation.
