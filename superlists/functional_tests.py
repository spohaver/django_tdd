from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_start_list_and_retrieve_it_later(self):
        # Sean has head about a cool new online to-do app.
        # He goes to check its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title), \
            "Browser title was " + self.browser.title
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Buy some games" into a text box (Cause games are awesome)
        inputbox.send_keys('Buy some games')

        # When he hits enter, the page updates, and now the page lists:
        # "1: Buy some games" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy some games')

        # There is still a text box inviting her to add another item. He enters
        # "Buy some downloadable content"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy some downloadable content')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items in the list
        self.check_for_row_in_list_table('1: Buy some games')
        self.check_for_row_in_list_table('2: Buy some downloadable content')

        # He wonders whether the site will remember her list. Then he sees that
        # the site has generated a unique URL for him -- there is some
        # expanatory text to that effect.
        self.fail('finish the test!')

        # He visits that URL - the to-do list is still there.

        # Satisfied he goes back to playing some other games.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
