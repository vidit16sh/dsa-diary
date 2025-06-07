
// #include<stdio.h>

// int main() 
// {
//     int n,m;
//     int pageHits=0, pageMiss=0;
    
//     printf("Enter the length of reference string: ");
//     scanf("%d",&n);
//     int refString[n];
    
//     printf("Enter total frames: ");
//     scanf("%d",&m);
//     int frames[m];

//     for(int i=0;i<n;i++)
//     {
//         int x;
//         printf("Enter the page request %d: ",i+1);
//         scanf("%d",&x);

//         refString[i]=x;
//     }

//     for(int i=0;i<m;i++)
//     {
//         frames[i]=-1;
//     }

//     for(int i=0;i<n;i++)
//     {
//         int pageFound = 0;
//         for(int j=0;j<m;j++)
//         {
//             if(refString[i] == frames[j])
//             {
//                 pageHits+=1;
//                 pageFound = 1;
//                 break;
//             }
//         }

//         if(!pageFound)
//         {
//             int index = 0;
//             int page = i+1;

//             for(int j=0;j<m;j++)
//             {
//                 int k;
//                 for(k=i-1;k>=0;k--)
//                 {
//                     if(refString[k] == frames[j])
//                     {
//                         if(k < page)
//                         {
//                             page = k;
//                             index = j;
//                         }
//                         break;
//                     }
//                 }
//                 if(k==-1)
//                 {
//                     index=j;
//                     break;
//                 }
//             }
//             frames[index] = refString[i];
//             pageMiss++;
//         }
//     }

//     printf("Pages Hits = %d, Page Miss = %d", pageHits, pageMiss);

// return 0;
// }


#include <stdio.h>

int main() {
    int n, m;
    int pageHits = 0, pageMiss = 0;

    printf("Enter the length of reference string: ");
    scanf("%d", &n);
    int refString[n];

    printf("Enter total frames: ");
    scanf("%d", &m);
    int frames[m];
    int pageLastUsed[m]; // Track the index of the last use for each page

    for (int i = 0; i < n; i++) {
        printf("Enter the page request %d: ", i + 1);
        scanf("%d", &refString[i]);
    }

    for (int i = 0; i < m; i++) {
        frames[i] = -1;
        pageLastUsed[i] = -1; // Initialize all pages as never used
    }

    for (int i = 0; i < n; i++) {
        int pageFound = 0;

        // Check if page already in memory
        for (int j = 0; j < m; j++) {
            if (refString[i] == frames[j]) {
                pageHits++;
                pageFound = 1;
                pageLastUsed[j] = i; // Update the index of last use for the page
                break;
            }
        }

        // If page not found in memory
        if (!pageFound) {
            // Find the least recently used page
            int leastUsedIndex = 0;
            for (int j = 1; j < m; j++) {
                if (pageLastUsed[j] < pageLastUsed[leastUsedIndex]) {
                    leastUsedIndex = j;
                }
            }

            // Replace least recently used page with new page
            frames[leastUsedIndex] = refString[i];
            pageMiss++;
            pageLastUsed[leastUsedIndex] = i; // Update the index of last use for the page
        }
    }

    printf("Pages Hits = %d, Page Miss = %d", pageHits, pageMiss);

    return 0;
}
