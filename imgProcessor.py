import scipy.io.wavfile as wav

from PIL import Image
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

fs, data = wav.read('wavfile8.wav')
data_crop = data[20*fs:21*fs]
resample = 6
data = data[::resample]
fs = fs/resample

def hilbert(data):
    analytical_signal = signal.hilbert(data)
    amplitude_envelope = np.abs(analytical_signal)
    return amplitude_envelope

data_am = hilbert(data)


width = int(fs/2)
w, h = width, int(data_am.shape[0]/width)
image = Image.new('RGB', (w, h))
x, y = 0, 0
for p in range(data_am.shape[0]):
    lum = int(data_am[p]/32 - 32)
    if lum < 0: lum = 0
    if lum > 255: lum = 255
    image.putpixel((x, y), (lum, lum, lum))
    x += 1
    if x >= w:
        if (y % 50) == 0:
            print(f"Line saved {y} of {h}")
        x = 0
        y += 1
        if y >= h:
            break
image = image.resize((w, 4*h))
plt.imshow(image)
plt.show()