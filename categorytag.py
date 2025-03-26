class CategoryTag:
    """
    A class to create and manage category tags.
    Tracks all created tags and provides methods to interact with them.
    """
    _all_tags = []
    
    def __init__(self, name):
        """
        Create a new category tag.
        Args:
        name (str): The name of the tag
        """
        self.name = name
        CategoryTag._all_tags.append(self)
    
    def __str__(self):
        """
        Provide a string representation of the tag.
        Returns:
        str: A description of the tag
        """
        return f"This is tag {self.name}"
    
    @classmethod
    def all_category_tags(self):
        """
        List all created category tags.
        Returns:
        str: A formatted string of all tag names
        """
        temp = ""
        for val, tag in enumerate(CategoryTag._all_tags):
            temp += f"{val+1}. {tag.name}\n"
        return f"These are all the tags that have been created: \n{temp}"
    


# j = CategoryTag("Action")
# i = CategoryTag("Thriller")

# print(i)
# print(j)
# print(CategoryTag.all_category_tags())
