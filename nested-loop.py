# for i in range(1,13):
#     for j in range(1,13):
#         print("{0} * {1} = {2}".format(i,j,j*i))
#     print("-" * 15)

shopping_list = ["milk" , "oats", "rice", "juice", "banana"]

for item in shopping_list:
    # if item != "rice":
    #     print("Buy " + item)
    if item == "rice":
        continue
    print("Buy " + item)
