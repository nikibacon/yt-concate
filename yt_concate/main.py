import sys
import getopt
import logging

from yt_concate.pipline.steps.preflight import Preflight
from yt_concate.pipline.steps.get_video_list import GetVideoList
from yt_concate.pipline.steps.initialize_yt import InitializeYT
from yt_concate.pipline.steps.download_captions import DownloadCaptions
from yt_concate.pipline.steps.read_cpation import ReadCaption
from yt_concate.pipline.steps.search import Search
from yt_concate.pipline.steps.download_videos import DownloadVideos
from yt_concate.pipline.steps.edit_video import EditVideo
from yt_concate.pipline.steps.clean_dir import CleanDir
from yt_concate.pipline.steps.postflight import Postflight
from yt_concate.pipline.steps.step import StepException
from yt_concate.pipline.pipeline import Pipeline
from yt_concate.utils import Utils


def config_logger(level):

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
    file_handler = logging.FileHandler('ty_concate.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    if level == 'NOTSET':
        stream_handler.setLevel(logging.NOTSET)
    elif level == 'DEBUG':
        stream_handler.setLevel(logging.DEBUG)
    elif level == 'WARNING':
        stream_handler.setLevel(logging.WARNING)
    elif level == 'ERROR':
        stream_handler.setLevel(logging.ERROR)
    elif level == 'CRITICAL':
        stream_handler.setLevel(logging.CRITICAL)

    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


def main():

    channel_id = 'UCKSVUHI9rbbkXhvAXK-2uxA'
    search_word = 'incredible'
    limit = 20
    cleanup = False
    level = 'INFO'

    short_opts = 'hi:s:l:c:v:'
    long_opts = 'help channel_id= search_word= limit= cleanup= level='.split()
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError:
        print('python main.py -i <channel_id> -s <search_word> -l <limit> -c <cleanup> -v <level>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('python main.py -i <channel_id> -s <search_word> -l <limit> -c <cleanup> -v <level>')
            sys.exit(0)
        elif opt in ('-i', '--channel_id'):
            channel_id = arg
        elif opt in ('-s', '--search_word'):
            search_word = arg
        elif opt in ('-l', '--limit'):
            limit = int(arg)
        elif opt in ('-c', '--cleanup'):
            if arg == 'True' or 'true':
                cleanup = True
        elif opt in ('-v', '--level'):
            level = arg

    if not channel_id or not search_word or not limit:
        print('python main.py -c <channel_id> -s <search_word> -l <limit>')
        sys.exit(2)

    inputs = {
        'channel_id': channel_id,
        'search_word': search_word,
        'limit': limit,
        'cleanup': cleanup,
        'level': level,
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
        CleanDir(),
        Postflight(),
    ]
    logger = config_logger(level)
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils, logger)


if __name__ == '__main__':
    main()




