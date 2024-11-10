def get_max_gates():
    arrival = [9.0, 9.40, 9.50, 11.00, 15.00, 18.00, 19.00, 20.00, 21.00, 22.00, 23.00]
    departure = [9.10, 12.00, 11.20, 11.30, 19.00, 20.00, 23.5, 23.5, 23.5, 23.5, 23.5]
  #
    # a = 9.0
    # d = 9.1
    #
    max_gate = 1
    i, j = 1, 0
    temp = 0
    while i < len(arrival) and j < len(departure):
        if departure[j] > arrival[i]:
            temp += 1
            i += 1
        else:
            j = i
            if temp > max_gate:
                max_gate = temp
            temp = 1
    print(max_gate)


coins = [7, 3, 2, 4, 9, 12, 56], people = 3
[2,3,4,9,7,12,56]

[1,47,48,50] i+

diff = 46
get_max_gates()
