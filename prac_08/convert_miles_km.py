from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class ConvertMilesKm(App):
    """An App that converts miles to kilometers"""
    output_text = StringProperty

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment_change(self,increment):
        value = float(self.root.ids.user_input.text)
        value += increment
        self.root.ids.user_input.text = str(value)

    def handle_convert_input(self, value):
        result = float(value) * 1.60934
        self.root.ids.output_label.text = str(result)


ConvertMilesKm().run()