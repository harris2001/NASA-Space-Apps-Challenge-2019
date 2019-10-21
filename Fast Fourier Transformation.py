import numpy as np
import random
import cv2

def universe_noise(image,prob):
    f = 300
    y0 = 254
    def y(t):
        y = int(y0 + 2*np.pi *f * t)
        return y
    '''Importing random sound in image
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob*2:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
                '''
    output = np.zeros(image.shape,np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.randint(1,100)
            if rdn < 30:
                #print (output[i][j])
                ii = int(i)
                jj = int(j)
                yy = int(y(ii*(image.shape[1])+jj))
                output[i][j] = output[i][j] + yy
                #print (output[i][j])
            else:
                output[i][j] = image[i][j]
    return output

#from PIL import Image
#img = Image.open('a.png').convert('L')
#img.save('a-gray.png')

image = cv2.imread('sattelite.png', 0)
noise_img = universe_noise(image,0.05)
cv2.imwrite('photo2.png', noise_img)


import matplotlib.pyplot as plt

im = plt.imread('photo2.png').astype(float)

plt.figure()
plt.imshow(im)
plt.title('Original image')

from scipy import fftpack
im_fft = fftpack.fft2(im)


def plot_spectrum(im_fft):
    from matplotlib.colors import LogNorm
    # A logarithmic colormap
    plt.imshow(np.abs(im_fft), norm=LogNorm(vmin=5))
    plt.colorbar()

plt.figure()
plot_spectrum(im_fft)
plt.title('Fourier transform')

keep_fraction = 0.1
im_fft2 = im_fft.copy()

r, c = im_fft2.shape

im_fft2[int(r*keep_fraction):int(r*(1-keep_fraction))] = 0

im_fft2[:, int(c*keep_fraction):int(c*(1-keep_fraction))] = 0

plt.figure()
plot_spectrum(im_fft2)
plt.title('Filtered Spectrum')

im_new = fftpack.ifft2(im_fft2).real

plt.figure()
plt.imshow(im_new)
plt.title('Reconstructed Image')
