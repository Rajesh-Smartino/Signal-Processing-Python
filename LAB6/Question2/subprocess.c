#include <string.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
	if (argc != 2) {
		printf("Usage: Programname string\n");
		return(-1);
	}
	printf("%s %d\n", argv[1], strlen(argv[1]));
	return(0);
}
