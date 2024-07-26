def tinh_tong(n):
    """
    Tính tổng tất cả các số nguyên từ 1 đến n

    Args:
    n (int): Giới hạn trên của dãy số nguyên
    Returns:
    int: Tổng các số nguyên từ 1 đến n
    """
    
    if n < 1:
        raise ValueError("n phải là một số nguyên dương")

    tong = 0
    for i in range(1, n + 1):
        # Cộng số hiện tại vào tổng
        tong += i  

    return tong

def main():
    # Định nghĩa giới hạn trên của dãy số
    n = 10
    try:
        # Tính tổng và in kết quả
        ket_qua = tinh_tong(n)
        print(f"Tổng các số nguyên từ 1 đến {n} là: {ket_qua}")
    except ValueError as e:
        # Xử lý lỗi nếu n không phải là số nguyên dương
        print(e)

if __name__ == "__main__":
    main()
