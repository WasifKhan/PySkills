# from create_main_dict  import create_main
# from create_slides_dict import create_slides
from os import chdir
import regex as re
from collections import OrderedDict


def create_main():
    readme = open("README.md", "r").readlines()
    contents = "".join(readme)
    main_readme_dict = OrderedDict()
    level1 = None
    curr_level2 = None
    page = re.split(r"\n", contents)
    for line in page:
        start = line[:3]
        if start == "## ":
            level1 = line[3:].strip()
            main_readme_dict[level1] = OrderedDict()
        elif start == "###":
            curr_level2 = line[3:].strip()
            main_readme_dict[level1][curr_level2] = []
        elif line[:1] == "*":
            main_readme_dict[level1][curr_level2].append(line[2:].strip())
    return main_readme_dict


# print(create_main())


def create_slides(filename):
    chdir("docs/slides")
    readme = open(filename, "r").readlines()
    contents = "".join(readme)
    module_dict = OrderedDict()
    page = re.split(r"\n", contents)
    section = None
    topic = None
    sub_topic = None
    slide_num = 1
    code_block_open = False
    for line in page:
        line = line.split()
        if line and line == ["---"]:
            slide_num += 1
            if code_block_open is True:
                err_msg = f"ERROR: Section: {section}, Topic: {topic}, Subtopic: {sub_topic}\nThere is an open code block in slide {slide_num}"
                raise AssertionError(err_msg)
        elif line == ["```"]:  # some are ```Python - check recursive function
            if code_block_open is False:
                code_block_open = True
            else:
                code_block_open = False
        elif line and line[0] == "#" and section == None:
            level1 = " ".join(line[1:])
            section = level1
            module_dict[section] = OrderedDict()
        elif line and line[0] == "##":
            if line[1].title() == "Topics":  ###
                topic = "Topics"  ###
            else:
                # print(line)
                # topic = None
                idx = 0
                dash_idx_1 = None
                dash_idx_2 = None
                for item in line:
                    if item == "-" and dash_idx_1 is None:
                        dash_idx_1 = idx
                    elif item == "-" and dash_idx_1:
                        if dash_idx_2 is None:
                            dash_idx_2 = idx
                    idx += 1
                if line and dash_idx_1 is None:
                    topic = " ".join(line[1 : idx + 1])
                    sub_topic = None
                elif dash_idx_1:
                    if dash_idx_2 is None:
                        sub_topic = " ".join(line[dash_idx_1 + 1 :])
                    else:
                        sub_topic = " ".join(line[dash_idx_1 + 1 : dash_idx_2])
                if topic not in module_dict[section]:
                    err_msg = (
                        f"ERROR: Section: {section} has not matching topics: {topic}"
                    )
                    raise AssertionError(err_msg)
                elif sub_topic and sub_topic not in module_dict[section][topic]:
                    err_msg = f"ERROR: Section: {section}, topic: {topic} has not matching subtopics: {sub_topic}"
                    raise AssertionError(err_msg)
        elif line and (line[0] == "-" or line[0] == "*"):
            if topic == "Topics":
                module_dict[section][" ".join(line[1:])] = OrderedDict()
            elif topic in module_dict[section] and sub_topic is None:
                module_dict[section][topic][" ".join(line[1:])] = []
            elif (
                sub_topic
                and topic in module_dict[section]
                and sub_topic in module_dict[section][topic]
            ):
                module_dict[section][topic][sub_topic].append(" ".join(line[1:]))
    return module_dict


# print(create_slides())


def test_slides():
    main = create_main()
    filenames = [i.lower().replace(" ", "_") + ".md" for i in main.keys()]
    for i in range(len(filenames)):
        slides = create_slides(filenames[i])
        section_name_main = list(main.keys())[i]
        section_name_slides = list(slides.keys())[0]
        if section_name_main != section_name_slides:
            err_msg = f"Section Mismatch: README: {section_name_main} differs from section title: {section_name_slides}"
            raise AssertionError(err_msg)
        topics_list_main = main[section_name_main].keys()
        topics_list_slides = slides[section_name_slides].keys()
        if topics_list_main != topics_list_slides:
            err_msg = f"Topics mismatch in section: '{section_name_main}'\nREADME {topics_list_main} differs from topic overview {topics_list_slides}"
            raise AssertionError(err_msg)
        for key in topics_list_main:
            # if key not in topics_list_slides:
            #     return f"Topic Error: {key} is in the main readme but not in the slides"
            slides_list = list(slides[section_name_main][key].keys())
            main_readme_list = main[section_name_main][key]
            slds = "".join(slides_list)
            mn = "".join(main_readme_list)
            if slds != mn:
                err_msg = f"Subtopic mismatch in section: '{section_name_main}', topic: '{key}'\nREADME {main_readme_list} differs from slide titles {slides_list}"
                raise AssertionError(err_msg)
        chdir("../..")
    return True


# print(test_slides())
