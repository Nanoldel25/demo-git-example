def demo_map():
   list1 = [1, 2, 3, 4]
   list2 = [3, 4, 5, 6]

   list_of_powers = list(map(pow, list1, list2))
   print(list_of_powers)

def main():
    # print('Hello main')
    demo_map()

if __name__ == "__main__":
    main()