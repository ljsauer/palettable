import cv2
import numpy as np
from sklearn.cluster import MiniBatchKMeans


class ColorPalette:
    def __init__(self, image, n_sig=5, position='topRight',
                 orient='horz', size=.3):
        self.image = image
        self.W = image.shape[1]
        self.H = image.shape[0]
        self.n_sig = n_sig
        self.sig_colors = []
        self.palette = []
        self.size = int(self.W * size)
        self.position = position
        self.orient = orient

    def get_significant_colors(self, centroids):
        print("Getting significant colors. . .")
        # Get the number of different clusters and calculate histogram
        hist = cv2.calcHist([self.image], [2], None, [256], [0, 256])
        hist = sorted(list(hist), reverse=True, key=lambda x: x[0])
        color_data = list(zip(hist, centroids))
        color_data = [(percent, color) for (percent, color) in color_data]
        for percent, color in color_data:
            self.sig_colors.append([int(c) for c in color])

    def create_palette(self):
        print("Creating a palette. . .")
        for idx, color in enumerate(self.sig_colors):
            img = np.zeros((self.size, self.size, 3), dtype=np.uint8)
            img[:] = self.sig_colors[idx]
            self.palette.append(img)

    def add_palette_to_image(self):
        print("Adding a palette to your image. . .")
        temp = cv2.resize(self.image, (self.W//10, self.H//10))
        reshape = temp.reshape(temp.shape[0] * temp.shape[1], 3)
        cluster = MiniBatchKMeans(n_clusters=self.n_sig,
                                  batch_size=100,
                                  max_iter=10).fit(reshape)
        self.get_significant_colors(cluster.cluster_centers_)
        self.create_palette()
        if self.orient == 'horz':
            palette = cv2.hconcat(self.palette)
            palette = cv2.resize(palette, (int(self.size*1.5),
                                           int(self.size//2.5)))
        elif self.orient == 'vert':
            palette = cv2.vconcat(self.palette)
            palette = cv2.resize(palette, (int(self.size//2.5),
                                           int(self.size*1.5)))

        if self.position == 'topRight':
            self.image[0:palette.shape[0],
                       self.W - palette.shape[1]:self.W] = palette
        elif self.position == 'bottomRight':
            self.image[self.H - palette.shape[0]:self.H,
                       self.W - palette.shape[1]:self.W] = palette
        elif self.position == 'topLeft':
            self.image[0:palette.shape[0], 0:palette.shape[1]] = palette
        elif self.position == 'bottomLeft':
            self.image[self.H - palette.shape[0]:self.H,
                       0:palette.shape[1]] = palette

    def show_image_with_palette(self, output):
        self.add_palette_to_image()
        temp_image = cv2.resize(self.image, (self.W//5, self.H//5))
        cv2.imshow("Made palettable", temp_image)
        key = cv2.waitKey(0) & 0xFF
        if key == ord('s'):
            filename = input("Please enter the filename under which to save"
                             " this image: ")
            print("Saving as:", filename+'.jpg')
            cv2.imwrite(output + filename + '.jpg', self.image)


"""
barcode generator:
hist = cv2.calcHist([self.image], [2], None, [256], [0, 256])
color_data = [color for color in hist]
for color in color_data:
    self.sig_colors.append([int(c) for c in color])
"""
