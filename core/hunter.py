import requests

class Hunter:
    
    def __init__(self, site):
        self.site = site
    
    #request
    def search(self):
        url = requests.get('https://api.hunter.io/v2/domain-search?domain={site}&api_key=239d49fcb82e071045c40b73bb9480bf59211561'.format(site=self.site))
        return url

    def treatment(self,ans):

        ans = ans.replace("data", "Info's URL")
        ans = ans.replace("meta", "Obs")
        ans = ans.replace("{", " ")
        ans = ans.replace("}", " ")
        ans = ans.replace("    ", "")
        ans = ans.replace("   ", "")
        ans = ans.replace("   ", "")
        ans = ans.replace("  ", "")
        ans = ans.replace("]", "-------------------")
        ans = ans.replace("[", "")
        ans = ans.replace('"', '')
        ans = ans.replace(',', '')

        return ans