# !pip install opencv-python

import numpy as np # https://numpy.org/ja/

class myLabeling:
    """ 特定の値以外はすべて0にする。
        Args:
        2d_numarray (<class 'numpy.ndarray'>): 2次元配列の画像データ
        value: フィルターする値
    """
    @staticmethod
    def filter(src, value):
        copied = src.copy();
        return np.where(copied != value, 0, value)

    """ maskに値が入っている場所の値のみをsrcから取得
    """
    @staticmethod
    def mask(src, mask):
        copied = mask.copy()
        for y in range(len(copied)):
            for x in range(len(copied[0])):
                if mask[y][x] != 0:
                    mask[y][x] = src[y][x]
        return copied

    """ maskのうち値が0以外のものsrcの上に上書きする。
    """
    @staticmethod
    def overwrite(src, mask):
        copied = src.copy()
        for y in range(len(copied)):
            for x in range(len(copied[0])):
                if mask[y][x] != 0:
                    copied[y][x] = mask[y][x]
        return copied

    """ 8近傍をチェックして、画像データと最大のラベルと最大のサイズをかえす
    """
    @staticmethod
    def cv_labeling(src):
        import cv2
        copied = src.copy()
        for y in range(len(copied)):
            for x in range(len(copied[0])):
                if copied[y][x] > 1:
                    copied[y][x] = 1
                else:
                    copied[y][x] = 0
        nLabels, labelImages, data, center = cv2.connectedComponentsWithStats(copied)
        max_label = 1
        for label in range(nLabels - 1):
            x, y, w, h, size = data[label + 1]
            if size > data[max_label][4]:
                max_label = label + 1
        x, y, w, h, size = data[max_label]
        return {'labelMap': labelImages, 'max_label': max_label, 'max_label_cnt': size, 'data': data[max_label]}

    def preprocess_detail(image):
        labelObject = myLabeling.cv_labeling(image)
        filtered = myLabeling.filter(labelObject['labelMap'], labelObject['max_label'])
        masked = myLabeling.mask(image, filtered)
        flatted = np.where(image.copy() > 0, 1, 0)
        masked_flat = np.where(masked > 0, 2, 0)
        img = myLabeling.overwrite(flatted, masked_flat)
        labelObject['labelMap'] = img
        return labelObject
        
    def preprocess(image):
        labelObject = myLabeling.cv_labeling(image)
        filtered = myLabeling.filter(labelObject['labelMap'], labelObject['max_label'])
        masked = myLabeling.mask(image, filtered)
        flatted = np.where(image.copy() > 0, 1, 0)
        masked_flat = np.where(masked > 0, 2, 0)
        img = myLabeling.overwrite(flatted, masked_flat)
        # imgに labelObject['labelMap'] や filteredを入れることで、処理の経過を見ることができます。
        return img

    def simple(image):
        labelObject = myLabeling.cv_labeling(image)
        filtered = myLabeling.filter(labelObject['labelMap'], labelObject['max_label'])
        masked = myLabeling.mask(image, filtered)
        # img = myLabeling.overwrite(flatted, masked_flat)
        img = masked
        # imgに labelObject['labelMap'] や filteredを入れることで、処理の経過を見ることができます。
        return img
        