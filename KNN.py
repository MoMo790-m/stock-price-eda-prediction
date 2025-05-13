def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])
    idx += 1
    res = []

    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx+1])
        idx += 2

        a = list(map(int, data[idx:idx+n]))
        idx += n

        h = list(map(int, data[idx:idx+n]))
        idx += n

        max_len = 0
        left = 0
        fruit_sum = 0

        for right in range(n):
            if right > 0 and h[right - 1] % h[right] != 0:
                left = right
                fruit_sum = 0

            fruit_sum += a[right]

            while fruit_sum > k:
                fruit_sum -= a[left]
                left += 1

            max_len = max(max_len, right - left + 1)

        res.append(str(max_len))

    print("\n".join(res))

solve()

