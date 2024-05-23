import subprocess

def change_video_metadata(video_path, title=None, audio_name=None, subtitle_name=None):
    """
    Change metadata of a video file using ffmpeg.
    
    Args:
        video_path (str): Path to the input video file.
        title (str): New title for the video.
        audio_name (str): New name for the audio track.
        subtitle_name (str): New name for the subtitle track.
        
    Returns:
        bool: True if metadata was successfully changed, False otherwise.
    """
    command = ['ffmpeg', '-i', video_path]
    
    if title:
        command.extend(['-metadata', f'title={title}'])
    
    if audio_name:
        command.extend(['-metadata', f'audio_name={audio_name}'])
        
    if subtitle_name:
        command.extend(['-metadata', f'subtitle_name={subtitle_name}'])
    
    command.append('-c:v')
    command.append('copy')
    command.append('-c:a')
    command.append('copy')
    command.append('-c:s')
    command.append('copy')
    command.append('output.mp4')
    
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to change metadata - {e}")
        return False

# Example usage:
if __name__ == "__main__":
    video_path = 'input.mp4'
    title = 'New Title'
    audio_name = 'New Audio Name'
    subtitle_name = 'New Subtitle Name'
    
    success = change_video_metadata(video_path, title, audio_name, subtitle_name)
    if success:
        print("Metadata changed successfully!")
    else:
        print("Failed to change metadata.")
