from ai.image_generation import generate_image

prompt = "A cute robot painting a sunset, digital art"

output_path = generate_image(prompt)

print(f"Image saved to {output_path}")
