from crawler.entity import Entity
from crawler.service import Service

class Controller:
    def __init__(self):
        self.entity = Entity
        self.service = Service
    def searching_data(self):
        service = self.service

        service.get_sichug_url()
        service.get_corona_page()


if __name__ == "__main__":
    api = Controller()
    api.searching_data()
