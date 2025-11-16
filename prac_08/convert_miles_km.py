from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class ConvertMilesKm(App):
    """An App that converts miles to kilometers"""
    message = StringProperty

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment_change(self, instance, value):

    def handle_calculation(self):
        ...
ConvertMilesKm().run()