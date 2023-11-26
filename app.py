from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os

# Load the OpenAI API key from the environment variable
open_ai_key = os.getenv('open_ai_key')

# Initialize the OpenAI client
client = OpenAI(api_key=open_ai_key)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form['movie_name']

    # Construct the prompt for the OpenAI API
    prompt = f"Recommend me a movie similar to '{movie_name}' and tell me why this recommedation also give me some details of the cast and genre of the movie "

    # Send the prompt to the OpenAI API and receive the response
    response = client.completions.create(
        model="text-davinci-003",
        #engine="text-davinci-003",  # Use the specified model "davinci-003"
        prompt=prompt,
        max_tokens=100,
    )

    # Extract the recommended movie from the response
    recommended_movie = response.choices[0].text.strip()

    # Pass the movie name and recommended movie to the template for rendering
    return render_template('index.html', movie_name=movie_name, recommended_movie=recommended_movie)

if __name__ == '__main__':
    app.run(debug=True)
