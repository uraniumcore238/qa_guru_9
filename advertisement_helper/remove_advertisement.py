import allure
import selene
from selene.support.shared.jquery_style import ss


@allure.title('Remove advertisement from the site')
def remove_advertisement():
    (
        ss('[id^=google_ads][id$=container__], [id^=RightSide_Advertisement]').with_(timeout=10)
            .should(selene.have.size_greater_than_or_equal(2))
            .perform(selene.command.js.remove)
    )
