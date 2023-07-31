#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
  * infinite_while - infinite while loop
  * Return: 0
  */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
  * main - creates 5 zombie processes
  * Return: 0 (success) or failure
  */

int main(void)
{
	pid_t proc_zombie;
	int z;

	for (z = 1; z <= 5; z++)
	{
		proc_zombie = fork();
		if (!proc_zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", proc_zombie);
	}
	infinite_while();

	return (0);
}
