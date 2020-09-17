from selenium import webdriver
from time import sleep
import pandas as pd


class ChromeExtension:
    def __init__(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('permissions.default.image', 2)
        self.driver = webdriver.Firefox()

        urls = [
            "https://chrome.google.com/webstore/detail/kami-extension-pdf-and-do/ecnphlgnajanjnkcmbpancdjoidceilk",
            "https://chrome.google.com/webstore/detail/alice-keeler-classroom-sp/ifkgpacemihiplnocjocpgmoiefcojik",
            "https://chrome.google.com/webstore/detail/easybib-toolbar/hmffdimoneaieldiddcmajhbjijmnggi",
            "https://chrome.google.com/webstore/detail/add-to-google-classroom/oaobmlmjmhedmlphfdmdjpppjmcljnkp",
            "https://chrome.google.com/webstore/detail/craftytext/kjgfnioibniobfkjcjjfikmhecajpcio",
            "https://chrome.google.com/webstore/detail/mote-voice-notes-feedback/ajphlblkfpppdpkgokiejbjfohfohhmk"
        ]

        master_list = []
        for url in urls:
            data_dict = {}
            self.driver.get(url)
            sleep(3)

            extension_name = self.driver.find_element_by_xpath(
                "//h1[contains(@class, 'e-f-w')]").text

            extension_short_desc = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'C-b-p-j-Pb')]").text

            category = self.driver.find_element_by_xpath(
                "//span[contains(@class, 'e-f-yb-w')]/a[contains(@class, 'e-f-y')]"
            ).text

            version = self.driver.find_element_by_xpath(
                "//span[contains(@class, 'C-b-p-D-Xe h-C-b-p-D-md')]").text

            updated = self.driver.find_element_by_xpath(
                "//span[contains(@class, 'C-b-p-D-Xe h-C-b-p-D-xh-hh')]").text

            size = self.driver.find_element_by_xpath(
                "//span[contains(@class, 'C-b-p-D-Xe h-C-b-p-D-za')]").text

            language = self.driver.find_element_by_xpath(
                "//span[contains(@class, 'C-b-p-D-Xe h-C-b-p-D-Ba')]").text

            developer_name = self.driver.find_element_by_class_name(
                "e-f-Me").text

            try:
                developer_address = self.driver.find_element_by_xpath(
                    "//div[contains(@class, 'C-b-lmDd0-Q7Zjwb')]").text
            except:
                developer_address = 'NAN'
                continue

            overview = self.driver.find_element_by_class_name(
                "C-b-p-j-Oa-i8xkGf").text

            overview_complete = extension_short_desc + overview

            data_dict['Extension Name'] = extension_name
            data_dict['Category'] = category
            data_dict['Version'] = version
            data_dict['Updated'] = updated
            data_dict['Size'] = size
            data_dict['Language'] = language
            data_dict['Developer Name'] = developer_name
            data_dict['Developer Adreess'] = developer_address
            data_dict['Overview'] = overview_complete

            master_list.append(data_dict)

        df = pd.DataFrame(master_list)
        df.to_csv('Chrome_Extension_Dataset_2.csv', index=False)
        """df.to_excel('Chrome_Extension_Dataset_1.xlsx',
                    engine='xlsxwriter',
                    index=False)"""


ChromeExtension()