from pathlib import Path

import cv2
import numpy as np
from tensorflow.keras.models import load_model

model_path = Path(__file__).resolve().parents[1] / "models" / "neurovision_cnn.keras"
# print(model_path)

class_names = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary",
]

model = load_model(model_path)


def predict_image(image_path):

    image = cv2.imread(str(image_path))

    if image is None:
        raise ValueError("Unable to read the image.")

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.resize(image, (224, 224))

    image = image.astype(np.float32) / 255

    image = np.expand_dims(image, axis=0)

    predictions = model.predict(image, verbose=0)[0]

    prediction_index = np.argmax(predictions)

    return {
        "class": class_names[prediction_index],
        "confidence": float(predictions[prediction_index]),
    }


# image_path = "../data/raw/glioma/images.jpg"

# result = predict_image(image_path)

# print("Predicted class:", result["class"])
# print("Confidence:", f"{result['confidence']:.2%}")


