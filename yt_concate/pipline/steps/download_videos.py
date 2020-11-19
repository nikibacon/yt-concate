from .step import Step
import time

from multiprocessing import Process
from threading import Thread
import concurrent.futures
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils, logger):
        start = time.time()
        # data 就是剛剛searching完的found物件 現在需要yt物件有分類在found裡 把他集合起來再拿來使用 易讀
        yt_set = set([found.yt for found in data])
        # 因為一個影片有可能會出現很多次同一個word 所以found物件或許會有重複的yt(url是同一個影片),所以用set把list裡重複的刪掉
        logger.info(f'videos to download= {len(yt_set)}')
        processes = []

        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
            for yt in yt_set:
                url = yt.url
                if utils.video_file_exists(yt):
                    logger.debug(f'found existing video file for {url}, skipping')
                    continue
                logger.debug('downloading' + url)

                process = executor.submit(self.download_videos, yt, utils, logger)
                processes.append(process)

        end = time.time()
        logger.info(f'download videos took {end - start} seconds')
        return data

    def download_videos(self, yt, utils, logger):
        url = yt.url
        try:
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)

        except AttributeError as e:
            # print(f"Attribute err when downloading video': {e} for {yt.url}")
            logger.warning(f"Attribute err when downloading video': {e} for {yt.url}")
        except KeyError as e:
            # print(f"Key err when downloading video: {e} for {yt.url}")
            logger.warning(f"Key err when downloading video: {e} for {yt.url}")
        except RegexMatchError as e:
            # print(f"Pytube err when downloading video: {e} for {yt.url}")
            logger.warning(f"Pytube err when downloading video: {e} for {yt.url}")


