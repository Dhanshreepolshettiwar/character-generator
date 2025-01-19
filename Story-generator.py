from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
model_name = "gpt2"  # You can use other models like 'gpt2-medium', 'gpt2-large', etc.
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Function to generate a story
def generate_story(prompt, max_length=200):
    # Encode the prompt text to tensor
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    
    # Generate the story using the model
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.9, temperature=0.7)
    
    # Decode and return the generated text
    story = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return story

# Example prompt for generating a story
prompt = "Once upon a time in a futuristic city, there lived a robot named Zeta who dreamed of exploring the stars."

# Generate a story
generated_story = generate_story(prompt)

# Print the generated story
print("Generated Story:")
print(generated_story)
