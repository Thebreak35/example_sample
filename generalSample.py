from sampleType1 import SampleType1
from sampleType2 import SampleType2


TYPE_1 = 1
TYPE_2 = 2

class GeneralSample(SampleType1, SampleType2):
    def __init__(self, sample_type: int):
        super().__init__()
        self.sample_instance = self._create_sample_instance_depend_on_type(sample_type)

    def sample(self):
        self.sample_instance.sample()

    def _create_sample_instance_depend_on_type(self, sample_type: int):
        if sample_type == TYPE_1:
            return SampleType1()
        if sample_type == TYPE_2:
            return SampleType2()

if __name__ == '__main__':
    a = GeneralSample(sample_type=1)
    b = GeneralSample(sample_type=2)
    c = GeneralSample(sample_type=2)

    print(a.sample())
    print(b.sample())
    print(c.sample())
    print(type(a.sample_instance) == type(c.sample_instance))
    print(type(b.sample_instance) == type(c.sample_instance))