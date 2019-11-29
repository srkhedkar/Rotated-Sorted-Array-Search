class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        start =  0
        end = len(A) -1        
        pivot = 0
        while ( start <= end ):
            middle = (start + end) // 2
            if (middle == 0):
                break
            if A[middle] < A[middle-1]:
                pivot = middle
                break
            elif A[middle] < A[end]:
                end = middle -1
            elif A[middle] > A[end]:
                start = middle + 1       
      

        if (A[pivot] <= B <= A[len(A) -1]):
            start = pivot
            end = len(A) -1

            while ( start <= end ):
                middle = (start + end) // 2
                if (A[middle] == B):
                    return middle
                if A[middle] < B:
                    start = middle + 1                    
                else:
                    end = middle -1

        if ( A[0] <= B <= A[pivot-1]):
            start = 0
            end = pivot-1
            while ( start <= end ):
                middle = (start + end) // 2
                if (A[middle] == B):
                    return middle
                if A[middle] < B:
                    start = middle + 1                    
                else:
                    end = middle -1           
        
        return -1