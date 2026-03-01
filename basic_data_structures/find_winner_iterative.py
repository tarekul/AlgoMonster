def find_winner(n: int, k: int) -> int:
    winner = 0
    
    for i in range(2, n + 1):
        winner = (winner + k) % i
    
    return winner
    

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    res = find_winner(n, k)
    print(res)