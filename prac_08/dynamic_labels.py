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

    def create_labels(self):
        """Create the labels and dynamically updates them"""
        for name in self.names:
            dynamic_label = DynamicLabel(text=name)
            self.root.ids.main.add_widget(dynmaic_label)

DynamicLabel().run()