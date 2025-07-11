import copy
from enum import Enum


class SkillLevel(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class Hobby:
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = skill_level

    def __repr__(self):
        return f"Hobby(name={self.name!r}, skill_level={self.skill_level!r})"


class Person:
    def __init__(self, name, hobbies, main_hobby=None):
        self.name = name
        self.hobbies = hobbies
        self.main_hobby = main_hobby

    def __repr__(self):
        return (
            f"Person(name={self.name!r}," +
            f"hobbies={self.hobbies!r}, main_hobby={self.main_hobby!r})"
        )


# Create an instance
original = Person(
    "Alice",
    ["reading", "cycling"],
    main_hobby=Hobby("swimming", SkillLevel.INTERMEDIATE),
)

# Make a deepcopy
cloned = copy.deepcopy(original)

# Modify the clone
cloned.name = "Bob"
cloned.hobbies.append("painting")
cloned.main_hobby.skill_level = SkillLevel.ADVANCED

print("Original:", original)
print("Cloned:  ", cloned)
