#include <stdio.h>
#include <stdlib.h>

int append_text_to_file(const char *filename, const char *text) {
  FILE *fp = fopen(filename, "a");
  if (fp == NULL) {
    perror("Nu am putut deschide fisierul");
    return -1;
  }
  fprintf(fp, "%s\n", text);
  fclose(fp);
  return 0;
}

int main(int argc, char *argv[]) {
  if (argc != 3) {
    fprintf(stderr, "Fol: %s gray_list.txt text_de_adaugat\n", argv[0]);
    return EXIT_FAILURE;
  }

  const char *file_path = argv[1];
  const char *line = argv[2];

  int status = append_text_to_file(file_path, line);
  if (status != 0) {
    return EXIT_FAILURE;
  }

  return EXIT_SUCCESS;
}
