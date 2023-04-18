import openai
import os
import random
import string

openai.api_key = "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"
model_engine = "text-davinci-003"  # or any other model ID

# Generate basic physical facts and personal motivations
basic_prompt = "Create a fantasy character who lives in a medieval world and explores dungeons to defeat skeletons and other monsters! Describe the character's race, hair color and style, and personal motivations."
basic_response = openai.Completion.create(
    engine=model_engine,
    prompt=basic_prompt,
    max_tokens=400,
    n=1,
    stop=None,
    temperature=0.55,
)

# Define possible options for character attributes
races = ["Human", "Dwarf", "Elf"]
hair_colors = ["black", "blonde", "brown", "red", "gray"]
hair_styles = ["short", "medium", "long", "curly", "straight"]
motivations = ["glory", "revenge", "riches", "power", "knowledge"]

# Randomly select character attributes
race = random.choice(races)
hair_color = random.choice(hair_colors)
hair_style = random.choice(hair_styles)
motivation = random.choice(motivations)

def generate_word(length):
   """Generate a random word with the specified length."""
   letters = string.ascii_lowercase
   word = ''.join(random.choice(letters) for _ in range(length))
   return word

# Define OpenAI prompt
history_prompt = f"Create a {race.lower()} character with {hair_color} {hair_style} hair. Describe the character's personality and motivations. What adventures has the character been on in their quest for {motivation}? Generate a short story about the character."

history_response = openai.Completion.create(
    engine=model_engine,
    prompt=history_prompt,
    max_tokens=800,
    n=1,
    stop=None,
    temperature=0.6,
)

# Extract information from history response
history = history_response.choices[0].text

# Print results
print(f"Race: {race}")
print(f"Hair Color: {hair_color}")
print(f"Hair Style: {hair_style}")
print(f"Motivations: {', '.join(motivations)}")
print(f"Year-by-Year History:\n{history}")