#include <bits/stdc++.h>

std::vector<std::string>	split(std::string str, std::string delemiter)
{
	std::vector<std::string>	ret;
	long long	pos = 0;
	std::string token = "";

	while ((pos = str.find(delemiter)) != std::string::npos)
	{
		token = str.substr(0, pos);
		ret.push_back(token);
		str.erase(0, pos + delemiter.length());
	}
	ret.push_back(str);
	return (ret);
}

int	main()
{	
	std::string str = "hello world seonggoc hihihi";
	std::vector<std::string> ret = split(str, " ");

	for (auto i : ret)
	{
		std::cout << i << std::endl;
	}
}