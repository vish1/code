#include <stdio.h>
#define Y_MAX 4
#define X_MAX 4

int matrix[X_MAX][Y_MAX] ={{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};

int print_spiral(int x_min, int y_min, int x_max, int y_max)
{
    int i,j;
    x_min--;
    while((x_max-x_min>=0)||(y_max-y_min>=0))
    {
        for(i=++x_min,j=y_min;i<=x_max;i++) printf("%d ",matrix[i][j]);
        for(j=++y_min,i=x_max;j<=y_max;j++) printf("%d ",matrix[i][j]);
        for(i=--x_max,j=y_max;i>=x_min;i--) printf("%d ",matrix[i][j]);
        for(j=--y_max,i=x_min;j>=y_min;j--) printf("%d ",matrix[i][j]);
    }
}

int print_matrix(int x_min, int y_min, int x_max, int y_max)
{
    int i,j;
    for(i=x_min;i<=x_max;i++)
    {
        for(j=y_min;j<=y_max;j++)
            printf("%d ",matrix[i][j]);
        printf("\n");
    }
}

int main()
{
    print_matrix(0,0,(X_MAX-1),(Y_MAX-1));
    print_spiral(0,0,(X_MAX-1),(Y_MAX-1));
}

