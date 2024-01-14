from moviepy.video.io.VideoFileClip import VideoFileClip
import math

def split_video(input_file, chunk_duration):
    video_clip = VideoFileClip(input_file)

    total_duration = video_clip.duration
    chunk_count = math.ceil(total_duration / chunk_duration)

    for i in range(chunk_count):
        start_time = i * chunk_duration
        end_time = min((i + 1) * chunk_duration, total_duration)

        chunk = video_clip.subclip(start_time, end_time)
        output_file = f"chunk_{i + 1}.mp4"
        chunk.write_videofile(output_file, codec="libx264")

    video_clip.close()

if __name__ == "__main__":
    input_file = input("Enter the path to the video file: ")
    chunk_duration = float(input("Enter the chunk duration in minutes: "))

    split_video(input_file, chunk_duration)
