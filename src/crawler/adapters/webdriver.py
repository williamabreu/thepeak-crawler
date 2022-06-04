import logging
from datetime import datetime
from time import sleep
from typing import List

from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver import Remote
from selenium.webdriver.support.select import Select

from src.crawler.config import CrawlerConfig
from src.crawler.domain.models import Track
from src.crawler.ports.webdriver import Webdriver

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


class SeleniumWebdriver(Webdriver):
    def __init__(self) -> None:
        self._sleep_time = 5
        self._driver_url = CrawlerConfig.selenium_url
        self._playlist_url = "https://www.thepeak.fm/recentlyplayed/"

    def run(self) -> List[Track]:
        with Remote(
            command_executor=self._driver_url,
            desired_capabilities={
                "browserName": "chrome",
                "platformName": "LINUX",
            },
        ) as driver:
            driver.get(self._playlist_url)
            tracks = []

            for ref_day in ("-1", "-2", "-3", "-4", "-5", "-6"):
                elem = driver.find_element_by_class_name("dateSelector")
                date_selector = Select(elem.find_element_by_tag_name("select"))
                date_selector.select_by_value(ref_day)

                sleep(self._sleep_time)

                while True:
                    try:
                        driver.find_element_by_class_name("moreBtn").click()
                    except ElementNotInteractableException:
                        break

                # Format example:
                # <div class="selectedDate">September 06, 2021</div>
                date = driver.find_element_by_class_name("selectedDate")

                # Format example:
                # <div class="songs">
                #   <div class="song">
                #     <div class="songTime primary_bgd_color">10:09 AM</div>
                #     <div class="songThumb">...</div>
                #     <div class="songInfo">
                #         <div class="songArtist">Young The Giant</div>
                #         <div class="songTitle">My Body</div>
                #         <div class="badge">...</div>
                #     </div>
                #   </div>
                # ...
                # </div>
                songs = driver.find_element_by_class_name("songs")

                content_date = date.text
                content_songs = songs.text.split("\n")

                if len(content_songs) % 3 != 0:
                    logger.warning(
                        "Something isn't smelling good... "
                        "The result content isn't multiple of 3."
                    )

                for i in range(len(content_songs) - 1, -1, -3):
                    time: str = content_songs[i - 2]
                    artist: str = content_songs[i - 1]
                    title: str = content_songs[i]

                    timestamp = datetime.strptime(
                        f"{content_date} {time}", "%B %d, %Y %I:%M %p"
                    )

                    tracks.append(
                        Track.create(
                            song_time=timestamp,
                            song_artist=artist,
                            song_title=title,
                        )
                    )

            return tracks
