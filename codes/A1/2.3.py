import soundfile as sf
from scipy import signal
#read .wav file
#reading input signal which is a soundfile
input_signal,fs = sf.read(r"C:\Users\DHANUSH PITTALA\Downloads\filter_codes_Sound_Noise.wav")

#sampling frequency of Input signal
sampl_freq=fs

#order of the filter
order = 4

#cutoff frquency 4kHz

cutoff_freq=4000.0
#digital frequency

Wn= 2*cutoff_freq/sampl_freq

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order,Wn, 'low')

#filtering  the input signal with butterworth filter

output_signal = signal.filtfilt(b, a,input_signal)

# output signal = signal.lfilter(b, a,input signal)
# write the output signal into .wav file

sf.write(r'C:\Users\DHANUSH PITTALA\Downloads\Sound With ReducedNoise.wav',output_signal, fs)
