def mysum(*numbers):
    _sum = 0
    for num in numbers:
        _sum += num
    return _sum


if __name__ == "__main__":
    # 测试函数
    def test_mysum():
        # 测试1：普通用法
        assert mysum(1, 2, 3) == 6, "mysum(1,2,3) should be 6"

        # 测试2：更多参数
        assert mysum(10, 20, 30, 40, 50) == 150, "mysum(10..50) should be 150"

        # 测试3：只有一个参数
        assert mysum(7) == 7, "mysum(7) should return 7 itself"

        # 测试4：负数
        assert mysum(-1, -2, 5) == 2, "should handle negative numbers"

        # 测试5：浮点数
        assert mysum(1.5, 2.5, 3.0) == 7.0, "should handle floats"

        # 测试6：无参数 → 应该返回 0
        assert mysum() == 0, "mysum() with no args should return 0"

        # 测试7：单个 0
        assert mysum(0) == 0, "mysum(0) == 0"

        # 测试8：很多 0
        assert mysum(0, 0, 0, 0) == 0, "all zeros sum to 0"

        print("all tests passed!")


    # 运行测试
    test_mysum()