import arcade
from mario import MyGame


window = MyGame(10,25)
window.setup()


#Pruebas con las teclas "WASD"
def test_w():
    assert window.on_key_press(arcade.key.W,None) == "arriba"
    
def test_s():
    assert window.on_key_press(arcade.key.S,None) == "abajo"

def test_a():
    assert window.on_key_press(arcade.key.A,None) == "izquierda"

def test_d():
    assert window.on_key_press(arcade.key.D,None) == "derecha"

        		
