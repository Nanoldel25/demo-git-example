def demo_zip():
    value1 = list(range(2, 10))
    value2 = list(range(10, 29, 3))
    print(value1)
    print(value2)

    for v1, v2 in zip(value1, value2):
        print('v1 =', v1, 'v2 =', v2, 'sum =', v1+v2)

    value3 = list(range(20, -7, -4))
    print("==="*10)

    for v1, v2, v3 in zip(value1, value2, value3):
        print('v1 =', v1, 'v2 =', v2, 'v3 =', v3, 'sum =', v1+v2+v3)

def demo_map():
   list1 = [1, 2, 3, 4]
   list2 = [3, 4, 5, 6]

   list_of_powers = list(map(pow, list1, list2))
   print(list_of_powers)

def main():
    # print('Hello main')
    demo_zip()
    demo_map()

if __name__ == "__main__":
    main()