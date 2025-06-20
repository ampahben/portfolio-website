from PIL import Image, ImageDraw, ImageFont
import os
import json

# Configuration
PROJECTS_FILE = "assets/data/projects.json"
OUTPUT_DIR = "assets/images/projects"
FONT_PATH = "arial.ttf"  # Change to your font path
IMAGE_SIZE = (600, 400)
COLORS = {
    "cloud": "#E0F7F2",
    "cybersecurity": "#F2F7E0",
    "web": "#E8F4FD"
}

def generate_image(category, title, filename):
    # Create blank image
    img = Image.new('RGB', IMAGE_SIZE, color=COLORS[category])
    draw = ImageDraw.Draw(img)
    
    # Add text
    try:
        font = ImageFont.truetype(FONT_PATH, 24)
    except:
        font = ImageFont.load_default()
    
    text = f"{title}\n{category.capitalize()} Project"
    draw.text((IMAGE_SIZE[0]//2, IMAGE_SIZE[1]//2), text, 
              font=font, fill="black", anchor="mm", align="center")
    
    # Save image
    os.makedirs(os.path.join(OUTPUT_DIR, category), exist_ok=True)
    img.save(os.path.join(OUTPUT_DIR, category, filename))
    print(f"Generated image for {title}")

def main():
    # Load projects data
    with open(PROJECTS_FILE) as f:
        projects = json.load(f)
    
    # Generate images for all projects
    for category in projects:
        for project in projects[category]:
            image_name = f"{project['id']}-{project['title'].lower().replace(' ', '-')}.jpg"
            generate_image(category, project['title'], image_name)
    
    print("Project image generation complete")

if __name__ == "__main__":
    main()