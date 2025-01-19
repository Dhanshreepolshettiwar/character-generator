# character-generator
AI Film Production Tool
Problem Statement
Filmmaking teams often struggle to align their creative visions during pre-production. Miscommunication and inefficiencies slow down progress and increase costs. This tool helps by turning scripts and character ideas into clear visuals and summaries, making collaboration smoother and more efficient.

Project Overview
This tool simplifies pre-production by converting written ideas into:
Scene Summaries: Brief breakdowns of key story points.
Character Bios: Rich backstories and motivations for characters.
Image Visuals: AI-generated images to represent scenes or characters visually.
Storyboarding: Visualizing the sequence of scenes with AI-generated images for easy flow and continuity.
An interactive platform bridges the gap between writers, directors, and producers, making the entire pre-production process more efficient.

Technologies Used
Backend:
WorqHat API: For analyzing scripts and generating text outputs (e.g., scene summaries and character bios).
Stable Diffusion (Diffusers): For creating high-quality AI-generated image visuals from text descriptions.
Frontend:
Streamlit: For building a user-friendly web interface to interact with the tool.
Hosting:
Streamlit Cloud: For easy deployment and sharing of the tool.

Setup Instructions
Prerequisites:
Install Python 3.8 or higher.
Install required libraries:
 pip install worqhat streamlit diffusers torch pillow moviepy
Get your WorqHat API key and configure it:
 export WORQHAT_API_KEY=your_key_here
Code Implementation
Script Analysis
 Summarize scripts into key scenes:
import requests
# Define your Worqhat API key
api_key = "sk-e95304071474418ca01507367e72fc60"
# Define the endpoint URL
url = "https://api.worqhat.com/v1/completions"
# Define the headers with the API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
# Define the story generation function
def generate_story(prompt):
    payload = {
        "model": "text-davinci-003",  # Use your desired model from Worqhat
        "prompt": prompt,
        "max_tokens": 250,  # Adjust the length of the story
        "temperature": 0.7,  # Controls randomness
    }
    # Send the POST request to the Worqhat API
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['text'].strip()
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example usage
description = "futuristic city from future"
story_prompt = f"Write a short story about a {description}."
story = generate_story(story_prompt)

# Print the generated story
print("Generated Story:")
print(story)


Character Bio Generation
 Create detailed biographies from character descriptions:
def generate_character_bio(character_description):
    payload = {
        "model": "text-davinci-003",
        "prompt": f"Generate a biography for this character:\n{character_description}",
        "max_tokens": 250,
    }
    response = requests.post("https://api.worqhat.com/v1/completions", json=payload, headers=headers)
    return response.json()["choices"][0]["text"]

Image Generation
 Produce visuals from scene or character descriptions using Stable Diffusion:
from diffusers import StableDiffusionPipeline
from PIL import Image  # To display the image inline in Colab

# Load the Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("cuda")  # Use "cpu" if GPU is unavailable

# Generate an image
description = "futuristic city from future"
image = pipe(description).images[0]

# Display the image inline
image.show()  # This will not work in Colab, so replace it with the code below
display(image)  # Use this to display the image inline in Colab

Interactive Frontend
Streamlit App
import streamlit as st

st.title("AI Film Production Tool")
st.subheader("Streamline Pre-Production")

# Script Input
script_text = st.text_area("Enter your script:")

if st.button("Generate Summary"):
    if script_text:
        summary = summarize_script(script_text)
        st.subheader("Scene Summary")
        st.write(summary)
    else:
        st.error("Please enter a script!")

# Character Input
character_traits = st.text_input("Enter character traits:")
if st.button("Generate Character Bio"):
    if character_traits:
        bio = generate_character_bio(character_traits)
        st.subheader("Character Biography")
        st.write(bio)
    else:
        st.error("Please enter character traits!")

# Visual Generation
visual_description = st.text_input("Enter a scene or character description for visuals:")
if st.button("Generate Visual"):
    if visual_description:
        image = generate_visual(visual_description)
        st.image(image, caption="Generated Visual")
    else:
        st.error("Please enter a description!")

Running Locally
 Run the application:
streamlit run app.py


Deployment
Deploy your project on Streamlit Cloud:
Push your code to a GitHub repository.
Link the repository to Streamlit Cloud and deploy it.

Usage Example
Input:
Script: A group of adventurers explores a magical forest.
Character: A brave knight with a mysterious past.
Visual: A magical forest glowing under moonlight.
Output:
Scene Summary: Key moments from the forest adventure.
Character Bio: The knight's backstory and motivations.
Image Visual: A generated image of the glowing forest.

Future Enhancements
Real-Time Collaboration: Add real-time feedback features for team collaboration.
Animation & Storyboarding Integration: Expand integration with animation and advanced storyboarding tools.
Storyboarding: Allow users to sequence generated visuals into a storyboard for a complete visual flow of the film.
This tool aims to streamline the creative process, making collaboration easier while bringing ideas to life and simplifying the pre-production phase for filmmakers.

