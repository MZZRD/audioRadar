import numpy as np
import time
from scipy.io import wavfile
import sounddevice as sd


def main():
    fs, data = wavfile.read('../wav/sin_1000Hz_3sec.wav')
    print("Start")
    t = time.time()
    sd.play(data, fs)
    sd.wait()
    print("Done, dt={0}".format(time.time()-t))


if __name__ == '__main__':
    main()
