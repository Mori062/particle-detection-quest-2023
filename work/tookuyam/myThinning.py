# 画像の細線化処理
# 参考：https://www.frontier.maxell.co.jp/blog/posts/23.html
import cv2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd # https://pandas.pydata.org/

class MyThinning:

    def thinning(self, image): # image: numpy
        is_Delete = True
        pre_image = image.copy()
        count = 0
        while is_Delete == True:
            is_Delete = False
            new_image = pre_image.copy()
            for y in range(len(pre_image)):
                for x in range(len(pre_image[0])):
                    if new_image[y][x] != 0 and self.is_delete(new_image, x, y):
                        is_Delete = True
                        new_image[y][x] = 0
            pre_image = new_image
            count += 1
            if count > 1000:
                break
        return pre_image
                    
    def is_delete(self, image, x, y):
        filters = self.get_filters()
        for filter in filters:
            if self.is_filterMatch(image, x, y, filter):
                return True
        return False
        
    def is_filterMatch(self, image, x, y, filter): # filter は 3x3のみ
        offset_y = -1
        for row in filter:
            offset_x = -1
            for filter_pixel in row:
                target_x = x + offset_x
                target_y = y + offset_y
                if self.is_in_range(image, target_x, target_y):
                    target_pixel = image[target_y][target_x]
                else:
                    target_pixel = 0 # 外側のピクセル
                if filter_pixel == -1:
                    pass
                elif filter_pixel == 0 and target_pixel != 0:
                    return False
                elif filter_pixel == 1 and target_pixel == 0:
                    return False
                offset_x += 1
            offset_y += 1
        return True
        
    def is_in_range(self, image, x, y):
        if 0 <= x < len(image[0]) and 0 <= y < len(image):
            return True
        return False
    
    def get_filters(self):
        return [ # -1:任意の値、 0: 0にマッチ、 1: ０以外にマッチ
            [ # 1
                [0, 0, -1],
                [0, 1, 1],
                [-1, 1, 1],
            ],
            [ # 2
                [-1, 0, 0],
                [1, 1, 0],
                [1, 1, -1],
            ],
            [ # 3
                [-1, 1, 1],
                [0, 1, 1],
                [0, 0, -1],
            ],
            [ # 4
                [1, 1, -1],
                [1, 1, 0],
                [-1, 0, 0],
            ],
            [ # 5
                [0, -1, 1],
                [0, 1, 1],
                [0, -1, 1],
            ],
            [ # 6
                [0, 0, 0],
                [-1, 1, -1],
                [1, 1, 1],
            ],
            [ # 7
                [1, 1, 1],
                [-1, 1, -1],
                [0, 0, 0],
            ],
            [ # 8
                [1, -1, 0],
                [1, 1, 0],
                [1, -1, 0],
            ],
            [ # 9
                [0, 0, 0],
                [0, 1, 1],
                [0, 0, 1],
            ],
            # [ # 10
            #     [0, 0, 0],
            #     [0, 1, 0],
            #     [1, 1, 0],
            # ],
            # [ # ori 10 - 1
            #     [1, 0, 0],
            #     [1, 1, 0],
            #     [0, 0, 0],
            # ],
            # [ # ori 10 - 2
            #     [0, 1, 1],
            #     [0, 1, 0],
            #     [0, 0, 0],
            # ],
            # [ # 11
            #     [0, 0, 0],
            #     [0, 1, 0],
            #     [0, 1, 1],
            # ],
            # [ # 12
            #     [0, 0, 0],
            #     [1, 1, 0],
            #     [1, 0, 0],
            # ],
            # [ # ori 12 - 1
            #     [1, 1, 0],
            #     [0, 1, 0],
            #     [0, 0, 0],
            # ],
            # [ # ori 12 - 2
            #     [0, 0, 1],
            #     [0, 1, 1],
            #     [0, 0, 0],
            # ],
            [ # ori 1 - 1
                [0, 0, 0],
                [0, 1, 1],
                [-1, 1, -1],
            ],
            [ # ori 1 - 2
                [-1, 0, 0],
                [1, 1, 0],
                [-1, 1, 0],
            ],
            [ # ori 1 - 3
                [-1, 1, -1],
                [1, 1, 0],
                [0, 0, 0],
            ],
            [ # ori 1 - 4
                [0, 1, -1],
                [0, 1, 1],
                [0, 0, -1],
            ],
            [ # ori 2 - 1
                [0, 0, 0],
                [1, 1, 0],
                [-1, 1, -1],
            ],
            [ # ori 2 - 2
                [-1, 1, 0],
                [1, 1, 0],
                [-1, 0, 0],
            ],
            [ # ori 2 - 3
                [-1, 1, -1],
                [0, 1, 1],
                [0, 0, 0],
            ],
            [ # ori 2 - 4
                [0, 0, -1],
                [0, 1, 1],
                [0, 1, -1],
            ],
            # [ # ori 3 - 1
            #     [0, 0, -1],
            #     [0, 1, 1],
            #     [0, 1, -1],
            # ],
            # [ # ori 3 - 2
            #     [0, 0, 0],
            #     [1, 1, 0],
            #     [0, 1, 0],
            # ],
            # [ # ori 3 - 3
            #     [0, 1, 0],
            #     [1, 1, 0],
            #     [0, 0, 0],
            # ],
            # [ # ori 3 - 4
            #     [0, 1, 0],
            #     [0, 1, 1],
            #     [0, 0, 0],
            # ],
        ]