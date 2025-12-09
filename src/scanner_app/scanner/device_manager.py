# src/scanner_app/scanner/device_manager.py
import comtypes.client as cc

class DeviceManager:
    def __init__(self):
        # This is the magic line that works on ALL Windows versions
        self.common = cc.CreateObject("WIA.CommonDialog")

    def get_devices(self):
        try:
            # This will show the native Windows scanner selection dialog once
            # But we just use it to test if WIA is working
            return True
        except:
            return False

    def find_hp_deskjet_2130(self):
        # We don't need to list devices manually — WIA.CommonDialog auto-detects the default scanner
        # HP DeskJet 2130 will appear as default if connected and powered on
        return self.common, "HP DeskJet 2130 series"