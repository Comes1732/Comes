video_file = "D:/Program Files (x64)/demo/Comes/Djanger/test_views/static/gbqq.mp4"
format_type = "D:/Program Files (x64)/demo/Comes/Djanger/test_views/StaticOut/"


import os
import sys
from moviepy.editor import AudioFileClip, VideoFileClip
import pyaudio
import wave
from typing import Optional, List

class AudioProcessor:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
    
    def extract_audio_from_video(self, video_path: str, output_path: Optional[str] = None) -> str:
        """从视频提取音频为MP3格式"""
        if not os.path.isfile(video_path):
            raise FileNotFoundError(f"视频文件不存在: {video_path}")
        
        if output_path is None:
            output_path = os.path.splitext(video_path)[0] + ".mp3"
        
        try:
            with VideoFileClip(video_path) as video:
                audio = video.audio
                audio.write_audiofile(output_path, codec="mp3")
            return output_path
        except Exception as e:
            raise RuntimeError(f"音频提取失败: {str(e)}")
    
    def batch_extract_audio(self, input_dir: str, output_dir: str, extensions: List[str] = [".mp4", ".avi"]):
        """批量提取文件夹内视频的音频"""
        if not os.path.isdir(input_dir):
            raise NotADirectoryError(f"输入目录无效: {input_dir}")
        
        os.makedirs(output_dir, exist_ok=True)
        
        for root, _, files in os.walk(input_dir):
            for file in files:
                if any(file.lower().endswith(ext) for ext in extensions):
                    video_path = os.path.join(root, file)
                    rel_path = os.path.relpath(root, input_dir)
                    output_subdir = os.path.join(output_dir, rel_path)
                    os.makedirs(output_subdir, exist_ok=True)
                    
                    output_file = os.path.splitext(file)[0] + ".mp3"
                    output_path = os.path.join(output_subdir, output_file)
                    
                    try:
                        self.extract_audio_from_video(video_path, output_path)
                        print(f"成功处理: {video_path} -> {output_path}")
                    except Exception as e:
                        print(f"处理失败 {video_path}: {str(e)}")
    
    def record_audio(self, output_path: str, duration: int = 5, 
                    sample_rate: int = 44100, channels: int = 2) -> str:
        """录制音频并保存为WAV格式"""
        frames = []
        stream = self.audio.open(format=pyaudio.paInt16,
                                channels=channels,
                                rate=sample_rate,
                                input=True,
                                frames_per_buffer=1024)
        
        print("录音中...")
        for _ in range(0, int(sample_rate / 1024 * duration)):
            frames.append(stream.read(1024))
        
        stream.stop_stream()
        stream.close()
        
        with wave.open(output_path, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))
        
        return output_path
    
    def convert_audio_format(self, input_path: str, output_path: str, 
                           output_format: str = "mp3") -> str:
        """转换音频文件格式"""
        if not os.path.isfile(input_path):
            raise FileNotFoundError(f"输入文件不存在: {input_path}")
        
        try:
            with AudioFileClip(input_path) as audio:
                audio.write_audiofile(output_path, codec=output_format)
            return output_path
        except Exception as e:
            raise RuntimeError(f"格式转换失败: {str(e)}")
    
    def __del__(self):
        self.audio.terminate()

def main():
    processor = AudioProcessor()
    print("音频处理器已初始化")
    
    # 示例用法
    try:
        # 从视频提取音频
        processor.extract_audio_from_video("input.mp4", "output.mp3")
        
        # 批量处理
        # processor.batch_extract_audio("videos", "audios")
        
        # 录音
        # processor.record_audio("recording.wav", duration=10)
        
        # 格式转换
        # processor.convert_audio_format("input.wav", "output.mp3")
        pass
    except Exception as e:
        print(f"发生错误: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
