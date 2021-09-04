import speech_recognition as sr
import moviepy.editor as me

# VIDEO_FILE = "C:/Users/mt204e/Videos/2021-09-03 11-52-22.mkv"
VIDEO_FILE = "C:\\Users\\Brandon\\Documents\\Other\\temp\\post_0231.mp4"
OUTPUT_AUDIO_FILE = "converted.wav"
OUTPUT_TEXT_FILE = "recognized.txt"
# try:
#     print('starting try...')
#     video_clip = me.VideoFileClip(r"{}".format(VIDEO_FILE))
#     video_clip.audio.write_audiofile(r"{}".format(OUTPUT_AUDIO_FILE))
#     recognizer =  sr.Recognizer()
#     audio_clip = sr.AudioFile("{}".format(OUTPUT_AUDIO_FILE))
#     with audio_clip as source:
#         audio_file = recognizer.record(source)
#     print("Please wait ...")
#     result = recognizer.recognize_google(audio_file)
#     with open(OUTPUT_TEXT_FILE, 'w') as file:
#         file.write(result)
#         print("Speech to text conversion successful.")
# except Exception as e:
#     print("Attempt failed -- ", e)
# try:
print('starting try...')
video_clip = me.VideoFileClip(r"{}".format(VIDEO_FILE))
video_clip.audio.write_audiofile(r"{}".format(OUTPUT_AUDIO_FILE))
recognizer =  sr.Recognizer()
audio_clip = sr.AudioFile("{}".format(OUTPUT_AUDIO_FILE))
with audio_clip as source:
    audio_file = recognizer.record(source)
print("Please wait ...")
result = recognizer.recognize_google(audio_file)
with open(OUTPUT_TEXT_FILE, 'w') as file:
    file.write(result)
    print("Speech to text conversion successful.")
# except Exception as e:
#     print("Attempt failed -- ", e)
    
#     pip install SpeechRecognition