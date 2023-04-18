from moviepy.video.io.VideoFileClip import VideoFileClip
from src.utils import Utils


class VideoTrimmer:
    def __init__(self, logging, event):
        self.logging = logging
        self.video_list = event['video_list_to_trim']

    def work_queue(self):
        try:
            for idx, video in self.video_list:
                _path = video['path']
                _seconds = video['seconds_to_remove']
                self.logging.info(f'Item {idx} - Trimming {_seconds} from {_path}')
                self._trim_video(video['path'], video['seconds_to_remove'], False)
        except Exception as err:
            self.logging.error(f'Error! issues with filename: {_path} - {err}')

    def _trim_video(self, video_path, seconds_to_remove, is_new_video_file=False):

        # Load the video file
        clip = VideoFileClip(video_path)

        # Get the duration of the video clip
        duration = clip.duration

        # Calculate the new end time of the video
        new_end_time = duration - seconds_to_remove

        # Trim the video clip from the beginning to the new end time
        trimmed_clip = clip.subclip(0, new_end_time)

        new_video_path = Utils.rename_file(video_path, new_text_to_append='_new_trim') if is_new_video_file else video_path

        # Write the trimmed clip to a new file
        trimmed_clip.write_videofile(new_video_path)
