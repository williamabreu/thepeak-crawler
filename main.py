from dependency_injector.wiring import Provide, inject
from kingdom_sdk.database import orm

from src.crawler.adapters.unit_of_work import CrawlerUnitOfWork
from src.crawler.bootstrap import CrawlerContainer
from src.crawler.ports.webdriver import Webdriver


@inject
def main(
    uow: CrawlerUnitOfWork = Provide[CrawlerContainer.uow],
    webdriver: Webdriver = Provide[CrawlerContainer.webdriver],
) -> None:
    orm.start_mappers("src.crawler.orm")
    tracks = webdriver.run()

    with uow:
        for track in tracks:
            uow.tracks.add(track)
        uow.commit()


if __name__ == "__main__":
    container = CrawlerContainer()
    container.wire(modules=[__name__])
    main()
