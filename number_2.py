def get_cats_info(path):
    cats = list()
    try:
        with open(path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                cat_info = {"id": (data[0]), "name": data[1], "age": (data[2])}
                cats.append(cat_info)
    except FileNotFoundError:
        print("File not found")
        return None
    return cats
cats_info = get_cats_info("cats.txt")
print(cats_info)