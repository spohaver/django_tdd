from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_start_list_and_retrieve_it_later(self):
        # Sean has head about a cool new online to-do app.
        # He goes to check its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title), \
            "Browser title was " + self.browser.title
        self.fail('Finish the test!')

        # He is invited to enter a to-do item straight away

        # He types "Buy some games" into a text box (Cause games are awesome)

        # When he hits enter, the page updates, and now the page lists:
        # "1: Buy some games" as an item in a to-do list

        # There is still a text box inviting her to add another item. He enters
        # "Buy some downloadable content"

        # The page updates again, and now shows both items in the list

        # He wonders whether the site will remember her list. Then he sees that
        # the site has generated a unique URL for him -- there is some
        # expanatory text to that effect.

        # He visits that URL - the to-do list is still there.

        # Satisfied he goes back to playing some other games.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
