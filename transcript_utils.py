import speech_recognition as sr
import moviepy.editor as me
import os

# from sms
from sms.file_system_utils import file_system_utils as fsu


OUTPUT_AUDIO_FILE = "converted.wav"
VID_FILE_EXT_L = ['.mp4']


def vid_file_to_transcript_txt(vid_file_path, output_txt_file_path):
    print('starting try...')
    video_clip = me.VideoFileClip(r"{}".format(vid_file_path))
    video_clip.audio.write_audiofile(r"{}".format(OUTPUT_AUDIO_FILE))
    recognizer =  sr.Recognizer()
    audio_clip = sr.AudioFile("{}".format(OUTPUT_AUDIO_FILE))
    with audio_clip as source:
        audio_file = recognizer.record(source)
    print("Please wait ...")
    result = recognizer.recognize_google(audio_file)
    with open(output_txt_file_path, 'w') as file:
        file.write(result)
    print("Speech to text conversion successful.")
    
    
def vid_file_to_transcript_txt_for_all_vid_nested_vid_files_in_dir(in_dir_path, out_dir_path):
    
    fsu.make_dir_if_not_exist(out_dir_path)
    
    file_path_l = fsu.get_dir_content_l(in_dir_path, object_type = 'file', content_type = 'abs_path', recurs_dirs = True)
    
    print(file_path_l)
    
    vid_file_path_l = []
    for file_path in file_path_l:
        
        ext = fsu.get_extention(file_path)
        
        if ext in VID_FILE_EXT_L:
            vid_file_path_l.append(file_path)
            
    print(vid_file_path_l)
    
    
    for vid_file_path in vid_file_path_l:
        print('')
        print('    Trying to create transcript for :  ', vid_file_path)
        print('')
        
        vid_name = fsu.get_basename_from_path(vid_file_path, include_ext = False)
        
        transcript_file_path = os.path.join(out_dir_path, vid_name + '__transcript.txt')
        
        vid_file_to_transcript_txt(vid_file_path, transcript_file_path)
        
    
    
    
    
if __name__ == "__main__":
#     vid_file_path = "C:\\Users\\Brandon\\Documents\\Other\\temp\\post_0231.mp4"
#     output_txt_file_path = "recognized.txt"
#     
#     vid_file_to_transcript_txt(vid_file_path, output_txt_file_path)
    



    
    # in_dir_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\transcript_tools_big_data_test\\test_in_dir"
    # out_dir_path = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\transcript_tools_big_data_test\\test_out_dir"
    in_dir_path = 'C:/tools/p/confluence_vids/version_control'
    out_dir_path = 'C:/tools/p/confluence_vids/version_control/transcripts'
    
    vid_file_to_transcript_txt_for_all_vid_nested_vid_files_in_dir(in_dir_path, out_dir_path)
    
    
    
    print('done')
    
    
    
        
