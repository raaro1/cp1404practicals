from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabel(App):
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root