
class CategoryTag:
    _all_tags = []
    def __init__(self, name):
        self.name = name
        CategoryTag._all_tags.append(self)
    
    def __str__(self):
        return f"This is tag {self.name}"

    @classmethod
    def all_category_tags(self):
        temp =  ""
        for val, tag in enumerate(CategoryTag._all_tags):
            temp += f"{val+1}. {tag.name}\n"
        return f"These are all the tags that have been created: \n{temp}"
    


j = CategoryTag("Action")
i = CategoryTag("Thriller")

print(i)
print(j)
print(CategoryTag.all_category_tags())