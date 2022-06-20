

class Astr_shadow:
    def __init__(self,astr_image,make_image):
        self.astr_image = make_image
        self.shadow_image = astr_image
        self.frame_count = 0
        self.frame_limit = 5
        self.flicker_count = 0
        self.flicker_limit = 7

    def init_flicker(self):
        self.flicker_count += 1
        self.frame_count = 0
        self.astr_image , self.shadow_image = self.shadow_image , self.astr_image

def flickering(self):
    if self.shadow.flicker_count != 0:
        self.shadow.frame_count += 1
        if self.shadow.frame_count == self.shadow.frame_limit:
            self.shadow.init_flicker()
            self.image = self.shadow.astr_image

        if self.shadow.flicker_count == self.shadow.flicker_limit:
            self.shadow.flicker_count = -1
            self.shadow.init_flicker()
