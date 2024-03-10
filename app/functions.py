from pytube import YouTube

class StreamInfo:
    def __init__(self, type, resolution, quality, has_audio, subtype, filesize, url):
        self.type = type
        self.resolution = resolution
        self.quality = quality
        self.has_audio = has_audio
        self.subtype = subtype
        self.filesize = filesize
        self.url = url

def get_video_info(video_url):
    try:
        yt = YouTube(video_url)

        video_info = {
            'video_title': yt.title,
            'views': yt.views,
            'publish_date': yt.publish_date,
            'thumbnail_url': yt.thumbnail_url,
            'streams_info': []
        }

        all_streams = yt.streams.all()

        video_streams = []
        audio_streams = []

        for stream in all_streams:
            if "video" in stream.mime_type:
                video_streams.append(stream)
            elif "audio" in stream.mime_type:
                audio_streams.append(stream)

        # Sort video streams by resolution in descending order
        video_streams.sort(key=lambda x: int(x.resolution[:-1]) if x.resolution else 0, reverse=True)

        # Sort audio streams by quality in descending order
        audio_streams.sort(key=lambda x: int(x.abr.split('kbps')[0]), reverse=True)

        # Sort video streams by type (With Audio first), then by resolution
        for stream in sorted(video_streams, key=lambda x: (x.includes_audio_track, int(x.resolution[:-1]) if x.resolution else 0), reverse=True):
            if stream.includes_audio_track:
                stream_info = StreamInfo(
                    type="Video (With Audio)",
                    resolution=stream.resolution,
                    quality=stream.abr,
                    has_audio=True,
                    subtype=stream.subtype,
                    filesize=format(stream.filesize / (1024 * 1024), '.2f'),
                    url=stream.url
                )
            else:
                stream_info = StreamInfo(
                    type="Video (No Audio)",
                    resolution=stream.resolution,
                    quality=None,
                    has_audio=False,
                    subtype=stream.subtype,
                    filesize=format(stream.filesize / (1024 * 1024), '.2f'),
                    url=stream.url
                )
            video_info['streams_info'].append(stream_info)

        for stream in audio_streams:
            stream_info = StreamInfo(
                type="Audio",
                resolution=stream.resolution,
                quality=stream.abr,
                has_audio=True,
                subtype=stream.subtype,
                filesize=format(stream.filesize / (1024 * 1024), '.2f'),
                url=stream.url
            )
            video_info['streams_info'].append(stream_info)

        return video_info

    except Exception as e:
        return {'error': str(e)}
