from bs4 import BeautifulSoup
# import lxml # can parse lxml into beautiful soup

print("\nOnline and Ready!\n")

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(f"\n---soup.title---\n{soup.title}\n")
# print(f"\n---soup.title.name---\n{soup.title.name}\n")
# print(f"\n---soup---\n{soup}\n")
# print(f"\n---soup.prettify()---\n{soup.prettify()}\n")

# # The two below only prints the first occurence of either of the tags
# print(soup.a)
# print(soup.li)

# What do we do when we want to find all the tags
all_anchor_tags = soup.findAll(name="a")  # Find all tages where the name is 'a'
# print(all_anchor_tags)

# all_paragraph_tags = soup.findAll(name="p")
# print(all_paragraph_tags)

# If we wanted all the text that can be found inside the anchor tags
for tag in all_anchor_tags:
    print(tag.get_text())


# What if we wanted all the href
for tag in all_anchor_tags:
    print(tag.get("href"))  # can parse in any of the attributes

# Find something by the id
# find will give only the first search query while findAll will return all of the search queries
heading = soup.find(name="h1", id="name")
print(heading)

# 'class' is a reserved keyword in python hence for bs4 we use 'class_'
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.get("class"))

# what if we want a specific a tag
company_url = soup.select_one(selector="p a")  # First macthing item
# "p a" is css selector, we are looking for an a tag that is sitting inside a p tag
print(company_url)

# can use css selector for class
name = soup.select_one(selector="#name")  # find where id=name
print(name)

# can use select to select all elements that match
headings = soup.select(".heading")
print(headings)

