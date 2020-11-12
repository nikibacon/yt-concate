from yt_concate.pipline.steps.preflight import Preflight
from yt_concate.pipline.steps.get_video_list import GetVideoList
from yt_concate.pipline.steps.initialize_yt import InitializeYT
from yt_concate.pipline.steps.download_captions import DownloadCaptions
from yt_concate.pipline.steps.read_cpation import ReadCaption
from yt_concate.pipline.steps.search import Search
from yt_concate.pipline.steps.download_videos import DownloadVideos
from yt_concate.pipline.steps.edit_video import EditVideo
from yt_concate.pipline.steps.postflight import Postflight
from yt_concate.pipline.steps.step import StepException
from yt_concate.pipline.pipeline import Pipeline
from yt_concate.utils import Utils


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word':'incredible',
        'limit':20,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()




