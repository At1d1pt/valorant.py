class ShopItem:
    def __init__(self , raw , name):
        self.raw = raw,
        self.name = name.capitalize()

    @property
    def cost(self):
        return self.raw['cost']

    @property
    def category(self):
        return self.raw['catrgory']
    
    @property
    def category_text(self):
        return self.raw['categoryText']

    @property
    def position(self):
        return self.raw['gridPosition']

    @property
    def can_be_trashed(self):
        return self.raw['canBeTrashed']

    @property
    def image(self):
        return self.raw['image'] if self.raw['image'] is not None else self.raw['newImage']

    @property
    def asset_path(self):
        return self.raw['assetPath']