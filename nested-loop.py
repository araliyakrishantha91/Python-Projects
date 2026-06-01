# for i in range(1,13):
#     for j in range(1,13):
#         print("{0} * {1} = {2}".format(i,j,j*i))
#     print("-" * 15)
#--------------------------------------------------------------------------------------
# shopping_list = ["milk" , "oats", "eggs", "rice", "juice", "banana"]

# for item in shopping_list:
#     # if item != "rice":
#     #     print("Buy " + item)
#     if item == "rice":
#         continue
#     print("Buy " + item)
#----------------------------------------------------------------------------------------
# shopping_list = ["milk" , "oats", "eggs", "rice", "juice", "banana"]
#
# search_for = "ricce"
# found_at = None
# # here (len(shopping_list)) = 6
# for index in range(len(shopping_list)):
#     print("testing {}".format(index))
#     if shopping_list[index] == search_for:
#         found_at = index
#         break
# if found_at is not None:
#     print("{} found at {}".format(search_for, found_at))
# else:
#     print("{} wasn't found".format(search_for))
#-------------------------------------------------------------------------------
shopping_list = ["milk" , "oats", "eggs", "rice", "juice", "banana"]
search_for = "rice"
found_at = None
if search_for in shopping_list:
    found_at = shopping_list.index(search_for)

if found_at is not None:
    print("{} found at {}".format(search_for, found_at))
else:
    print("{} wasn't found".format(search_for))
