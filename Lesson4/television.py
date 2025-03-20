class Television:
    def __init__(self,power_button):
        self.power_button = False
        self.channel = 3
        self.volume = 5

    def channel_up(self):
        self.channel += 1
    
    def channel_down(self):
        self.channel -= 1
    
    def return_channel(self):
        return self.channel
    
    def volume_up(self):
        self.volume += 1
    
    def volume_down(self):
        self.volume -= 1

    def get_volume(self):
        return self.volume
    
    def __str__(self):
        return f"Channel: {self.channel}\nVolume: {self.volume}"
    
    def __repr__(self):
        return f"Television({self.channel},{self.volume})"
    
tele1 = Television(True)
tele1.channel_up()
tele1.volume_down()
print(tele1)