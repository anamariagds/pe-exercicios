def diz_codigo(a):
     return ord(a)
    
def main():
    n = str(input("Digite apenas um caracter: "))
    car = diz_codigo(n)

    print(f'O código do caractere {n} é {car}')

if __name__=='__main__':
    main()
