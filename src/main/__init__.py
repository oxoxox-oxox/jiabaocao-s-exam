"""
A simple robot simulator on a 2D grid.
"""

from enum import Enum
from typing import Tuple


class Facing(Enum):  # Facing 我们定义为一个枚举类，用于定义方向。如有疑问可以自行 Google / Ask AI
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3


class Grid():
    def __init__(self, width: int, height: int, enemy_pos: tuple):  # DO NOT EDIT THIS METHOD
        self.width: int = width
        self.height: int = height
        self._current_pos: tuple = (0, 0)
        self.current_direction = Facing.UP
        self.enemy_pos: tuple = enemy_pos
        self.position_history: dict = {}  # 用于存储位置历史，键为步数，值为坐标

    @property
    def current_pos(self) -> Tuple[int, int]:
        """
        current_pos 属性的 getter，返回私有属性 _current_pos
        """
        return self._current_pos

    @current_pos.setter
    def current_pos(self, value: Tuple[int, int]) -> None:
        """
        current_pos 属性的 setter（作为第 1 题留空）

        要求：
          - 接受一个长度为 2 的 tuple (x, y)
          - 若传入非 tuple 或长度不为 2，应抛出 TypeError
          - 将 x, y 强制转换为 int ，检查是否超出了宽高范围，如果任何一个超出则将其限制在最大宽高范围即可
          - 处理后存入 self._current_pos
        """

        pass  # TODO: Question 1

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError

        x = int(value[0])
        y = int(value[1])
        if x > self.width:
            x = self.width
        elif x < 0:
            x = 0
        if y > self.height:
            y = self.height
        elif y < 0:
            y = 0
        self._current_pos = (x, y)

    def move_forward(self) -> Tuple[int, int]:  # type: ignore
        '''
        让机器人向当前方向走一格
        返回新的坐标 (x,y) 同时更新成员变量
        利用好上面的 setter
        以右为X轴正方向，上为Y轴正方向
        '''
        pass  # TODO: Question 2

        x = self._current_pos[0]
        y = self._current_pos[1]

        if self.current_direction == Facing.RIGHT:
            new_pos = (x + 1, y)
        elif self.current_direction == Facing.UP:
            new_pos = (x, y + 1)
        elif self.current_direction == Facing.LEFT:
            new_pos = (x - 1, y)
        elif self.current_direction == Facing.DOWN:
            new_pos = (x, y - 1)
        else:
            new_pos = (x, y)

        self.current_pos = new_pos  # 这会调用 setter 进行边界检查
        return self.current_pos

    def turn_left(self) -> Facing:  # type: ignore
        '''
        让机器人逆时针转向
        返回一个新方向 (Facing.UP/DOWN/LEFT/RIGHT)
        '''
        pass  # TODO: Question 3a

        current_direction_value = self.current_direction.value
        new_direction_value = (current_direction_value + 1) % 4
        self.current_direction = Facing(new_direction_value)
        return self.current_direction

    def turn_right(self) -> Facing:  # type: ignore
        '''
        让机器人顺时针转向
        '''
        pass  # TODO: Question 3b
        current_direction_value = self.current_direction.value
        new_direction_value = (current_direction_value - 1) % 4
        self.current_direction = Facing(new_direction_value)
        return self.current_direction

    def find_enemy(self) -> bool:  # type: ignore
        '''
        如果找到敌人（机器人和敌人坐标一致），就返回true
        '''
        pass  # TODO: Question 4

        if self._current_pos == self.enemy_pos:
            return True
        else:
            return False

    def record_position(self, step: int) -> None:
        '''
        将当前位置记录到 position_history 字典中
        键(key)为步数 step，值(value)为当前坐标 self.current_pos
        例如：step=1 时，记录 {1: (0, 0)}
        '''
        pass  # TODO: Question 5a
        if len(self.position_history) == 0:
            self.position_history[1] = self._current_pos
        else:
            previous_step = max(self.position_history.keys())
            self.position_history[previous_step + 1] = self._current_pos

    def get_position_at_step(self, step: int) -> tuple:  # type: ignore
        '''
        从 position_history 字典中获取指定步数的坐标
        如果该步数不存在，返回 None
        '''
        pass  # TODO: Question 5b
        if step in self.position_history.keys():
            return self.position_history[step]
        else:
            return None


"""
在这里你需要实现 AdvancedGrid 类，继承自 Grid 类，并添加以下功能：
1. 追踪移动步数
2. 计算到敌人的曼哈顿距离

类名：AdvancedGrid
继承自：Grid
包含以下新属性：
- steps: int - 追踪移动步数，初始值为 0

包含以下方法：
1. move_forward(self) -> Tuple[int, int]
    调用父类的 move_forward 方法完成移动
    新增实现：移动步数 self.steps 加 1
    返回：移动后新坐标

2. distance_to_enemy(self) -> int
    计算当前位置到敌人位置的曼哈顿距离
    曼哈顿距离 = |x1 - x2| + |y1 - y2|
    返回：曼哈顿距离值

"""
# TODO: Question 6


class AdvancedGrid(Grid):
    def __init__(self, width, height, enemy_pos):
        super().__init__(width, height, enemy_pos)
        self.steps = 0

    def move_forward(self):
        super().move_forward()
        self.steps += 1
        return self._current_pos

    def distance_to_enemy(self):
        self.manhadun_distance = abs(
            self._current_pos[0] - self.enemy_pos[0]) + abs(
            self._current_pos[1] - self.enemy_pos[1])
        return self.manhadun_distance
