#include <stdio.h>

void selectionSort(int A[], int n) {
    for (int i=0; i<n-1; i++){
        int k = i;
        for (int j=i+1; j<n; j++){
            if (A[j]<A[k]){
                k = j;
            }
        }
        int t = A[i];
        A[i] = A[k];
        A[k] = t;
    }
	return;
}

void evenOddSelectionSort(int A[], int n){
    int even[n];
    int odd[n];
    
    int n_even = 0;
    int n_odd = 0;
    
    selectionSort(A,n);
    
    for (int i=0; i<n; i++){
        if (A[i]%2 == 0){
            // add A[i] to even
            even[n_even] = A[i];
            n_even++;
        }
	    else {
	        // add A[i] to odd
	        odd[n_odd] = A[i];
	        n_odd++;
	    }
    }
    
    printf("Sorted even numbers: "); 
    for (int i = 0; i < n_even; i++) {
        printf("%d ", even[i]);
    } 
    
    printf("\nSorted odd numbers: "); 
    for (int i = 0; i < n_odd; i++) {
        printf("%d ", odd[i]);
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

	evenOddSelectionSort(A, n);
}




