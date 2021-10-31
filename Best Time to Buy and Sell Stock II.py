class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i = 0
        j = 0
        continueEndFlag = False
        profit = 0
        while i < len(prices):
            if prices[i] == max(prices):
                i += 1
                continue
            buySelector = prices[i]
            j = i + 1
            while j < len(prices):
                sellSelector = prices[j]
                k = j + 1
                # определяем конец последовательности чисел (+1 каждый день)
                while k < len(prices):
                    sellSelector2 = prices[k]
                    if sellSelector2 == prices[k-1] + 1:
                        continueEndFlag = [True, k]
                        k += 1

                if buySelector + 1 < sellSelector and continueEndFlag == False:
                    # buy!
                    thisProfit = sellSelector - buySelector
                    profit += thisProfit
                    i = j + 1
                    break
                elif continueEndFlag:
                    j = continueEndFlag[1]
                    continueEndFlag = False
                    continue

                else:
                    j += 1
            else:
                i += 1

        return profit

    # def mapMaxProfit(self, prices: list[int]) -> list:
    #     profit2 = 0
    #     # делаем таблицу и представляем её в виде двухмерного списка,
    #     # во внешнем списке по индексу 0 всегда цена на данный день
    #     mainTableList = prices
    #
    #     for i in range(0, len(mainTableList)):
    #         # создаем вложенный список, индеекс 0 - цена на этот день, длина списка = длине списка цен на день,
    #         # значение во сложенном списке - профит от продажи акции в день по соотв.индексу
    #         # (помним, что продать вчера нельзя)
    #         mainTableList[i] = list(mainTableList[i:len(mainTableList)])
    #
    #     for i in range(0, len(mainTableList)):
    #
    #         for j in range(0, len(mainTableList[i])):
    #
    #     return mainTableList


if __name__ == '__main__':
    # Solution().maxProfit([1, 2, 3, 4, 5])
    print(Solution().maxProfit([1, 2, 3, 4, 5]))
# [7,1,5,3,6,4]
