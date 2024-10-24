
import numpy as np  # นำเข้า numpy สำหรับการทำงานกับ matrices

# ฟังก์ชันการใช้ Set
def set_operations():
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    # การรวมกันของสองเซต
    union_set = set_a | set_b
    # การหาจุดร่วมของสองเซต
    intersection_set = set_a & set_b
    # การหาความแตกต่างของสองเซต
    difference_set = set_a - set_b

    print("Union of A and B:", union_set)
    print("Intersection of A and B:", intersection_set)
    print("Difference of A and B:", difference_set)

# ฟังก์ชันการใช้ Sequences
def sequence_operations(n):
    sequence = [i for i in range(1, n + 1)]  # สร้างลำดับของตัวเลขจาก 1 ถึง n
    print(f"Sequence from 1 to {n}:", sequence)
    return sequence

# ฟังก์ชันการใช้ Sums
def sum_of_sequence(sequence):
    total_sum = sum(sequence)  # คำนวณผลรวมของลำดับที่สร้าง
    print(f"Sum of the sequence: {total_sum}")
    return total_sum

# ฟังก์ชันการใช้ Matrices
def matrix_operations():
    matrix_a = np.array([[1, 2], [3, 4]])  # สร้างเมทริกซ์ A
    matrix_b = np.array([[5, 6], [7, 8]])  # สร้างเมทริกซ์ B

    matrix_sum = matrix_a + matrix_b  # การบวกเมทริกซ์
    matrix_product = np.dot(matrix_a, matrix_b)  # การคูณเมทริกซ์

    print("Matrix A:\n", matrix_a)
    print("Matrix B:\n", matrix_b)
    print("Sum of A and B:\n", matrix_sum)
    print("Product of A and B:\n", matrix_product)

# ฟังก์ชันหลักในการเรียกใช้ฟังก์ชันทั้งหมด
def main():
    print("---- Set Operations ----")
    set_operations()

    print("\n---- Sequence Operations ----")
    sequence = sequence_operations(5)  # สร้างลำดับจาก 1 ถึง 5

    print("\n---- Sum of Sequence ----")
    sum_of_sequence(sequence)

    print("\n---- Matrix Operations ----")
    matrix_operations()

# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    main()
