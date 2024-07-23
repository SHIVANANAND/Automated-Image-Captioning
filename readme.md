# Automated Image Captioning

This project provides an automated image captioning service using a deep learning model. The application is built with TensorFlow for model handling and Streamlit for the web interface.

You can upload an image and get a caption generated by the model.

## Deployed Application

Check out the deployed application: [Automated Image Captioning](https://automated-image-captioning.streamlit.app/)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

## Project Structure

- `app.py`: Main application file for Streamlit.
- `requirements.txt`: List of Python packages required for the project.
- `tokenizer.pkl`: Pre-trained tokenizer.
- `best_model.h5`: Pre-trained image captioning model.

## Usage

1. Upload an image using the "Choose an image..." button.
2. The application will display the uploaded image.
3. A caption will be generated and displayed below the image.

## Contributors
[SHIVAN ANAND](https://github.com/SHIVANANAND) <BR>
[ANIRUDH SHUKLA](https://github.com/Anirudh-Shukla) <BR>
[GAURAV KUMAR CHAURASIYA](https://github.com/gauravkumarchaurasiya) <BR>

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Acknowledgements

- TensorFlow
- Streamlit
- VGG16 model from Keras applications
