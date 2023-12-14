from flask import Flask, render_template, request, jsonify
import numpy as np
from ml_model_svm import SVMModel
from flask_cors import CORS
from pydub import AudioSegment
app = Flask(__name__)
CORS(app)
# Create instances of the models
svm_model = SVMModel()




def extract_features_from_audio_file(audio_file):
    # Load the audio file
    audio = AudioSegment.from_file(audio_file)

    # Convert stereo to mono
    audio = audio.set_channels(1)

    # Convert to numpy array
    audio_array = np.array(audio.get_array_of_samples())

    # Sample rate (replace with the actual sample rate of your audio)
    sample_rate = audio.frame_rate

    # Extract features (replace this with your actual feature extraction code)
    # Example: you can use numpy to calculate the mean and standard deviation of the first 57 samples
    mean_amplitude = np.mean(audio_array[:57])
    std_amplitude = np.std(audio_array[:57])

    # Create a feature vector with 57 features
    features = [mean_amplitude, std_amplitude] + list(audio_array[:55])

    # Reshape the features to a 2D array with one row
    features = np.array(features).reshape(1, -1)

    return features


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/svm_service', methods=['GET', 'POST'])
def svm_service():
    try:
        print("Request received.")  # Debug print

        # Check if the request contains a file
        if 'audio_file' in request.files:
            audio_file = request.files['audio_file']
            
            print("Audio file received.")  # Debug print

            # Process the audio file and extract features
            # (Replace this with your actual code for feature extraction)
            audio_features = extract_features_from_audio_file(audio_file)
            print("Audio features extracted.")  # Debug print

            # Use the extracted features for genre classification
            prediction = svm_model.classify_genre(audio_features)
            print("Prediction:", prediction)  # Debug print
	
            return jsonify({'genre_prediction': prediction})
        else:
            return jsonify({'error': 'No audio file uploaded.'}), 400  # Return a 400 status code for bad request

    except Exception as e:
        print(f"An error occurred: {str(e)}")  # Debug print
        return jsonify({'error': str(e)}), 500  # Return a 500 status code for internal server errors

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
