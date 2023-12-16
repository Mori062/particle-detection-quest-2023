
import numpy as np

class MyOpenClose:
    
    @staticmethod
    def opening(image, non_zero_thread=3):
        cp = image.copy()
        for y in range(len(image)):
            for x in range(len(image[0])):
                if image[y][x] == 0:
                    continue
                offsets = [ (-1, 0),
                   (0, -1),           (0, 1),
                    (1, 0),
                ]
                values = []
                for offset in offsets:
                    _y = y + offset[0]
                    _x = x + offset[1]
                    if 0 <= _y < len(image) and 0 <= _x < len(image[0]):
                        values.append(image[_y][_x])
                    else:
                        values.append(0)
                if np.count_nonzero(values) <= non_zero_thread:
                    cp[y][x] = 0
                # cp[y][x] = np.count_nonzero(values)
        return cp
        
    @staticmethod
    def closing(image, non_zero_thread=1):
        cp = image.copy()
        for y in range(len(image)):
            for x in range(len(image[0])):
                if image[y][x] != 0:
                    continue
                offsets = [ (-1, 0),
                   (0, -1),           (0, 1),
                    (1, 0),
                ]
                values = []
                for offset in offsets:
                    _y = y + offset[0]
                    _x = x + offset[1]
                    if 0 <= _y < len(image) and 0 <= _x < len(image[0]):
                        values.append(image[_y][_x])
                    else:
                        values.append(0)
                if np.count_nonzero(values) >= non_zero_thread:
                    cp[y][x] = 2
                # cp[y][x] = np.count_nonzero(values)
        return cp
    