def squaredvalues(beg, end):
    lst = []

    for i in range(beg, end):
        lst.append(i**2)

        lst_even = []
        lst_odd =[]

        for i in list():
            if i %2==0:

                lst_even.append(i)
            else:
                lst_odd.append(i)
                print("here a list of even squares within specified range",lst_even)
                print("here a list of odd squares within specified range",lst_odd)
                beg = int(input("enter starting range : "))
                end = int(input("enter end range : "))

                squaredvalues(beg, end)