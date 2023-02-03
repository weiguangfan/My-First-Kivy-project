import kivy
from kivy.event import EventDispatcher
from kivy.properties import NumericProperty


# class MyClass(object):
#     def __init__(self):
#         super(MyClass, self).__init__()
#         self.numeric_var = 1


class MyClass(EventDispatcher):
    numeric_var = NumericProperty(1)

    def on_touch_down(self, touch):
        if super().on_touch_down(touch):
            return True
        if not self.collide_point(touch.x, touch.y):
            return False
        print('you touched me!')
        return True
