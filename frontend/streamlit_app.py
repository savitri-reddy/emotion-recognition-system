import streamlit as st
import requests

st.set_page_config(page_title="Emotion Recognition", page_icon="😊")

st.title("😊 Emotion Recognition System")
st.write("Upload a face image to predict the emotion.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Show uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict Emotion"):
        try:
            files = {
                "file": uploaded_file.getvalue()
            }

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                files=files
            )

            if response.status_code == 200:
                result = response.json()

                st.success(f"Predicted Emotion: {result['emotion']}")
                st.info(f"Confidence: {result['confidence']}")
            else:
                st.error("Prediction API failed.")

        except Exception as e:
            st.error(f"Error: {e}")