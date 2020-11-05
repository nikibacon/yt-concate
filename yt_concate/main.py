from yt_concate.pipline.steps.get_video_list import GetVideoList
from yt_concate.pipline.steps.download_captions import DownloadCaptions
from yt_concate.pipline.steps.preflight import Preflight
from yt_concate.pipline.steps.postflight import Postflight
from yt_concate.pipline.steps.step import StepException
from yt_concate.pipline.pipeline import Pipeline
from yt_concate.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()




