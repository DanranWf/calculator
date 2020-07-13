# from api.calculator import CalT

from api.calculator import CalTool
import pytest


class TestCal:

    def setup_class(self):    #============ only runs one time during the execution of the class
        print('class operation')
    def setup(self):
        self.cal=CalTool()
        print('before prepa')

    # @pytest.mark.parametrize(a,b,result,['2,2,4','3,1,4','5,9,14'])
    def test_add(self):
        print('add method')
        sum=self.cal.add()
        print(sum)

    @pytest.mark.parametrize("a,b", [(2, 2), (3, 1), (5, 9)])
    def test_add9(self, a, b):
        print('add method')
        sum = self.cal.addlwj(a,b)
        print(sum)
        # assert self.cal.add() == 9
        # assert self.cal.add(2,7)==9        #==============why methond cant be sent with args

    # @pytest.mark.parametrize()
    def test_minus(self):
        self.cal.minus()

    def test_multi(self):
        self.cal.multi()

    def test_div(self):
        self.cal.div()

    def test_lwj(self):
        aa=CalTool(16,12)    #========== new agrs should be sent to the class parenthesis
        aa.lwj()             #========== method cant be be sent with args

    def teardown(self):
        print('afer clean work')

    # @pytest.mark.parametrize(
    #     "test_input,expected",
    #     [
    #         ("3+5", 8),
    #         pytest.param("1+7", 8, marks=pytest.mark.basic),
    #         pytest.param("2+4", 6, marks=pytest.mark.basic, id="basic_2+4"),
    #         pytest.param(
    #             "6*9", 42, marks=[pytest.mark.basic, pytest.mark.xfail], id="basic_6*9"
    #         ),
    #     ],
    # )
    # def test_eval(test_input, expected):
    #     assert eval(test_input) == expected

    def teardown_class(self):    #============ only runs one time during the execution of the class
        print('class ends work')

