import json

with open ("blog_posts.json") as data_file:
    data = json.load(data_file)

print(json.dumps(data, indent=4))
blog_1 = data[0]
print(blog_1["blog_id"])