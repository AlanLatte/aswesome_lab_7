class ExitFromAddMethod(Exception):
    def __init__(self, message: str = "Выход из меню добавления поезда."):
        self.message = message

    def __str__(self):
        return self.message
