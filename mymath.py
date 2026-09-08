def factorial_recursive(n):
    """
    팩토리얼 함수 (재귀)
    :param n: 입력 값
    :return: 팩토리얼 결과
    """
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)

def factorial_iterative(n):
    """
    팩토리얼 함수 (반복)
    :param n: 입력 값
    :return: 팩토리얼 결과
    """
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result