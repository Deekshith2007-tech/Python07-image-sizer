import os
from PIL import Image

def resize_images(input_folder, output_folder, width, height, output_format="JPEG"):
    # Create output folder if not exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    
    for filename in os.listdir(input_folder):
        try:
            file_path = os.path.join(input_folder, filename)

            
            if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')):
                continue
            
            
            img = Image.open(file_path)

            
            resized_img = img.resize((width, height))

            
            new_filename = os.path.splitext(filename)[0] + "." + output_format.lower()
            save_path = os.path.join(output_folder, new_filename)

            resized_img.save(save_path, output_format)

            print(f"✔ Resized & saved: {save_path}")

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")



input_folder =r"D:\Python internship\image sizer\images"
output_folder =r"D:\Python internship\image sizer\resized_images" 

width = 800  
height = 600 

resize_images(input_folder, output_folder, width, height, output_format="PNG")

print("\n Batch resizing completed!")