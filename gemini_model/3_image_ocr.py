from ai.image_ocr import summarize_image_to_json

image_path = "./image_2.png"

summary = summarize_image_to_json(image_path)

print(summary)
