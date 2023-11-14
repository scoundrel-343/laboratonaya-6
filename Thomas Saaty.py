def main():
    try:
        n = int(input("Введите количество критериев: "))
    except ValueError:
        print("! Ошибка ! Введите правильное значение")
        return
    a=[[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i == j):
                a[i][j] = 1.00
            else:
                print("Введите отношение критерия", i+1 , "к критерию", j+1,"(число в десятичном формате)")
                a[i][j] = float(input())
    sums = ves(a,n)
    for i in range(n):
        print(round(sums[i], 2))

#Функция для вычисления весовых коэффициентов
def ves(a,n):
    sum = 0.0
    sums = [0.0] * n
    for i in range(n):
        for j in range(n):
            sum += a[i][j]
    for i in range(n):
        for j in range(n):
            sums[i] += a[i][j]
    for i in range(n):
        sums[i] = sums[i] / sum
    return sums

if __name__ == "__main__":
    main()