#include <stdio.h>

int main()
{
#pragma omp parallel
  // omp stands for Open Multithreaded Programming
  // This should print "hello world" once for each logical core of the cpu
  printf ("hello world");
}
