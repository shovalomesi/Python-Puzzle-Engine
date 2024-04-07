# Mendi Lirmak 316162510
# Dana Farber 209376359
# Shoval Omesi 307984294

import random

class Prover:
    def __init__(self, packets):
        self.packets = packets

    def turn_over_and_shuffle(self):
        for packet in self.packets:
            random.shuffle(packet)