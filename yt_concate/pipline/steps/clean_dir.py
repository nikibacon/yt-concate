import os

from .step import Step
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR


class CleanDir(Step):
    def process(self, data, inputs, utils, logger):
        if inputs['cleanup']:
            try:
                os.rmdir(VIDEOS_DIR)
                os.rmdir(CAPTIONS_DIR)
            except OSError as e:
                # print(e)
                logger.warning(f"OSError : {e} ")
            else:
                logger.info("The directory is deleted successfully")
        else:
            logger.info("ALL FILES EXIST")
