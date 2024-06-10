def md_nre_single_sample (y, y_hat, n, p):
    result = (y**(1/n) - y_hat**(1/n))**p
    print(result)

md_nre_single_sample(100, 99.5, 2, 1)
md_nre_single_sample(20, 19.5, 2, 1)