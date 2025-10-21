from abc import ABC, abstractmethod


class Touch(ABC):
    
    @abstractmethod
    def click(self, x: int, y: int, duration: int = 100):
        """
        click 点击

        Args:
            x (int): 横坐标
            y (int): 纵坐标
            duration (int, optional): 持续时间. Defaults to 100.
        """
        
    @abstractmethod
    def swipe(self, points: list, duration: int = 300):
        """
        swipe 滑动

        Args:
            points (list): [(x,y),(x,y),(x,y)] 坐标列表
            duration (int): 持续时间. Defaults to 300.
        """

    @abstractmethod
    def touch_with_id(self, touch_id: int, x: int, y: int, operation: str):
        """
        touch_with_id 指定id点触控
        需要外部延迟管理

        Args:
            touch_id (int): 触控点id
            x (int): 横坐标
            y (int): 纵坐标
            operation (str): "down","move","up"
        """
