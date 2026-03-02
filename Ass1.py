class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x) 

    def pop(self):
        if not self.is_empty():
            return self.items.pop() 
        return None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None 

    def is_empty(self):
        return len(self.items) == 0 

    def size(self):
        return len(self.items) 

# Global counter for Fibonacci calls ---

naive_calls = 0

def factorial(n):
    if n < 0: return None 
    if n == 0 or n == 1: return 1 
    return n * factorial(n - 1)

def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1: return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def binary_search(arr, key, low, high, stack):
    if low > high:
        return -1 
    mid = (low + high) // 2
    stack.push(mid)  
    
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1, stack)
    else:
        return binary_search(arr, key, mid + 1, high, stack)

def run_tests():
    print("--- Part A: Factorial ---")
    n = int(input("Enter Fibonacci number n :"))   
    print(f"Factorial({n}) = {factorial(n)}")

    print("\n--- Part B: Fibonacci (Naive) ---")
    global naive_calls
    n = int(input("Enter Fibonacci number n (non-negative integer): "))
    naive_calls = 0
    ans_naive = fib_naive(n)
    print(f"n={n}: Result={ans_naive} | Total Recursive Calls={naive_calls}")

    print("\n--- Part C: Binary Search Trace ---")
    test_arr = [1, 3, 5, 7, 9, 11, 13]
    key_to_find = 7
    search_stack = StackADT()
    
    res = binary_search(test_arr, key_to_find, 0, len(test_arr)-1, search_stack)
    print(f"Searching for {key_to_find} in {test_arr}")
    print(f"Result Index: {res}")
    
    print("Mid-indices pushed to Stack (Path of search):", end=" ")
    while not search_stack.is_empty():
        print(search_stack.pop(), end=" ")
    print()

if __name__ == "__main__":
    run_tests()