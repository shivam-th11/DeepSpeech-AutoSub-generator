import ffmpeg

def merge_video_and_subtitles(video_file, subtitle_file, output_file):
    ffmpeg.input(video_file).output(output_file, vf='subtitles='+subtitle_file, strict='experimental').run()

video_file = 'video.mp4'
subtitle_file = 'subtitle_file.srt'
output_file = 'output_video_with_subtitles.mp4'

merge_video_and_subtitles(video_file, subtitle_file, output_file)