from moviepy.editor import AudioFileClip
import librosa

def convert_to_audio():
	origin_mp4 = AudioFileClip("D:\\document\\video\\DJI_0459_006.MP4")
	print(type(origin_mp4))
	origin_mp4.write_audiofile('D:\\document\\video\\DJI_0459_006.wav')

def audio_inspect():
	audio, freq = librosa.load('D:\\document\\video\\DJI_0459_006.wav')
	print(f"audio: {audio} and audio shape: {audio.shape} \n freq: {freq}")
	print(f"audio type: {type(audio)} \n freq type: {type(freq)}")
	time = len(audio)/freq
	print(time)


if __name__ == "__main__":
	audio_inspect()
