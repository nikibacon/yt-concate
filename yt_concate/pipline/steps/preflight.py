from .step import Step


class Preflight(Step):
    def process(self, data, inputs, utils, logger):
        # print('in Preflight')
        utils.create_dirs()
        logger.info('--------------------in Preflight---------------------')
