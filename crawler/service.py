from crawler.entity import Entity
class Service:
    def __init__(self):
        self.entity = Entity
    @staticmethod
    def get_sichug_url(dong):
        # 정부24의 정부/지자체 운영사이트에서 검색해서 들어감
        # https://www.gov.kr/portal/orgSite?Mcode=11181
