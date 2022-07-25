import allure
from selene.core.entity import Element
from selene.support.conditions import have


class TableChecking:


    def asserts_exact_text(self, el: Element, text: str):
        allure.step(f'Assert exact text {text}')
        el.should(have.exact_text(text))


    def asserts_texts_in_rows(self, els: all, expeted_text):
        allure.step(f'Assert text {expeted_text} in rows')
        for el in els:
            row_text = el.text
            assert row_text in expeted_text, f'Actual text{row_text} but expected is {expeted_text}'
