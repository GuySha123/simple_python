from icecream import ic
from helper.calcs import sumTwoNums,multTwoNums,divTwoNums, sumThreeNums, multThreeNums,biggerNum
from helper.name import welcome

if __name__ == '__main__':
    ic(sumTwoNums(2, 4))
    ic(multTwoNums(2, 4))
    ic(divTwoNums(2, 4))
    ic(sumThreeNums(2, 4, 5))
    ic(multThreeNums(2, 4, 5))
    ic(biggerNum(5,6))
    ic(welcome('Guy'))