k = input("Item: ").strip().lower()

li = { 
    "apple": 130,
    "avocado": 50,
    "sweet cherries": 100,
    "banana": 110,
    "grapes": 90
}

if(k in li):
    print("Calories:", li[k])
