class Role:
    def __init__(self , data):
        self.raw = data
    
    @property
    def uuid(self):
        return self.raw['uuid']

    @property
    def name(self):
        return self.raw['displayName']
    
    @property
    def description(self):
        return self.raw['description']
    
    @property
    def display_icon(self):
        return self.raw['displayIcon']

    @property
    def asset_path(self):
        return self.raw['assetPath']