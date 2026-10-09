def main():
    print("Calculadora de litros utlizados (12km por litro)")
    print("................................................")

    tempo = float(input("Digite o TEMPO da viagem .: "))

    velocidade = float(input("Digite a Velocidade media : "))

    distancia = velocidade * tempo
    litros = distancia/12

    print()
    print("...............................................")
    print()

    print(f"a velocidade media ficou em .: {velocidade} km/h")
    print(f"o tempo total ficou em ......: {tempo} horas")
    print(f"a distancia percorrida foi ..: {distancia} km")
    print(f"foram gastos ................: {litros:.2f} Litros")

    print()
    print("Aperte <enter> para continuar")
    input()

if __name__ == "__main__":
    main()
