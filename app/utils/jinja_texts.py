import os

from typing import NoReturn, Union

import yaml
from jinja2 import Template

from app.utils.misc import check_timestamp, convert_timestamp_to_str

class JinjaTexts:
    """Класс для генерации шаблонов из yaml файла"""
    def __init__(
        self,
        file_name: str
    ):
        """
        :param file_name: `str` - yaml файл в котором хранятся шаблоны
        """
        self.file_name = file_name

        with open(self.file_name, 'r') as file:
            self.yaml = yaml.safe_load(file)

    def __get_template(
        self,
        template_name: str
        ) -> Union[Template, NoReturn]:
        """
        Получение шаблона
        :param template_name:`str` - название шаблона
        :raise NameError если шаблон не найден
        """

        if template_name not in self.yaml:
            raise NameError(f'Template "{template_name}" not find in "{self.file_name}"')

        template_text = self.yaml[template_name]
        template = Template(template_text)

        template.globals.update(check_timestamp=check_timestamp)
        template.globals.update(timestamp_to_str=convert_timestamp_to_str)

        return template

    def gettext(
        self,
        template_name: str,
        context: dict | None = None
    ) -> str:
        """Генерирует текст на основе шаблона
        :param template_name: `str` - переменная в yaml файле
        :param context: `Optional[dict]` - """

        template = self.__get_template(template_name)

        text = template.render(
            context if context else {}
        )

        text = text.replace('\n', '')
        text = text.replace('<br>', '\n')
        print(text)
        return text

dir = os.path.dirname(os.path.dirname(__file__))
path = os.path.join(dir, 'messages.yaml')

Texts = JinjaTexts(path)
