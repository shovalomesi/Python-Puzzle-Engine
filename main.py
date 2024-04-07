# Mendi Lirmak 316162510
# Dana Farber 209376359
# Shoval Omesi 307984294

from board import Board
from verifier import Verifier
from prover import Prover


def main():
    sudoku_board = Board()

    print("\n****** STEP 1 ******\n")
    sudoku_board.place_cards_according_to_step1()
    sudoku_board.print_solved_board_with_hidden_cards()

    print("\n****** STEP 2 ******\n")
    verifier = Verifier(sudoku_board.board)
    verifier.make_packets_for_columns()
    print("After column packets made:\n")
    sudoku_board.print_solved_board_with_hidden_cards()
    
    verifier.make_packets_for_rows()
    print("After row packets made:\n")
    sudoku_board.print_solved_board_with_hidden_cards()
    
    sudoku_board.sub_grid_print = True
    verifier.make_packets_for_subgrids()
    print("After subgrid packets made:\n")
    sudoku_board.print_solved_board_with_hidden_cards()

    print("\n****** STEP 3 ******\n")
    prover_columns = Prover(verifier.columns_packets)
    prover_rows = Prover(verifier.rows_packets)
    prover_subgrids = Prover(verifier.subgrid_packets)
    
    print("Before turning over and shuffling:")
    print_packets_info(prover_columns.packets, "Columns packets:")
    print_packets_info(prover_rows.packets, "Rows packets:")
    print_packets_info(prover_subgrids.packets, "Subgrids packets:")
    
    prover_columns.turn_over_and_shuffle()
    prover_rows.turn_over_and_shuffle()
    prover_subgrids.turn_over_and_shuffle()
    
    print("After turning over and shuffling:")
    print_packets_info(prover_columns.packets, "Columns packets:")
    print_packets_info(prover_rows.packets, "Rows packets:")
    print_packets_info(prover_subgrids.packets, "Subgrids packets:")

    print("\n****** STEP 4 ******\n")
    verify = verifier.verify_packets()
    print("After sorting:")
    print_packets_info(prover_columns.packets, "Columns packets:")
    print_packets_info(prover_rows.packets, "Rows packets:")
    print_packets_info(prover_subgrids.packets, "Subgrids packets:")
    if verify:
        print("All packets contain all values from 1 to 9.")
    else:
        print("Some packets do not contain all values from 1 to 9.")



def print_packets_info(packets, text):
    print(text)
    for i, packet in enumerate(packets):
        print(f"Packet {i + 1}: {packet}")
    print()

if __name__ == "__main__":
    main()
