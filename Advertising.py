class Advertising:
    def __init__(self, dataFile):
        # This data was collected from the 2010 United States Census
        # TODO: Read in Demographic data from the file provided
        pass

    def calculations(self):
        # TODO: Fill this method with your calculations
        pass

    # The following methods return the effectiveness of the campaign divided by age demographic.
    # The value represents the percentage of the age range that will see the advertisement.
    # The percentages are in order by age group: Child, Teenager, Young Adult, Adult, Senior.
    def instagramAd(self):
        adEffectiveness = [0.13, 0.47, 0.73, 0.24, 0.01]
        return adEffectiveness

    def facebookAd(self):
        adEffectiveness = [0.01, 0.02, 0.30, 0.48, 0.22]
        return adEffectiveness

    def youtubeAd(self):
        adEffectiveness = [0.62, 0.41, 0.49, 0.32, 0.05]
        return adEffectiveness

    def tiktokAd(self):
        adEffectiveness = [0.82, 0.71, 0.24, 0.19, 0.01]
        return adEffectiveness

    def billboard(self):
        adEffectiveness = [0.07, 0.20, 0.20, 0.20, 0.15]
        return adEffectiveness

    def tvCommercial(self):
        adEffectiveness = [0.05, 0.18, 0.28, 0.50, 0.33]
        return adEffectiveness

    # Sponsor a cycling team
    def sponsorTeam(self):
        adEffectiveness = [0.27, 0.24, 0.37, 0.47, 0.26]
        return adEffectiveness

    # Demographic Data inner class. This object stores demographic information for a neighborhood
    class DemographicData:
        # Demographic information
        def __init__(self, neighborhoodName, popC, popT, popYA, popA, popS):
            self.name = neighborhoodName
            self.popChildren = popC
            self.popTeenagers = popT
            self.popYoungAdults = popYA
            self.popAdults = popA
            self.popSeniors = popS
            self.popTotal = popC + popT + popYA + popA + popS

        def getName(self):
            return self.name

        def getPopulation(self, type):
            # Returns the population of a specific category
            # children, teenagers, youngAdults, adults, seniors, or total
            if type == "children":
                return self.popChildren
            elif type == "teenagers":
                return self.popTeenagers
            elif type == "youngAdults":
                return self.popYoungAdults
            elif type == "adults":
                return self.popAdults
            elif type == "seniors":
                return self.popSeniors
            elif type == "total":
                return self.popTotal
            else:
                print("Invalid population type for getPopulation() call.")
                return -1
