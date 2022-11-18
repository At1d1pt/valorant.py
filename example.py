import valorant

client = valorant.Client()

weapon = client.weapon(name='Phantom')
print(f"{weapon.name} [{weapon.category_short}]")