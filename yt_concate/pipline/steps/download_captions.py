import os
import time
from threading import Thread
from multiprocessing import Process
import concurrent.futures
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from .step import Step
from yt_concate.settings import CAPTIONS_DIR
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils, logger):
        start = time.time()
        logger.info('downloading caption.......')
        # download the package by:  pip install pytube
        processes = []

        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
            for yt in data:
                logger.debug('downloading caption' + str(yt.id))
                # print('downloading caption for', yt.id)
                if utils.caption_file_exists(yt):
                    logger.debug('found existing caption file' + str(yt.id))
                    # print('found existing caption file')
                    continue
                process = executor.submit(self.download_captions, yt, utils, logger)
                processes.append(process)
                # print('executor:' + executor.__str__() + 'process:' + process.__str__())

        end = time.time()
        # print('took', end - start, 'second')
        # file_cnt = 0
        # for name in os.listdir(CAPTIONS_DIR):
        #     if os.path.isfile(os.path.join(CAPTIONS_DIR, name)):
        #         file_cnt += 1
        file_cnt = len([name for name in os.listdir(CAPTIONS_DIR) if os.path.isfile(os.path.join(CAPTIONS_DIR, name))])
        logger.info(f'---------------downloading caption done....cost time: {str(end - start)} ,Caption files: {file_cnt}')
        return data

    def download_captions(self, yt, utils, logger):
        try:
            source = YouTube(yt.url)
            en_caption = source.captions.get_by_language_code('en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            # print(en_caption_convert_to_srt)
            text_file = open(yt.caption_filepath, "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        except AttributeError as e:
            logger.warning(f"Attribute err: {e} for {yt.url}")
            # print(f"Attribute err: {e} for {yt.url}")
        except KeyError as e:
            logger.warning(f"Key err: {e} for {yt.url}")
            # print(f"Key err: {e} for {yt.url}")
        except RegexMatchError as e:
            logger.warning(f"Pytube err: {e} for {yt.url}")
            # print(f"Pytube err: {e} for {yt.url}")




