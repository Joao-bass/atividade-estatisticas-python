import statistics

def calcular_estatisticas(preco):
    media = statistics.mean(preco)
    print('Media = ',media)
    moda = statistics.mode(preco)
    print('Moda = ',moda)
    mediana = statistics.median(preco)
    print('Mediana = ',mediana)
    variancia = statistics.pvariance(preco)
    print('Variancia = ',variancia)
    desvio = statistics.pstdev(preco)
    print('Desvio Padrão = ',desvio)
    ampli = max(preco) - min(preco)
    print('Amplitude = ', ampli)
    
