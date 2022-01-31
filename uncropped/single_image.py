import imageio
import matplotlib.pyplot as plt

pic = imageio.imread('/Users/jonathanlifferth/Documents/Health/beard_color/small/2022-01-09_11-18cb.jpg')
plt.figure(figsize=(5, 5))
plt.imshow(pic)
