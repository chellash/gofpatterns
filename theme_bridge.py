class ThemeImplementation:
    def background_color(self):
        pass

    def font_color(self):
        pass

class Light(ThemeImplementation):
    def background_color(self):
        return "#FFFFFF"

    def font_color(self):
        return "#000000"

class Dark(ThemeImplementation):
    def background_color(self):
        return "#000000"

    def font_color(self):
        return "#FFFFFF"

class Custom(ThemeImplementation):
    def __init__(self, background_color, font_color):
        self.background_color = background_color
        self.font_color = font_color

    def background_color(self):
        return self.background_color

    def font_color(self):
        return self.font_color

class Theme:
    def __init__(self, implementation):
        self.implementation = implementation

    def background_color(self):
        return self.implementation.background_color()

    def font_color(self):
        return self.implementation.font_color()

# Usage
light = Theme(Light())
dark = Theme(Dark())
custom = Theme(Custom("#555555", "#EEEEEE"))

print("Light theme background color:", light.background_color()) # Light theme background color: #FFFFFF
print("Dark theme font color:", dark.font_color()) # Dark theme font color: #FFFFFF
print("Custom theme background color:", custom.background_color()) # Custom theme background color: #555555