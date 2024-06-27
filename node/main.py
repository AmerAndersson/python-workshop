from node.app import DoublyLinkedList


def main() -> None:
    # the main function to run
    dll = DoublyLinkedList()
    dll.insert(data="apple")
    dll.insert(data="banana")
    dll.insert(data="cherry")

    print("Doubly Linked List:")
    current = dll.head
    while current:
        print(current.data)
        current = current.next

    target = "cherry"
    found_node = dll.find(target=target)
    if found_node:
        print(f"Found {target} in the list.")
        dll.delete(target=target)
        print(f"{target} deleted from the list.")
    else:
        print(f"{target} not found in the list.")


if __name__ == "__main__":
    main()
