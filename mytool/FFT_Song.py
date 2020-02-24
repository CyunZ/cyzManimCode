import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
import struct
from scipy.fftpack import fft,ifft,fftfreq,rfft,irfft
from scipy import signal
import math



def getSongFormula(wavfile_name,filter_amplitude=50):
    """
    返回音频的余弦函数表达式参数
        wavfile_name:文件名
        filter_amplitude:过滤掉该强度以下的频率
        返回值 [(强度,频率,相位(角度))]
        例如 [(75, 44, -132), (56, 47, 110)]
    """
    song = AudioSegment.from_wav(wavfile_name)
    nchannels = song.channels #声道数
    sample_width = song.sample_width #位深
    Fs = song.frame_rate #采样率
    N = int(song.frame_count()) #采样点数量
    
    #取得声波数据
    y = [0]*N
    for i in range(N):
        val = song.get_frame(i)
        left = val[0:2] #取左声道数据 默认双声道 位深16bit
        v = struct.unpack('h',left)[0]
        y[i] = v

    yy = fft(y)
    abs_yf = np.abs(yy)

    max_fre = Fs // 2
    frequencys = [0] * (max_fre)
    params = []

    for i in range(max_fre):
        index_i_hz = i * N // Fs # 波形的频率 = index * Fs / N，倒推计算索引：index = 波形频率 * N / Fs
        frequencys[i] = int( round( abs_yf[index_i_hz] * 2.0/N ) )  # 弦波分量的振幅放大了N/2倍
        if frequencys[i] > filter_amplitude: # 过滤赋值低于50的频率信号
            if i == 0: # 直流分量
                frequencys[i] /= 2
            else : # 交流分量
                phase = int( round( np.angle( yy[index_i_hz],True ) ) ) # 计算相位
                params.append((frequencys[i],i,phase))
                # print("{}cos(2pi x {} + {}/180pi)".format(frequencys[i],i,phase))
    
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

    max_fre = Fs // 2
    frequencys = [0] * (max_fre)
    params = []

    for i in range(max_fre):
        index_i_hz = i * N // Fs # 波形的频率 = index * Fs / N，倒推计算索引：index = 波形频率 * N / Fs
        frequencys[i] = int( round( abs_yf[index_i_hz] * 2.0/N ) )  # 弦波分量的振幅放大了N/2倍
        if frequencys[i] > filter_amplitude: # 过滤赋值低于50的频率信号
            if i == 0: # 直流分量
                frequencys[i] /= 2
            else : # 交流分量
                phase = int( round( np.angle( yy[index_i_hz],True ) ) ) # 计算相位
                params.append((frequencys[i],i,phase))
                # print("{}cos(2pi x {} + {}/180pi)".format(frequencys[i],i,phase))
    
    return params,frequencys