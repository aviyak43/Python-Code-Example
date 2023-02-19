# Aviya Keisar _311515415
import Classes as Cls

def print_menu(name):
    '''Prints the menu'''
    print("Hello " + name + ':')
    print("1: add new cars",
          "2: sell cars",
          "3: print cars details",
          "4: print store details",
          "5: exit",
          "Choose option 1-5:", sep='\n')


def main():
    '''main function'''
    name = input("Please insert the name of the store owner:")
    store = Cls.CarStore(name)
    while True:
        print_menu(name)
        choice = int(input())
        if choice == 1:
            store.add_cars()
        elif choice == 2:
            store.sell_car()
        elif choice == 3:
            store.print_cars()
        elif choice == 4:
            print(store)
        elif choice == 5:
            break


if __name__ == '__main__':
    main()
