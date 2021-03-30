from months import search_pi_day
from birthdaylocations import append_locations
from sweepstakes import pick_winner
from linkedlist import LinkedList
from binarysearchtree import BinarySearchTree

if __name__ == '__main__':
    pi_day = search_pi_day()
    future_locations = append_locations()
    sweepstakes_winner = pick_winner()
    linked_list = LinkedList()
    binary_search = BinarySearchTree()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)