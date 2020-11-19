from .step import Step
from yt_concate.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils, logger):
        search_word = inputs['search_word']

        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue

            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)
                    # Found是新的物件 裡面會有yt, caption, time
        # print(f'searching files: {len(found)}')
        logger.info(f'searching files: {len(found)}')
        return found
