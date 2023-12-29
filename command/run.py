from button import Button
from receptor import Receptor
from commands import ButtonCommand

receptor = Receptor()
button = Button()

button.set_command(ButtonCommand(receptor, {"Resposta": "OK"}))
button.action()
