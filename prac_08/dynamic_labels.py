from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabel(App):
    """Dynamic adds labels to a Label widget"""

    def __init__(self, **kwargs):
        """Initialize the list of names """
        super().__init__(**kwargs)
        self.names = ["Roi","Crispin","Cody", "Thaedyn", "Ethann"]

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.make_labels()
        return self.root

    def make_labels(self):
        """Makes the labels and dynamically updates them"""
        for name in self.names:
            dynamic_label = Label(text=name)
            self.root.ids.main.add_widget(dynamic_label)

DynamicLabel().run()