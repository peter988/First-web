import fitz  # PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        text = doc[page_num].get_text("text")
        oem_number = extract_oem_number(text)
        
        for img_index, img in enumerate(doc[page_num].get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            image_filename = f"{page_num + 1}_img_{img_index + 1}.jpg"
            image_path = os.path.join(output_folder, image_filename)
            
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)
            print(f"Extracted: {image_path}")

def extract_oem_number(text):
    import re
    match = re.search(r"\b[A-Z0-9]{6,}\b", text)
    return match.group(0) if match else "unknown"

pdf_path = "DK0823110803-1-Final Invoice(With Application) (2).pdf"
output_folder = "extracted_images3"
extract_images_from_pdf(pdf_path, output_folder)