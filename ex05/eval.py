class Evaluator:
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return(-1)
        mapped = zip(coefs, words)
        somme = 0
        for words in mapped:
            somme += words[0] * len(words[1])
        return(somme)

    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return(-1)
        somme = 0
        for i, j in enumerate(words):
            somme += len(j) * coefs[i]
        return(somme)
