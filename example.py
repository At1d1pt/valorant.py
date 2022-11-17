import valorant

client = valorant.Client()
print(client.agent(name='jett').voicelines.get_voice_line(878055936 , 'wav'))