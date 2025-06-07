#include <stdio.h>

int main() {
    int n, m;
    int pageFaults = 0;

    printf("Enter the length of reference string: ");
    scanf("%d", &n);
    int refString[n];

    printf("Enter total frames: ");
    scanf("%d", &m);
    int frames[m];

    printf("Enter the reference string: ");
    for (int i = 0; i < n; ++i)
        scanf("%d", &refString[i]);

    for (int i = 0; i < m; ++i)
        frames[i] = -1;

    for (int i = 0; i < n; ++i) {
        int found = 0;
        for (int j = 0; j < m; ++j) {
            if (frames[j] == refString[i]) {
                found = 1;
                break;
            }
        }
        if (!found) {
            int index = -1, farthest = -1;
            for (int j = 0; j < m; ++j) {
                int k;
                for (k = i; k < n; ++k) {
                    if (frames[j] == refString[k]) {
                        if (k > farthest) {
                            farthest = k;
                            index = j;
                        }
                        break;
                    }
                }
                if (k == n) {
                    index = j;
                    break;
                }
            }
            frames[index] = refString[i];
            ++pageFaults;
        }
    }

    printf("Page Faults = %d\n", pageFaults);

    return 0;
}
