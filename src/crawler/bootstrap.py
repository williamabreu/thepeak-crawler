from dependency_injector import containers, providers

from src.crawler.adapters.unit_of_work import CrawlerUnitOfWork
from src.crawler.adapters.webdriver import SeleniumWebdriver


class CrawlerContainer(containers.DeclarativeContainer):
    webdriver = providers.Singleton(SeleniumWebdriver)
    uow = providers.Singleton(CrawlerUnitOfWork)
