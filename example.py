import valorant

client = valorant.Client()
role = client.role('duelist')
print(role.name)