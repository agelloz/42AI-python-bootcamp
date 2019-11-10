
class Evaluator:
    @staticmethod
    def zip_evaluate(coefs: list=[], words: list=[]):
        if len(coefs) != len(words):
            print(-1)
            return
        iterator = zip(coefs, words)
        res_list = list(iterator)
        res = 0
        for res_tuple in res_list:
            res += res_tuple[0] * len(res_tuple[1])
        print(res)

    @staticmethod
    def enumerate_evaluate(coefs: list=[], words: list=[]):
        if len(coefs) != len(words):
            print(-1)
            return
        res_list = enumerate(words)
        i = 0
        res = 0
        for res_tuple in res_list:
            res += coefs[i] * len(res_tuple[1])
            i += 1
        print(res)

