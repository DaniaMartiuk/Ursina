from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

# загрузка текстур
grass_block = load_texture('assets/grass_block.png')
dirt_block = load_texture('assets/dirt_block.png')
stone_block = load_texture('assets/stone_block.png')
brick_block= load_texture('assets/brick_block.png')
sky_t = load_texture('assets/skybox.png')
block = grass_block

def update():
    global block
    if held_keys['1']:
        block = grass_block
    if held_keys['2']:
        block = dirt_block
    if held_keys['3']:
        block = stone_block
    if held_keys['4']:
        block = brick_block


# ///////////////////////////////////////
# class Test_Qube(Entity):
#     def __init__(self):
#         super().__init__(
#             model = 'cube',
#             color = color.white,
#             texture = 'white_cube',
#             rotation = Vec3(45,45,45)
#         )
#
# app = Ursina()
#
# def update():
#     # передвижение по координате X
#     # sq.x += 0.1
#
#     # Время между кадрами
#     # print("Time DT: ", time.dt)
#
#     # если кнопка нажата held_keys['любая кнопка'] то передвигаемся
#     # if held_keys['a']:
#     #     sq.x -= 0.5
#     # if held_keys['d']:
#     #     sq.x += 0.5
#     # if held_keys['s']:
#     #     sq.y -= 0.5
#     # if held_keys['w']:
#     #     sq.y += 0.5
#
#     #Прокрутка куба на месте
#     if held_keys['a']:
#         sq.rotation_y -= 0.5
#     if held_keys['d']:
#         sq.rotation_y += 0.5
#     if held_keys['s']:
#         sq.rotation_x -= 0.5
#     if held_keys['w']:
#         sq.rotation_x += 0.5
#
# # ////////////////////////////////////////////
# # Название окна с игрой
# window.title = 'Test Game'
#
# # Белая линия для закрития приложения
# window.borderless = False
#
# #Полний екран
# window.fullscreen = False
#
# # Доп кнопка для закрития окна
# window.exit_button.visible = False
#
# # Видимость ФПС
# window.fps_counter.enable = True
# # ////////////////////////////////////////////
# # Создание квадрата
# sq = Test_Qube()
#
# app.run()
# //////////////////////////////////////////////////////////////////

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_t,
            scale=300,
            double_sided=True
        )


class Cube(Button):
    def __init__(self, position = (0,0,0),block_t = grass_block):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = block_t,
            scale = 0.5,
            color = color.white,
            highlight_color = color.white
        )
    def input(self, key):
        # если нажали любую кнопку
        if self.hovered:
            if key == 'right mouse down':
                cube = Cube(self.position + mouse.normal,block)
            if key == 'left mouse down':
                destroy(self)


for z in range(16):
    for x in range(16):
        cube = Cube((x,0,z))

player = FirstPersonController()
sky = Sky()
app.run()