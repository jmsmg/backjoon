#include <iostream>
#include <vector>

std::vector<int> v;

void	printV(std::vector<int> &v)
{
	for (unsigned int i = 0; i < v.size(); i++)
	{
		std::cout << v[i] << " ";
	}
	std::cout << std::endl;
}

void	makePermutation(int n, int r, int depth)
{
	if (r == depth)
	{
		printV(v);
		return ;
	}
	for (int i = depth; i < n; i++)
	{
		std::swap(v[i], v[depth]);
		makePermutation(n, r, depth + 1);
		std::swap(v[i], v[depth]);
	}
}
int	main()
{
	for (int i = 1; i < 4; i++)
		v.push_back(i);
	makePermutation(3, 3, 0);
}
