import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepare video data for exporting"""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video to a folder"""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec"""

    def prepare_export(self, video_data):
        print('Preparing video for lossless export.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video in lossless format to {folder}')


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec"""

    def prepare_export(self, video_data):
        print('Preparing video for H.264 export.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video in H.264 format to {folder}')


class AudioExporter(ABC):

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepare audio data for exporting"""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio to a folder"""


class WAVAudioExporter(AudioExporter):
    """WAV audio exporting codec"""

    def prepare_export(self, video_data):
        print('Preparing video for WAV export.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video in WAV format to {folder}')


class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec"""

    def prepare_export(self, audio_data):
        print('Preparing audio for audio export.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting audio in AAC format to {folder}')


class ExporterFactory(ABC):
    """Factory that represents a combination of video and audio codecs."""

    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter belonging to this factory"""

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter belonging to this factory"""


class FastExporter(ExporterFactory):

    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):

    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


def read_factory() -> ExporterFactory:
    factories = {
        'low': FastExporter(),
        'master': MasterQualityExporter()
    }

    while True:
        export_quality = input("Enter desired output quality (low, master)")
        if export_quality in factories:
            return factories[export_quality]
        else:
            print(f"Unknown output quality option: {export_quality}")


factory = read_factory()

# get the exporters
video_exporter = factory.get_video_exporter()
audio_exporter = factory.get_audio_exporter()

# do the exports
folder = pathlib.Path('usr/tmp/video')
video_exporter.do_export(folder)
audio_exporter.do_export(folder)
