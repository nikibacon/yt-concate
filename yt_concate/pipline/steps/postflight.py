from .step import Step


class Postflight(Step):
    def process(self, data, inputs, utils, logger):
        # print('in Postflight')
        logger.warning('----------------in Postflight-------------------------')