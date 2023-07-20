import AdvertisingSolution

class AdCampaign:
    def main(self):
        # This class will test your Advertisement Solution
        fileName = input("Please enter the name of the file with the demographic information: ")
        ad = Advertising(fileName)
        ad.calculations()

ad_campaign = AdCampaign()
ad_campaign.main()
