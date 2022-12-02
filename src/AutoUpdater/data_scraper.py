# simple script to scrape all required medaia data from leagueoflegends.fandom.com
# Have chrome installed in standart directory and place chromedriver in this dir
import time
from typing import List
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from pathlib import Path
import logging

logging.basicConfig(filename="data_scraper.log", encoding="utf-8", level=logging.DEBUG)


class DataScraper:
    def __init__(self) -> None:
        self._image_path = Path(__file__).parents[2] / Path("data\\champions")
        # set chromedriver.exe path
        self._driver = webdriver.Chrome(
            executable_path=Path(__file__).GetDirectoryName()
            / "C:\\Users\\tobia\\Documents\\Code\\LeagueHelper\\src\\related_scripts\\chromedriver.exe"
        )
        self._driver.implicitly_wait(0.5)
        # maximize browser
        self._driver.maximize_window()

        self._enable_download_champ_icons = False

    def __del__(self):
        self._driver.quit()

    def run(self):
        champs = self._get_champion_list()
        self._download_data(champs)

    def do_for_each_champ(func):
        def inner(*args, **kwargs):
            for champ in args[1]:
                func(args[0], champ)

        return inner

    def _download_data(self, champs):
        self._download_champ_data(champs)

    @do_for_each_champ
    def _download_champ_data(self, *args):
        self._open_url(f"https://leagueoflegends.fandom.com/wiki/{args[0]}/LoL")
        self._confirm_cookies()
        if self._enable_download_champ_icons:
            self._download_champ_icons(args[0])

    def _download_champ_icons(self, champ):
        path = str(self._image_path / (champ + "/"))
        file = Path(f"{champ}_circle.png")
        Path(path).mkdir(parents=True, exist_ok=True)
        with open(path / file, "wb") as file:
            time.sleep(1)
            try:
                image = self._driver.find_element(
                    By.XPATH, f"//img[@alt='{champ} OriginalCircle.png']"
                )
                logging.info("Saving Image: " + path)
                file.write(image.screenshot_as_png)
            except:
                logging.error("NEED TO FIX THIS: SPECIAL CHARS")  # TODO

    def _open_url(self, url):
        self._driver.get(url)
        self._confirm_cookies()

    def _confirm_cookies(self):
        try:
            self._driver.find_element(
                By.XPATH, "//*[@data-tracking-opt-in-accept='true']"
            ).click()
        except selenium.common.exceptions.NoSuchElementException:
            logging.info("No cookies confirmation required")

    def _get_champion_list(self):
        self._open_url("https://leagueoflegends.fandom.com/wiki/List_of_champions")
        champ_table = self._driver.find_element(
            By.XPATH,
            "//*[@class='article-table sticky-header sortable jquery-tablesorter']",
        )
        champ_list = []
        champ_table_content = champ_table.find_element(By.TAG_NAME, "tbody")
        table_element = champ_table_content.find_elements(By.TAG_NAME, "tr")
        for el in table_element:
            champ = el.find_element(By.TAG_NAME, "td")
            champ_name = champ.get_attribute("data-sort-value")
            champ_list.append(champ_name)
        return champ_list


if __name__ == "__main__":
    ds = DataScraper()
    ds.run()
