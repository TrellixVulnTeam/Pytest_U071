import pytest
from dop_methods import Methods


@pytest.fixture
def app(request):
    dop = Methods()
    request.addfinalizer(dop.destroy)
    return dop


def test_search(app):
    app.input_search()
    app.present_element()







# Unittest
# class two_mos(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#     def test_serach(self):
#         driver = self.driver
#         driver.maximize_window()
#         driver.get("http://www.mos.ru")
#         driver.find_element_by_class_name('mos-layout-icon-search_black').click()
#         driver.find_element_by_class_name('tt-input').send_keys(u'Собянин')
#         driver.find_element_by_class_name('mos-layout-icon-search_black').click()
#         driver.implicitly_wait(10)
#         driver.find_element_by_class_name('wdg-mayor')
#         # time.sleep(5)
#     def tearDown(self):
#         self.driver.close()
# if __name__ == "__main__":
#     unittest.main()
