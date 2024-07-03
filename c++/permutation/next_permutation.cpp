#include <bits/stdc++.h>

int	main()
{
	std::vector<int> a = {2, 1, 3};

	sort(a.begin(), a.end());
	do
	{
		for (auto i : a)
		{
			std::cout << i << " ";
		}
		std::cout << std::endl;
	} while (next_permutation(a.begin(), a.end()));
}