class Settings:
    #all settings for AlienInvasion game.
    def __init__(self):
        """ Initialize game settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (230,230,230)

        #bullet property

        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
