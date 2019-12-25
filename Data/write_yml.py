import os
import pytest
import yaml


def get_sum_data():
    sum_list = []
    with open("../Data/value2.yaml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        for i in data.values():
            sum_list.append(tuple(i.values()))

    return sum_list


# print(get_sum_data())

#
class TestSum:
    @pytest.mark.parametrize("a,b,c", get_sum_data())
    def test_sum(self, a, b, c):
        print("{}+{}={}".format(a, b, c))
        assert a + b == c
