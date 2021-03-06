from controllers.thread_led_controller import ThreadLedController
from utils.sync_led_utils import SyncLedUtils


class IteratorLedController(ThreadLedController):
    def __init__(self, config):
        super().__init__(self.__work, config)

        self.__colors = config.colors
        self.__current_colors = []
        self.__update_time = config.update_time

    def __get_next_color(self):
        if not self.__current_colors:
            self.__current_colors = self.__colors[::]

        return self.__current_colors.pop(0)

    def __work(self):
        color = self.__get_next_color()
        while not self._should_stop_thread:
            next_color = self.__get_next_color()
            SyncLedUtils.do_animated_color(self._leds, color, next_color, self.__update_time)
            color = next_color
