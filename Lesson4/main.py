from television import Television
# from the module television import class Television

import math_ops


def main():
    my_tele = Television(True)
    my_tele.channel_up()
    my_tele.volume_up()
    print(my_tele)

    x1 = 5
    x2 = 10
    y1 = -5
    y2 = -15
    print(math_ops.dist(x1,y1,x2,y2))



if __name__ == '__main__':
    main()