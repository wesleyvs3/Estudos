#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX 11
#define MAX_ENTRADAS 100

char entradas[MAX_ENTRADAS][MAX];
char entrada[MAX];
char resultado[MAX];
bool usado[MAX];
int len;

void quicksortString(char arr[], int low, int high) {
    if (low < high) {
        char pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                char tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
        char tmp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = tmp;

        int pi = i + 1;
        quicksortString(arr, low, pi - 1);
        quicksortString(arr, pi + 1, high);
    }
}

void permutar(int nivel) {
    if (nivel == len) {
        resultado[nivel] = '\0';
        printf("%s\n", resultado);
        return;
    }
    for (int i = 0; i < len; i++) {
        if (usado[i]) continue;
        if (i > 0 && entrada[i] == entrada[i - 1] && !usado[i - 1]) continue;
        usado[i] = true;
        resultado[nivel] = entrada[i];
        permutar(nivel + 1);
        usado[i] = false;
    }
}

int main() {
    int n;
    scanf("%d", &n);
    getchar();

    for (int i = 0; i < n; i++) {
        fgets(entrada, MAX, stdin);
        entrada[strcspn(entrada, "\n")] = '\0';

        len = strlen(entrada);
        quicksortString(entrada, 0, len - 1);

        memset(usado, 0, sizeof(usado));
        permutar(0);
        printf("\n");
    }

    return 0;
}