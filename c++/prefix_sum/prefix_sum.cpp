#include <bits/stdc++.h>

using namespace std;

int arr[100004] = {0};
int psum[100004] = {0};
int	main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int	N;
	int	M;

	int	a;
	int	b;

	cin >> N;
	cin >> M;

	for (int i = 1; i < N; i++)
	{
		cin >> arr[i];
		psum[i] = psum[i - 1] + arr[i];
	}

	for (int i = 0; i < M; i++)
	{
		cin >> a;
		cin >> b;

		cout << psum[b] - psum[a - 1] << "\n";
	}
}
