# scanner_app/src/scanner_app/utils/session_manager.py
class SessionManager:
    def __init__(self):
        self.images = []

    def add_image(self, image):
        self.images.append(image)

    def get_images(self):
        return self.images

    def clear_images(self):
        self.images = []