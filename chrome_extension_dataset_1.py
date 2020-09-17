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

            data_dict['Extension Name'] = extension_name
            data_dict['Short Description'] = extension_short_desc

            master_list.append(data_dict)

            print(extension_name, extension_short_desc)

        df = pd.DataFrame(master_list)
        df.to_csv('Chrome_Extension_Dataset_1.csv', index=False)
        """df.to_excel('Chrome_Extension_Dataset_1.xlsx',
                    engine='xlsxwriter',
                    index=False)"""


ChromeExtension()