# src/scanner_app/scanner/scanner_manager.py
from PIL import Image
import io
import array

class ScannerManager:
    def scan(self, wia_common_dialog):
        try:
            # Show native Windows scan dialog
            wia_image = wia_common_dialog.ShowAcquireImage()

            if wia_image is None:
                return None

            # Get the binary data correctly (this works on ALL Windows versions)
            filedata = wia_image.FileData
            binary_data = filedata.BinaryData

            # The real fix: WIA returns an array of integers → convert to bytes
            if isinstance(binary_data, (tuple, list, array.array)):
                binary_data = bytes(binary_data)

            # Open with PIL
            return Image.open(io.BytesIO(binary_data)).convert("RGB")

        except Exception as e:
            print(f"Scan error: {e}")
            return None