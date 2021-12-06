#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 256

int main() {
  int horizontal_position = 0;
  int depth = 0;

  char buffer[MAX_LEN];
  while (fgets(buffer, MAX_LEN, stdin)) {
    // remove trailing newline
    buffer[strcspn(buffer, "\n")] = 0;

    // split line into intruction and value
    char *instruction = strtok(buffer, " ");
    int value = atoi(strtok(NULL, " "));

    // each instruction's first character is unique
    switch (instruction[0]) {
    case 'f': // forward
      horizontal_position += value;
      break;
    case 'b': // backward
      horizontal_position -= value;
      break;
    case 'u': // up
      depth -= value;
      break;
    case 'd': // down
      depth += value;
      break;
    }
  }

  int result = horizontal_position * depth;
  printf("%d\n", result);
}