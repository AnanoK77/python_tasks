# დავალება 1
# user1_info = []
# user2_info = []
# user3_info = []
# consumer_info = []
#
#
# def input_user_info(user_list):
#     name = input("Enter your name: ")
#     surname = input("Enter your surname: ")
#     age = input("Enter your age: ")
#     user_list.extend([name, surname, age])
#
#
# input_user_info(user1_info)
# input_user_info(user2_info)
# input_user_info(user3_info)
#
#
# consumer_info.append(user1_info)
# consumer_info.append(user2_info)
# consumer_info.append(user3_info)
#
#
# user_index = int(input("Enter user index (1, 2, or 3): ")) - 1
#

# selected_user = consumer_info[user_index]
# print("Name:", selected_user[0])
# print("Lastname:", selected_user[1])
# # print("Age:", selected_user[2])
#
# # დავალება 2.
#
# actor_info = {
#     "Angelina": {
#         "last_name": "Jolie",
#         "age": 46,
#         "movies": ["Mr. & Mrs. Smith", "Maleficent", "Girl, Interrupted"]
#     }
# }
#
#
# def search_actor(actor_name):
#     for first_name, info in actor_info.items():
#         if first_name.lower() == actor_name.lower() or info["last_name"].lower() == actor_name.lower():
#             print(f"Name: {first_name} {info['last_name']}")
#             print(f"Age: {info['age']}")
#             print("Movies:")
#             for movie in info["movies"]:
#                 print(f"- {movie}")
#             return
#     print("Actor not found.")
#
#
# while True:
#     actor_name = input("Enter the first or last name of the actor (or 'quit' to exit): ")
#     if actor_name.lower() == "quit":
#         break
#     search_actor(actor_name)

# #დავალება 3
# def unique_list(input_list):
#     unique_elements = list(set(input_list))
#     return unique_elements
#
# # Example usage:
# original_list = [10, 21, 21, 33, 13, 10, 5]
# unique_result = unique_list(original_list)
# print("Original List:", original_list)
# print("Unique List:", unique_result)

#დავალება4

# #     combined_set = set1.union(set2)
# #     result_tuple = tuple(combined_set)
# #     return result_tuple
# #

# # set1 = {7, 8, 9}
# # set2 = {9, 10, 11}
# # result = set_to_tuple(set1, set2)
# # print("Combined Tuple:", result)

# #დავალება 5
# def is_dict_empty(input_dict):
#     if not input_dict:
#         return True
#     else:
#         return False
#
# empty_dict = {}
# non_empty_dict = {'key': 'value'}
#
# print("Is empty_dict empty?", is_dict_empty(empty_dict))
# print("Is non_empty_dict empty?", is_dict_empty(non_empty_dict))

# #დავალება 6
# def count_characters(string):
#     char_count = {}
#     for char in string:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     return char_count
#
#
# input_string = 'w3schools'
# result = count_characters(input_string)
# print(result)


