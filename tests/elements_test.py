import time
from pages.elements_page import TextBoxPage
from conftest import driver


class TestTextBox:

    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        input_data = text_box_page.fill_all_fields()
        output_data = text_box_page.check_filled_form()
        assert input_data == output_data , "input doesn't equal to output"
"""
        print(full_name+" "+out_full_name)
        print(email+" "+out_email)
        print(current_address+" "+out_current_address)
        print(permanent_address+" "+out_permanent_address)
"""





