class StringProcessor:
    @staticmethod
    def process(text: str) -> str:
        if not text:
            return "."
        processed_text = text[0].upper() + text[1:]
        if not processed_text.endswith("."):
            processed_text += "."
        return processed_text

#     Проверить, что метод process класса StringProcessor корректно преобразует входную строку:
# Первая буква строки должна быть заглавной. Если строка не заканчивается точкой,
# то она должна быть добавлена в конце. Создайте минимум 3 позитивных
# и 2 негативных теста.