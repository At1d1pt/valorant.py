from .shop import ShopItem

class DamageRange:
    def __init__(self , data):
        self.raw = data

    @property
    def start(self):
        return self.raw['rangeStartMeters']

    @property
    def end(self):
        return self.raw['rangeEndMeters']

    @property
    def head(self):
        return self.raw['headDamage']
    
    @property
    def body(self):
        return self.raw['bodyDamage']

    @property
    def leg(self):
        return self.raw['legDamage']

class ADS:
    def __init__(self , data):
        self.raw = data

    @property
    def zoom(self):
        return self.raw['zoomMultiplier']

    @property
    def fire_rate(self):
        return self.raw['fireRate']

    @property
    def run_speed_multiplier(self):
        return self.raw['runSpeedMultiplier']

    @property
    def burst_count(self):
        return self.raw['burstCount']

    @property
    def first_bullet_accuracy(self):
        return self.raw['firstBulletAccuracy']

class AltGunStats:
    def __init__(self, data):
        self.raw = data

    @property
    def shotgun_pellet_count(self):
        return self.raw['shotgunPelletCount']
    
    @property
    def burst_range(self):
        return self.raw['burstRate']

class WeaponStats:
    def __init__(self, data):
        self.raw = data

    @property
    def fire_rate(self):
        return self.raw['fireRate']

    @property
    def magazine_size(self):
        return self.raw['magazineSize']

    @property
    def run_speed_multiplier(self):
        return self.raw['runSpeedMultiplier']

    @property
    def equip_time(self):
        return self.raw['equipTimeSeconds']

    @property
    def reload_time(self):
        return self.raw['reloadTimeSeconds']

    @property
    def first_bullet_accuracy(self):
        return self.raw['firstBulletAccuracy']

    @property
    def shotgun_pellet_count(self):
        return self.raw['shotgunPelletCount']

    @property
    def wall_penetration_short(self):
        return self.raw['wallPenetration'].split('::')[1]
    
    @property
    def wall_penetration(self):
        return self.raw['wallPenetration']

    @property
    def feature(self):
        return self.raw['feature']

    @property
    def fire_mode(self):
        return self.raw['fireMode']

    @property
    def alt_fire_type(self):
        return self.raw['altFireType']

    @property
    def alt_fire_type_short(self):
        return self.raw['altFireType'].split('::')[1]

    @property
    def ads(self):
        return None if self.raw['adsStats'] is None else ADS(self.raw['adsStats'])

    @property
    def alt_fire(self):
        return None if self.raw['altShotgunStats'] is None else AltGunStats(self.raw['altShotgunStats'])

    @property
    def air_burst_stats(self):
        return self.raw['airBurstStats']

    @property
    def damage_ranges(self):
        r = []

        for damage_range in self.raw['damageRanges']:
            r.append(DamageRange(damage_range))

        return r

class Weapon:
    def __init__(self , data):
        self.raw = data

    @property
    def name(self):
        return self.raw['displayName']

    @property
    def category_short(self):
        return self.raw['category'].split('::')[1]

    @property
    def category(self):
        return self.raw['category']

    @property
    def uuid(self):
        return self.raw['uuid']

    @property
    def default_skin_uuid(self):
        return self.raw['defaultSkinUuid']

    @property
    def display_icon(self):
        return self.raw['displayIcon']

    @property
    def kill_stream_icon(self):
        return self.raw['killStreamIcon']

    @property
    def asset_path(self):
        return self.raw['assetPath']

    @property
    def shop(self):
        return ShopItem(self.raw['shopData'] , name=self.name)

    @property
    def stats(self):
        return WeaponStats(self.raw['weaponStats'])