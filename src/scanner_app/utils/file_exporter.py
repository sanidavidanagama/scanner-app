# scanner_app/src/scanner_app/utils/file_exporter.py
from PIL import Image
import os

class FileExporter:
    def export_to_pdf(self, images, path, filename):
        try:
            full_path = os.path.join(path, filename)
            rgb_images = [img.convert('RGB') for img in images]
            rgb_images[0].save(full_path, save_all=True, append_images=rgb_images[1:])
            return True
        except Exception as e:
            print(f"Export error: {e}")
            return False