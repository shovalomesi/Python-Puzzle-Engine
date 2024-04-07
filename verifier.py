# Mendi Lirmak 316162510
# Dana Farber 209376359
# Shoval Omesi 307984294

import random

class Verifier:
    def __init__(self, solved_board):
        self.solved_board = solved_board
        self.columns_packets = []
        self.rows_packets = []
        self.subgrid_packets = []

    def make_packets_for_columns(self):
        for col in range(9):
            packet = []
            for i in range(9):
                cell = self.solved_board[i][col]
                value = random.choice(cell)
                packet.append(value)
                cell.remove(value)
            self.columns_packets.append(packet)

    def make_packets_for_rows(self):
        for row in range(9):
            packet = []
            for col in range(9):
                cell = self.solved_board[row][col]
                value = random.choice(cell)
                packet.append(value)
                cell.remove(value)
            self.rows_packets.append(packet)

    def make_packets_for_subgrids(self):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                packet = []
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        cell = self.solved_board[row][col]
                        value = random.choice(cell)
                        packet.append(value)
                        cell.remove(value)
                self.subgrid_packets.append(packet)

    def verify_packets(self):
        for packet in self.columns_packets + self.rows_packets + self.subgrid_packets:
            sorted_packet = sorted(packet)
            packet[:] = sorted_packet
            if sorted_packet != list(range(1, 10)):
                return False
        return True