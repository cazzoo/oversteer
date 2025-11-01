from .device import Device
from evdev import ecodes

class T500RS(Device):
    def get_autocenter(self):
        return 0

    def set_autocenter(self, autocenter):
        input_device = self.get_input_device()
        input_device.write(ecodes.EV_FF, ecodes.FF_AUTOCENTER, int(autocenter))
        return True

    def get_spring_level(self):
        path = self.checked_device_file("spring_level")
        if not path:
            return 0
        with open(path, "r") as file:
            data = file.read()
        level = data.strip()
        return int(level)

    def set_spring_level(self, level):
        path = self.checked_device_file("spring_level")
        if not path:
            return False
        level = str(level)
        with open(path, "w") as file:
            file.write(level)
        return True

    def get_damper_level(self):
        path = self.checked_device_file("damper_level")
        if not path:
            return 0
        with open(path, "r") as file:
            data = file.read()
        level = data.strip()
        return int(level)

    def set_damper_level(self, level):
        path = self.checked_device_file("damper_level")
        if not path:
            return False
        level = str(level)
        with open(path, "w") as file:
            file.write(level)
        return True

    def get_friction_level(self):
        path = self.checked_device_file("friction_level")
        if not path:
            return 0
        with open(path, "r") as file:
            data = file.read()
        level = data.strip()
        return int(level)

    def set_friction_level(self, level):
        path = self.checked_device_file("friction_level")
        if not path:
            return False
        level = str(level)
        with open(path, "w") as file:
            file.write(level)
        return True
