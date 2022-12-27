from .set_laptops import get_laptops


def filter_laptops(prop: str) -> list:
    laptops = get_laptops()
    out_list = sorted(laptops, key=lambda x: (x[prop], x['product_name']))
    return out_list
