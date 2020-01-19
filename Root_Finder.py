print ('nROOTx Finder\n\n')

pwr_list = []

def pwr_test(num):
    n = 2
    k = 2
    while k <= num**.5 + 1:
        try:
            if num == k**2:
                pwr_list.append(str(k) + '^' + str(n))
                print(pwr_list[-1])
                break
            elif num < k**n:
                if pwr_list == []:
                    if k > num**.5:
                        print('None')
                n = 2
                k = k + 1
            elif num != k**n:
                n = n + 1
            elif num == k**n:
                pwr_list.append(str(k) + '^' + str(n))
                print(pwr_list[-1])
                n = n + 1
            else:
                print('None')
        except:
            return
    print('')
    print('Done')
    return


def test():
    print("Type Number To Find It's Roots\n")
    x = int(input())
    print('')
    pwr_test(x)


def again():
    print('\n\n')
    test()
    again()


test()
again()
