import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

# Configuration
TECH_STACK = [
    "python", "django", "wordpress", "postgresql", 
    "azure", "aws", "react", "nodejs", "mongodb",
    "docker", "kubernetes", "terraform", "ansible"
]
ICON_SIZE = "64"  # 16, 24, 32, 48, 64, 128, 256, 512
OUTPUT_DIR = "assets/images/icons"

def download_icon(tech):
    base_url = "https://skillicons.dev/icons"
    url = f"{base_url}?i={tech}&theme=light"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, f"{tech}.svg")
        
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {tech} icon")
    except Exception as e:
        print(f"Failed to download {tech} icon: {e}")

def main():
    print(f"Downloading {len(TECH_STACK)} tech icons to {OUTPUT_DIR}")
    
    # Use threading to download icons faster
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_icon, TECH_STACK)
    
    print("Icon download complete")

if __name__ == "__main__":
    main()