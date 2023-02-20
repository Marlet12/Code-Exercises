#include <stdio.h>

void InsertionSort(int A[], int n) {
    for (int i=1; i<n; i++) {
        int j = i-1;
        int t = A[i];
        
        while (j>=0 && t<A[j]) {
            A[j+1] = A[j];
            j = j-1;
        }
        
        A[j+1] = t;
    }
	return;
}

void printArray(int A[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", A[i]);
    printf("\n");
}

int main(int argc, const char * argv[]) {
	int A[100];
	int n = 0;

	printf("Values of A separated by spaces (non-number to stop):");
	
	while (scanf("%d", &A[n]) == 1) {
		n++;
	}

	scanf("%*s");
	
	printf("Result: ");
	
	InsertionSort(A,n);
	printArray(A,n);

}



