def factorial_recursive(n):
    # 如果 n 是 0 或 1，返回 1（基礎情況）
    if n == 0:
        return 1
    # 遞迴調用自身來計算階乘
    return n * factorial_recursive(n - 1)

# 測試範例
print(factorial_recursive(5))  # 輸出應為 120