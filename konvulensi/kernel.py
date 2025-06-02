class Kernel:
    PREWITT = [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ]
    GAUSIAN = [
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ]
    MEDIAN_FILTER = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    ROBERTS_X = [
        [1, 0],
        [0, -1]
    ]
    ROBERTS_Y = [
        [0, 1],
        [-1, 0]
    ]
