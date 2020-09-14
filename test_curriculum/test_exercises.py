def test_exercises():
    import os

    os.chdir("exercises")
    # Go through main README in module and extract all sections
    for directory in os.listdir():
        if directory == "README.md":
            readme = open("README.md")
            lines = readme.readlines()
            sections = []
            is_section = False
            for line in lines:
                if is_section:
                    sections.append(line[2:-1].lower().replace(" ", "_"))
                if line == "## Exercise Sections\n":
                    is_section = True
            readme.close()

    # Go through each section and extract all the exercises
    for section in sections:
        os.chdir(section)
        # Go through each exercise and run tests against model solution
        for directory in os.listdir():
            readme = open("README.md")
            lines = readme.readlines()
            exercises = []
            is_exercises = -1
            for line in lines:
                if is_exercises == 1:
                    exercises.append(
                        line[line.find("[") + 1 : line.find("]")]
                        .replace(" ", "_")
                        .lower()
                    )
                    y = 10
                elif is_exercises == 0:
                    if line[0:3] == "|:-":
                        is_exercises += 1
                    else:
                        raise FileNotFoundError(
                            f"Incorrect format for README in {section} section"
                        )
                else:
                    if line == "| Exercise ID | Exercise |\n":
                        is_exercises += 1

            if is_exercises != 1:
                raise FileNotFoundError(
                    f"Incorrect format for README in {section} section"
                )
            readme.close()

        for exercise in exercises:
            os.chdir(f"{exercise}/solution")
            import subprocess

            failure = subprocess.call("pytest test_solution.py", shell=True)
            if failure:
                raise AssertionError(
                    f"Model solution for {exercise} in {section} section failed tests"
                )
            os.chdir("../..")
        os.chdir("..")
    os.chdir("..")
