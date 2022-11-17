from .role import Role

class Agent:
    def __init__(self, data) -> None:
        self.raw = data

    @property
    def uuid(self):
        return self.raw[['uuid']]

    @property
    def name(self):
        return self.raw['displayName']
    
    @property
    def description(self):
        return self.raw['description']

    @property
    def developerName(self):
        return self.raw['developerName']

    @property
    def character_tags(self):
        return self.raw['characterTags']

    @property
    def display_icon(self):
        return self.raw['displayIcon']

    @property
    def display_icon_small(self):
        return self.raw['displayIconSmall']

    @property
    def bust_potrait(self):
        return self.raw['bustPortrait']

    @property
    def full_potrait(self):
        return self.raw['fullPortrait']

    @property
    def full_potrait_v2(self):
        return self.raw['fullPortraitV2']

    @property
    def kill_feed_potrait(self):
        return self.raw['killfeedPortrait']

    @property
    def background(self):
        return self.raw['background']

    @property
    def background_gradient_colors(self):
        return self.raw['backgroundGradientColors']

    @property
    def asset_path(self):
        return self.raw['assetPath']

    @property
    def is_full_potrait_facing_right(self):
        return self.raw['isFullPortraitRightFacing']

    @property
    def is_playable_character(self):
        return self.raw['isPlayableCharacter']

    @property
    def is_available_for_test(self):
        return self.raw['isAvailableForTest']

    @property
    def is_base_character(self):
        return self.raw['isBaseContent']

    @property
    def role(self):
        return Role(self.raw['role'])