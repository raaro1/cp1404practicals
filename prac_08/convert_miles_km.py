from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_VALUE = 1.60934

class ConvertMilesKm(App):
    """An App that converts miles to kilometers"""
    output_text = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment_change(self,increment):
        """Handles when up and down button is used"""
        try:
            value = float(self.root.ids.user_input.text)
            value += increment
            self.root.ids.user_input.text = str(value)
        except ValueError:
            value = 0
            value += increment
            self.root.ids.user_input.text = str(value)

    def handle_convert_input(self, value):
        """Handles converting then input in miles"""
        try:
            result = float(value) * CONVERSION_VALUE
            self.output_text = str(result)
        except ValueError:
            self.output_text = "0.0"


ConvertMilesKm().run()