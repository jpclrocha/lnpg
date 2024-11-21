#include <stdio.h>

void main()
{
    int n;
    scanf("%d", &n);

    int matriz[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &matriz[i]);
    }

    int count = 0;

    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            // Condition to check if the element is duplicate or not
            if (matriz[i] == matriz[j])
            {
                count++;
                break;
            }
        }
    }

    printf("%d", n - count);
}