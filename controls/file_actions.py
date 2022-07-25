from pathlib import Path

import allure
from selene.core.entity import Element

import tests


class FileActions:


    def attach_file(self, el: Element, file_path):
        allure.step(f'Attach file located - {file_path}')
        file: str = Path(tests.__file__).parent.parent.joinpath(file_path)
        el.type(file)
