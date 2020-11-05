from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    # 不要笨笨的一個一個的去生成 可以用for loop
    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            try:
                # 要接收上個步驟return的東西 接完在傳給下一個step ex.字幕()才拿得到list
                data = step.process(data, inputs, utils)
            except StepException as e:
                print('Exception happened:', e)
                break
