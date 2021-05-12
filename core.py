from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# ///////////////////////////////////////
#studing 1
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
# studing 2


class Cube(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 30,
            texture = 'white_cube',
            color = color.white,
            highlight_color = color.red
        )
    def input(self, key):
        # если нажали любую кнопку
        if self.hovered:
            if key == 'right mouse down':
                cube = Cube(self.position + mouse.normal)
            if key == 'left mouse down':
                destroy(self)

app = Ursina()

#cube = Cube()

for z in range(16):
    for x in range(16):
        cube = Cube((x,0,z))

player = FirstPersonController()

app.run()
app.run()