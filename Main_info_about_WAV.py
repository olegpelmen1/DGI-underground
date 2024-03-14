
import struct


def print_INFO(data):
    chunkId = struct.unpack_from('i', data, offset=0)
    chunkSize = struct.unpack_from('i', data, offset=4)
    format = struct.unpack_from('i', data, offset=8)
    subchunk1Id = struct.unpack_from('i', data, offset=12)
    subchunk1Size = struct.unpack_from('i', data, offset=16)
    audioFormat = struct.unpack_from('h', data, offset=20)
    numChannels = struct.unpack_from('h', data, offset=22)
    sampleRate = struct.unpack_from('i', data, offset=24)
    byteRate = struct.unpack_from('i', data, offset=28)
    blockAlign = struct.unpack_from('h', data, offset=32)
    bitsPerSample = struct.unpack_from('h', data, offset=34)
    subchunk2Id = struct.unpack_from('i', data, offset=36)
    subchunk2Size = struct.unpack_from('i', data, offset=40)
    a = []
    b = ['chunkId', 'chunkSize', 'format', 'subchunk1Id', 'subchunk1Size', 'audioFormat', 'numChannels', 'sampleRate', 'byteRate', 'blockAlign', 'bitsPerSample', 'subchunk2Id', 'subchunk2Size']
    for i in range(13):
        a =  [chunkId, chunkSize, format, subchunk1Id, subchunk1Size, audioFormat, numChannels, sampleRate, byteRate, blockAlign, bitsPerSample, subchunk2Id, subchunk2Size]
    for i in range(13):
        print(b[i],' ',a[i])
    return a    



class Wav():
    chunkId = 0
    chunkSize = 0
    format = 0
    subchunk1Id = 0
    subchunk1Size = 0
    audioFormat = 0
    numChannels = 0
    sampleRate = 0
    byteRate = 0
    blockAlign = 0
    bitsPerSample = 0
    subchunk2Id = 0
    subchunk2Size = 0

    def __init__(self, chunkIdd, chunkSized, formatd, subchunk1Idd, subchunk1Sized, audioFormatd, numChannelsd, sampleRated, byteRated, blockAlignd, bitsPerSampled, subchunk2Idd, subchunk2Sized):
        self.chunkId = chunkIdd
        self.chunkSize = chunkSized
        self.format = formatd
        self.subchunk1Id = subchunk1Idd
        self.subchunk1Size = subchunk1Sized
        self.audioFormat = audioFormatd
        self.numChannels = numChannelsd
        self.sampleRate = sampleRated
        self.byteRate = byteRated
        self.blockAlign = blockAlignd
        self.bitsPerSample = bitsPerSampled
        self.subchunk2Id = subchunk2Idd
        self.subchunk2Size = subchunk2Sized

with open("1.wav", "rb") as file:
    data = file.read()
    Info = print_INFO(data)
    Some_WAV = Wav(Info[0],Info[1],Info[2],Info[3],Info[4],Info[5],Info[6],Info[7],Info[8],Info[9],Info[10],Info[11],Info[12])
    if Some_WAV.audioFormat == 0:
        print('class empy')
    else:
        print('All Nice man! Class created\nFor example byteRate:', Some_WAV.byteRate)




    




