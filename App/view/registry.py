import flet

# history of all the tickets opened
class registry(flet.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return flet.Text("Registry")