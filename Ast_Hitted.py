

class Astr_shadow:
    def __init__(self,astr_image,shadow_image):
        self.astr_image = astr_image
        self.shadow_image = shadow_image
        self.frame_count = 0
        self.frame_limit = 5
        self.flicker_count = 0
        self.flicker_limit = 7

    def init_flicker(self):
        self.flicker_count = 0
        self.flicker_count += 1
        self.frame_count = 0

    def cycle_flicker(self):
        self.flicker_count += 1
        self.frame_count = 0

def flickering(self):
    if self.shadow.flicker_count != 0:
        self.shadow.frame_count += 1
        if self.shadow.frame_count == self.shadow.frame_limit:
            self.shadow.cycle_flicker()
            self.image , self.shadow_image = self.shadow_image , self.image

        if self.shadow.flicker_count > self.shadow.flicker_limit:
            self.image = self.shadow.astr_image
            self.shadow_image = self.shadow.shadow_image
