# src/scanner_app/ui/main_window.py
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from scanner_app.scanner.device_manager import DeviceManager
from scanner_app.scanner.scanner_manager import ScannerManager
from scanner_app.utils.session_manager import SessionManager
from scanner_app.utils.file_exporter import FileExporter
from scanner_app.ui.components import ImageThumbnail


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Scanner App")

        self.device_manager = DeviceManager()
        self.scanner_manager = ScannerManager()
        self.session_manager = SessionManager()
        self.file_exporter = FileExporter()

        self.wia_dialog = self.device_manager.common          # <-- the working WIA object
        self.scanner_name = "HP DeskJet 2130 series"

        self.export_path = tk.StringVar(value=".")
        self.filename = tk.StringVar(value="scanned.pdf")

        self._build_ui()
        self.refresh_scanner_status()

    def _build_ui(self):
        # 1. Configure Printer
        printer_frame = tk.Frame(self.root)
        printer_frame.pack(pady=10)

        tk.Label(printer_frame, text="Printer:").pack(side=tk.LEFT)
        self.printer_label = tk.Label(printer_frame, text=self.scanner_name)
        self.printer_label.pack(side=tk.LEFT, padx=10)
        self.status_label = tk.Label(printer_frame, text="Status: Checking…", fg="orange")
        self.status_label.pack(side=tk.LEFT, padx=10)
        tk.Button(printer_frame, text="Refresh", command=self.refresh_scanner_status).pack(side=tk.LEFT)

        # 2. Export Path
        path_frame = tk.Frame(self.root)
        path_frame.pack(pady=10)

        tk.Label(path_frame, text="Export Path:").pack(side=tk.LEFT)
        tk.Entry(path_frame, textvariable=self.export_path, width=50).pack(side=tk.LEFT, padx=10)
        tk.Button(path_frame, text="Browse", command=self.browse_export_path).pack(side=tk.LEFT)

        # 3. Filename
        filename_frame = tk.Frame(self.root)
        filename_frame.pack(pady=10)

        tk.Label(filename_frame, text="Filename:").pack(side=tk.LEFT)
        tk.Entry(filename_frame, textvariable=self.filename, width=30).pack(side=tk.LEFT, padx=10)
        tk.Label(filename_frame, text=".pdf").pack(side=tk.LEFT)

        # 4. Scan Button
        tk.Button(self.root, text="Scan", font=("Arial", 12), height=2, command=self.scan_document).pack(pady=15)

        # 5. Scanned Images Container
        self.images_container = tk.Frame(self.root)
        self.images_container.pack(pady=10, fill=tk.X)

        # 6. Reset Session
        tk.Button(self.root, text="Reset Session", command=self.reset_session).pack(pady=5)

        # 7. Export PDF
        tk.Button(self.root, text="Export PDF", font=("Arial", 12), bg="#4CAF50", fg="white",
                  command=self.export_pdf).pack(pady=15)

    def refresh_scanner_status(self):
        # With the CommonDialog approach the scanner is always considered "available" if WIA works
        self.status_label.config(text="Online", fg="green")
        self.printer_label.config(text=self.scanner_name)

    def check_printer_status(self):
        self.refresh_scanner_status()

    def browse_export_path(self):
        path = filedialog.askdirectory()
        if path:
            self.export_path.set(path)

    def scan_document(self):
        self.root.config(cursor="watch")
        self.root.update()

        image = self.scanner_manager.scan(self.wia_dialog)

        self.root.config(cursor="")
        if image:
            self.session_manager.add_image(image)
            self.display_scanned_images()
        else:
            messagebox.showwarning("Scan cancelled", "No image was scanned (user cancelled or no paper).")

    def display_scanned_images(self):
        for widget in self.images_container.winfo_children():
            widget.destroy()

        for idx, img in enumerate(self.session_manager.get_images()):
            thumb = ImageThumbnail(self.images_container, img, idx)
            thumb.pack(side=tk.LEFT, padx=5, pady=5)

    def reset_session(self):
        self.session_manager.clear_images()
        for widget in self.images_container.winfo_children():
            widget.destroy()

    def export_pdf(self):
        images = self.session_manager.get_images()
        if not images:
            messagebox.showwarning("Warning", "No images to export.")
            return

        path = self.export_path.get()
        filename = self.filename.get()
        if not filename.endswith(".pdf"):
            filename += ".pdf"

        success = self.file_exporter.export_to_pdf(images, path, filename)
        if success:
            messagebox.showinfo("Success", f"PDF saved as:\n{path}\\{filename}")
        else:
            messagebox.showerror("Error", "Failed to create PDF.")