def ft_euclid(a, b):
  if a % b == 0:
    return b
  r = a % b
  return ft_euclid(b, r)

print(ft_euclid(192, 162))
