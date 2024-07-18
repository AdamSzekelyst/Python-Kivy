import os

# Disable Kivy console logging
os.environ['KIVY_NO_CONSOLELOG'] = "1"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Define the KV language string for UI layout
kv_string = """
<Button>:
    size_hint: 1/4, 1/5
    font_size: 20

<CalculatorLayout>:
    orientation: "vertical"
    padding: 4
    TextInput:
        id: display
        text: ""
        readonly: True
        foreground_color: 1, 1, 1, 1
        background_color: 0, 0, 0, 1
        font_size: 50
        multiline: False
        size_hint: 1, 1/8
    
    StackLayout:
        orientation: "lr-bt"
        spacing: 2
        Button:
            text: "0"
            on_press: root.button_pressed(self)
        Button:
            text: "="
            background_color: 0.4, 0.45, 0.44, 1
            on_press: root.calculate()
        Button:
            text: "."
            on_press: root.button_pressed(self)
        Button:
            text: "+"
            on_press: root.button_pressed(self)
        Button:
            text: "1"
            on_press: root.button_pressed(self)
        Button:
            text: "2"
            on_press: root.button_pressed(self)
        Button:
            text: "3"
            on_press: root.button_pressed(self)
        Button:
            text: "-"
            on_press: root.button_pressed(self)
        Button:
            text: "4"
            on_press: root.button_pressed(self)
        Button:
            text: "5"
            on_press: root.button_pressed(self)
        Button:
            text: "6"
            on_press: root.button_pressed(self)
        Button:
            text: "*"
            on_press: root.button_pressed(self)
        Button:
            text: "7"
            on_press: root.button_pressed(self)
        Button:
            text: "8"
            on_press: root.button_pressed(self)
        Button:
            text: "9"
            on_press: root.button_pressed(self)
        Button:
            text: "/"
            on_press: root.button_pressed(self)
        Button:
            text: "clear"
            size_hint: 1, 1/10
            on_press: display.text = ""
"""

# Load the KV string
Builder.load_string(kv_string)

# Define the CalculatorLayout class inheriting from BoxLayout
class CalculatorLayout(BoxLayout):

    # Flag to indicate if the display should be cleared
    clear = False

    # Method to evaluate and display the result of the expression
    def calculate(self):
        expression = self.ids["display"].text

        try:
            # Evaluate the mathematical expression
            exp = str(eval(expression))
        except:
            # Handle invalid expressions
            exp = "Invalid operation"
            self.clear = True

        # Update the display with the result or error message
        self.ids["display"].text = exp

    # Method to handle button presses
    def button_pressed(self, btn):
        if self.clear:
            # Clear the display if the previous operation was invalid
            self.ids["display"].text = ""
            self.clear = False

        # Append the pressed button's text to the display
        text = btn.text
        self.ids["display"].text += text

# Define the CalculatorApp class inheriting from App
class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

# Run the application
if __name__ == '__main__':
    CalculatorApp().run()