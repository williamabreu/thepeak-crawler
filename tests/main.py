import json
import logging
from datetime import datetime
from typing import Dict

from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver import Chrome

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


def create_track(time: datetime, artist: str, title: str) -> Dict[str, str]:
    return {
        "songTime": time.isoformat(),
        "songArtist": artist,
        "songTitle": title,
    }


def main() -> None:
    with Chrome(executable_path="./chromedriver.exe") as driver:
        driver.get("https://www.thepeak.fm/recentlyplayed/")

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

    result = []

    for i in range(len(content_songs) - 1, -1, -3):
        time: str = content_songs[i - 2]
        artist: str = content_songs[i - 1]
        title: str = content_songs[i]

        timestamp = datetime.strptime(
            f"{content_date} {time}", "%B %d, %Y %I:%M %p"
        )

        result.append(create_track(timestamp, artist, title))

    with open("result.json", "w") as fp:
        json.dump(result, fp, indent=2)


if __name__ == "__main__":
    main()
