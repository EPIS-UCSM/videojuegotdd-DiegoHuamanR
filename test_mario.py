import arcade
from mario import MyGame


window = MyGame(10,25)
window.setup()
#arcade.run()


#Pruebas con las teclas "WASD"
def test_w():
    assert window.on_key_press(arcade.key.W,None) == "arriba"
    
def test_s():
    assert window.on_key_press(arcade.key.S,None) == "abajo"

def test_a():
    assert window.on_key_press(arcade.key.A,None) == "izquierda"

def test_d():
    assert window.on_key_press(arcade.key.D,None) == "derecha"
#######################################################################################

def obstaculo():
    wall = arcade.Sprite("cylinder.png", CYLINDER_SCALING)
    assert windows.wall_list.append(wall) == "cilindro"

def posicion_obstaculo():
    wall = arcade.Sprite("cylinder.png", CYLINDER_SCALING)
    assert wall.position== [256, 110]

def posicion_obstaculo1():
    wall = arcade.Sprite("cylinder.png", CYLINDER_SCALING)
    assert wall.position== [865, 110]

def posicion_obstaculo2():
    wall = arcade.Sprite("cylinder.png", CYLINDER_SCALING)
    assert wall.position== [3800, 110]

def posicion_obstaculo3():
    wall = arcade.Sprite("cylinder.png", CYLINDER_SCALING)
    assert wall.position== [1200, 110]

    





