class Season():
    def __init__(self, id, title, season, productionYear, ageRatingName, abstract, episodes):
        self.id = id
        self.title = title
        self.season = season
        self.productionYear = productionYear
        self.ageRatingName = ageRatingName
        self.abstract = abstract
        self.episodes = episodes

    def showSeason(self):
        print(self.title)
        print(self.season)
        print(self.productionYear)
        print(self.ageRatingName)
        print(self.abstract)
