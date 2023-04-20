from moviepy.video.io.VideoFileClip import VideoFileClip
from src.utils import Utils


class VideoTrimmer:
    def __init__(self, logging, event):
        self.logging = logging
        self.video_list = event['toTrim']

    def work_queue(self):
        try:
            for video in self.video_list:
                _path = video['path']
                _seconds = video['secondsToRemove']
                is_new_video_file = video['isNew'] if 'isNew' in video else False
                new_text_to_append = video['textToAppend'] if 'textToAppend' in video else '_new_trim'
                self.logging.info(f'Trimming {_seconds} seconds from {_path}')
                self._trim_video(video['path'], video['secondsToRemove'], is_new_video_file, new_text_to_append)
        except Exception as err:
            self.logging.error(f'Error! issues with filename: {_path} - {err}')

    def _trim_video(self, video_path, seconds_to_remove, is_new_video_file, new_text_to_append):
        try:

            # Load the video file
            clip = VideoFileClip(video_path)

            # Get the duration of the video clip
            duration = clip.duration

            # Calculate the new end time of the video
            new_end_time = duration - seconds_to_remove

            # Trim the video clip from the seconds stamp to the end of the movie
            trimmed_clip = clip.subclip(seconds_to_remove, duration)

            new_video_path = Utils.rename_file(video_path, new_text_to_append=new_text_to_append) if is_new_video_file else video_path

            # Write the trimmed clip to a new file
            trimmed_clip.write_videofile(new_video_path)

        except Exception as err:
            raise
