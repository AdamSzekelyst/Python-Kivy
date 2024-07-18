import pyautogui
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from pynput import mouse
from PIL import ImageGrab
from time import sleep
from pynput.keyboard import Listener, KeyCode
from kivy.config import Config

# Set the size and properties of the Kivy window
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '550')
Config.set('graphics', 'resizable', '0')

# Kivy string for the layout and UI elements
kv_string = """
<Button>:
    font_size: 17
    size_hint: 0.3, 0.1
    border: 0.1, 0.1, 0.1, 0.1
    background_color: 0, 0.6, 1, 1

<CyberStrikeLayout>:
    canvas:
        Rectangle:
            source: "Warrior_Male.png"
            size: 272, 360
            pos: 185, -50
        Rectangle:
            source: "discord.png"
            size: 45, 45
            pos: 7, 7

    Slider:
        id: Slider
        orientation: "horizontal"
        min: 0.001
        max: 2
        pos_hint: {'y':0.45}
        value: root.delay
        on_value: root.slide_it(*args)
        
    Label:
        text: "Delay(sec): " + str(Slider.value)
        font_size: 20
        pos_hint: {'y':0.39}
        
    Button:
        text: "Csere"
        pos_hint: {'x':0.02, 'y':0.7}
        on_release: root.CSbutton_release()
    TextInput:
        id: CSdisplay
        text: "Add meg a helyét!"
        readonly: True
        background_color: 1, 1, 1, 1
        foreground_color: 0, 0, 0, 1
        font_size: 18
        multiline: False
        size_hint: 0.65, 0.1
        border: 0.1, 0.1, 0.1, 0.1
        pos_hint: {'x':0.33, 'y':0.7}
        
    Button:
        text: "Bónuszok"
        pos_hint: {'x':0.02, 'y':0.59}
        on_release: root.Bbutton_release()
    TextInput:
        id: Bdisplay
        text: "Add meg a helyét!"
        readonly: True
        background_color: 1, 1, 1, 1
        foreground_color: 0, 0, 0, 1
        font_size: 18
        multiline: False
        size_hint: 0.65, 0.1
        border: 0.1, 0.1, 0.1, 0.1
        pos_hint: {'x':0.33, 'y':0.59}
        
    Button:
        text: "START"
        pos_hint: {"x":0.34, "y":0.47}
        on_release: root.Start_release()
        
    Label:
        text: "rgb(125, 168, 129)"
        font_size: 20
        pos_hint: {'x':-0.21, 'y':-0.2}
        color: 0,1, 0.2, 1
        
    Label:
        text: "rgb(231, 231, 2)"
        font_size: 20
        pos_hint: {'x':-0.21, 'y':-0.25}
        color: 1, 1, 0.2, 1
        
    TextInput:
        text: "Ádám#7368"
        readonly: True
        background_color: 1, 1, 1, 1
        foreground_color: 0, 0, 0, 1
        font_size: 27
        multiline: False
        size_hint: 0.4, 0.078
        border: 0.1, 0.1, 0.1, 0.1
        pos_hint: {'x':0.13, 'y':0.015}
"""

# Load the Kivy string
Builder.load_string(kv_string)

# Main class for the layout of the app
class CyberStrikeLayout(FloatLayout):

    delay = 1 # Default delay value
    Bcolor = "" # Variable to store color at the B location
    Bcoordinates = "" # Variable to store coordinates of the B location

    def slide_it(self, *args):
        # Update the delay based on the slider value
        global delay
        delay = float(args[1])
        print(delay)

    def Bbutton_release(self):
        # Function to capture the coordinates and color at the B location when the button is clicked

        def checkColor(x, y):
            # Function to get the color at the specified coordinates
            global Bcoordinates
            Bcoordinates = str(x) + ":" + str(y)
            bbox = (x, y, x + 1, y + 1)
            im = ImageGrab.grab(bbox=bbox)
            rgbim = im.convert('RGB')
            r, g, b = rgbim.getpixel((0, 0))
            global Bcolor
            Bcolor = f'rgb{(r, g, b)}'

        def onClick(x, y, button, pressed):
            # Mouse listener callback to capture the coordinates and stop the listener
            if pressed and button == mouse.Button.left:
                checkColor(x, y)
                mlstnr.stop()

        if __name__ == '__main__':
            # Clear the display text and start the mouse listener
            self.ids["Bdisplay"].text = ""
            with mouse.Listener(on_click=onClick) as mlstnr:
                mlstnr.join()
            # Display the captured color and coordinates
            print(Bcolor)
            print(Bcoordinates)
            self.ids["Bdisplay"].text += Bcolor + " " + Bcoordinates

    CScoordinates = "" # Variable to store coordinates of the CS location

    def CSbutton_release(self):
        # Function to capture the coordinates at the CS location when the button is clicked

        def onClick(x, y, button, pressed):
            # Mouse listener callback to capture the coordinates and stop the listener
            if pressed and button == mouse.Button.left:
                global CScoordinates
                CScoordinates = str(x) + ":" + str(y)
                mlstnr.stop()

        if __name__ == '__main__':
            # Clear the display text and start the mouse listener
            self.ids["CSdisplay"].text = ""
            with mouse.Listener(on_click=onClick) as mlstnr:
                mlstnr.join()
            # Display the captured coordinates
            print(CScoordinates)
            self.ids["CSdisplay"].text += CScoordinates

    def Start_release(self):
        # Function to start the main action when the START button is pressed

        start_key = KeyCode(char='a') # Define the key to start the action

        def on_press(key):
            # Callback for key press listener
            if key == start_key:
                current_color = ""
                i = 0
                while current_color != "rgb(231, 231, 2)" and i < 400:
                    # Main loop to perform actions until the specified color is found or max iterations reached
                    global CScoordinates
                    Clist = CScoordinates.strip().split(":")
                    pyautogui.moveTo(int(Clist[0]), int(Clist[1]))
                    pyautogui.click()
                    sleep(delay)

                    global Bcoordinates
                    Blist = Bcoordinates.strip().split(":")
                    pyautogui.moveTo(int(Blist[0]), int(Blist[1]))
                    pyautogui.click()

                    bbox = (int(Blist[0]), int(Blist[1]), int(Blist[0]) + 1, int(Blist[1]) + 1)
                    im = ImageGrab.grab(bbox=bbox)
                    rgbim = im.convert('RGB')
                    r, g, b = rgbim.getpixel((0, 0))
                    print(f'rgb{(r, g, b)}')
                    current_color = f'rgb{(r, g, b)}'
                    i += 1
                    print(i)
                    sleep(delay)

                listener.stop() # Stop the key listener

        with Listener(on_press=on_press) as listener:
           listener.join()

# Main class for the Kivy app
class CyberStrikeApp(App):
    def build(self):
        return CyberStrikeLayout()

# Entry point of the program
def main():
    CyberStrikeApp().run()

if __name__=="__main__":
    main()