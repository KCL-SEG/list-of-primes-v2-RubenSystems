

#define true 1
#define false 0

char is_prime(unsigned int number) {
	if (number == 1) {
		return false;
	}

	unsigned long i = 2; 
	while (i * i <= number) {
		if (number % i == 0) {
			return false;
		}
		i++;
	}
	return true;
}