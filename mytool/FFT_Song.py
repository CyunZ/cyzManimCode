import numpy as np
from pydub import AudioSegment
import struct
from scipy.fftpack import fft,ifft,fftfreq,rfft,irfft
from scipy import signal
import math


def getSongData(wavfile_name):
    """
    取得声波数据
    """
    song = AudioSegment.from_wav(wavfile_name)
    nchannels = song.channels #声道数
    sample_width = song.sample_width #位深
    Fs = song.frame_rate #采样率
    N = int(song.frame_count()) #采样点数量

    y = [0]*N
    for i in range(N):
        val = song.get_frame(i)
        left = val[0:sample_width] #取左声道数据 默认双声道 位深16bit
        v = struct.unpack('h',left)[0]
        y[i] = v
    return y,Fs,N

def getSongFormula(wavfile_name,filter_amplitude=50):
    """
    返回音频的余弦函数表达式参数
        wavfile_name:文件名
        filter_amplitude:过滤掉该强度以下的频率
        返回值 [(强度,频率,相位(角度))]
        例如 [(75, 44, -132), (56, 47, 110)]
    """
    y,Fs,N = getSongData(wavfile_name)
    yy = fft(y)
    abs_yf = np.abs(yy)

    max_fre = Fs // 2
    frequencys = [0] * (max_fre)
    params = []

    for i in range(max_fre):
        index_i_hz = i * N // Fs # 波形的频率 = index * Fs / N，倒推计算索引：index = 波形频率 * N / Fs
        frequencys[i] = round( abs_yf[index_i_hz] * 2.0/N , 2)   # 弦波分量的振幅放大了N/2倍
        if frequencys[i] > filter_amplitude: # 过滤幅值低于指定值的频率信号
            if i == 0: # 直流分量
                frequencys[i] /= 2
            else : # 交流分量
                phase =  round( np.angle( yy[index_i_hz],True ) , 2)  # 计算相位
                params.append((frequencys[i],i,phase))
                # print("{}cos(2pi x {} + {}/180pi)".format(frequencys[i],i,phase))
    
    return params

def getSongFormula2(wavfile_name,filter_amplitude=50):
    """
    返回音频的余弦函数表达式参数
        wavfile_name:文件名
        filter_amplitude:过滤掉该强度以下的频率
        返回值 [(强度,频率,相位(角度))]
        例如 [(75, 44, -132), (56, 47, 110)]
    """
    y,Fs,N = getSongData(wavfile_name)
    yy = fft(y)
    abs_yf = np.abs(yy)

    max_fre = Fs / 2
    params = []
    dc = abs_yyl[0] /N # 直流分量 被放大了N倍

    for i in range(1,len(abs_yf)):
        freq = i*Fs/N   # 频率 = index * Fs / N
        if freq > max_fre: # 最大频率不会超过采样频率的一般
            break
        amplitude = abs_yyl[i] * 2.0/N
        if amplitude > filter_amplitude: # 过滤幅值低于指定值的频率信号
                phase =  np.angle( yy[index_i_hz],True ) # 计算相位
                params.append((amplitude,freq,phase))
    return params

def getWavDataFormula(data,Fs,filter_amplitude=50):
    """
    返回音频的余弦函数表达式参数
        data: 数据数组
        Fs:采样率
        filter_amplitude:过滤掉该强度以下的频率
        返回值 [(强度,频率,相位(角度))]
        例如 [(75, 44, -132), (56, 47, 110)]
    """
    # song = AudioSegment.from_wav(wavfile_name)
    # nchannels = song.channels #声道数
    # sample_width = song.sample_width #位深
    # Fs = song.frame_rate #采样率
    # N = int(song.frame_count()) #采样点数量
    N = len(data)
    #取得声波数据
    y = data

    yy = fft(y)
    abs_yf = np.abs(yy)

    max_fre = Fs / 2
    params = []
    dc = abs_yyl[0] /N # 直流分量 被放大了N倍

    for i in range(1,len(abs_yf)):
        freq = i*Fs/N   # 频率 = index * Fs / N
        if freq > max_fre: # 最大频率不会超过采样频率的一般
            break
        amplitude = abs_yyl[i] * 2.0/N
        if amplitude > filter_amplitude: # 过滤幅值低于指定值的频率信号
                phase =  np.angle( yy[index_i_hz],True ) # 计算相位
                params.append((amplitude,freq,phase))
    
    return params