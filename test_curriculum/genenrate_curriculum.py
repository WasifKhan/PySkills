import os
import re

from matplotlib import pyplot as plt


def has_slides(section):
    # checks if section has a section/docs/slides folder
    slides = os.path.join(section, "docs", "slides")
    return os.path.exists(slides) and os.path.isdir(slides)


def get_sections(folder="."):
    # if folder is already a section, then just return that
    if has_slides(folder):
        return [folder]
    # else it's something like "." and get all sections
    return [s for s in os.listdir(folder) if has_slides(s)]


def is_md(fname):
    # check if a file ends in .md and not overview
    if re.match(".*\.md$", fname) and not re.match("overview.md", fname, re.I):
        return True  # re.match returns a match object, hence return True
    return False


def get_subsections(section):
    # return all the .md files in /docs/slides
    path = os.path.join(section, "docs", "slides")
    files = os.listdir(path)
    return [md for md in files if is_md(md)]


def get_ex_subs(section):
    path = os.path.join(section, "exercises")
    files = [os.path.join(section, "exercises", f) for f in os.listdir(path)]
    return [d for d in files if os.path.isdir(d)]


def count_slides(fname):
    with open(fname, "r") as f:
        data = f.read()  # .decode("utf-8")
    # split on either --- or ===
    slides = re.split("\r?\n\-\-\-\r?\n|\r?\n===\r?\n", data)
    return len(slides)


def count_exercises(folder):
    files = [os.path.join(folder, f) for f in os.listdir(folder)]
    exs = [d for d in files if os.path.isdir(d)]
    return len(exs)


def is_camel(s):
    # return if likely camelCase
    return s.lower() != s


def pretty_name(s):
    if is_md(s):
        # chop off the .md
        s = s[:-3]
    if os.path.isdir(s):
        # chop off the leading folder info
        s = os.path.split(s)[-1]
    # split on - or _ capitalize and join with spaces
    return " ".join(
        [w.capitalize() if not is_camel(w) else w for w in re.split("\-|_", s)]
    )


def count_section(section):
    # return a dictionary with the counts for each subsection
    # also return the total
    subs = get_subsections(section)
    res = {}
    total = 0
    for sub in subs:
        fname = os.path.join(section, "docs", "slides", sub)
        count = count_slides(fname)
        res[pretty_name(sub)] = count
        total += count
    return total, res


def count_section_ex(section):
    subs = get_ex_subs(section)
    res = {}
    total = 0
    for sub in subs:
        count = count_exercises(sub)
        res[pretty_name(sub)] = count
        total += count
    return total, res


def count_all(folder="."):
    sections = get_sections(folder)
    res = {}
    total = 0
    for section in sections:
        count, _ = count_section(section)
        res[pretty_name(section)] = count
        total += count
    return total, res


def count_all_ex(folder="."):
    sections = get_sections(folder)
    res = {}
    total = 0
    for section in sections:
        count, _ = count_section_ex(section)
        res[pretty_name(section)] = count
        total += count
    return total, res


def lineify(s):
    "Replace ' ' with '\n' so graph text isn't so clumped"
    return "\n".join(s.split())


def make_graph(title, slides):
    plt.rc("xtick", labelsize=8)
    plt.subplots(
        figsize=(10, 5)
    )  # need to make it big enough so text doesn't overlap...
    rects = plt.bar(list(map(lineify, slides.keys())), slides.values())
    plt.ylabel("Number of Slides")
    plt.title(title)
    # add numbers to the bars
    for r in rects:
        h = r.get_height()
        plt.text(r.get_x() + r.get_width() / 2, h + 0.25, str(h), ha="center")
    plt.savefig(title + "-slides.png")
    plt.clf()


def make_graph_ex(title, exercises):
    plt.rc("xtick", labelsize=8)
    plt.subplots(
        figsize=(10, 5)
    )  # need to make it big enough so text doesn't overlap...
    rects = plt.bar(
        list(map(lineify, exercises.keys())), exercises.values(), color="tab:orange"
    )
    plt.ylabel("Number of Exercises")
    plt.title(title)
    # add numbers to the bars
    for r in rects:
        h = r.get_height()
        plt.text(r.get_x() + r.get_width() / 2, h + 0.25, str(h), ha="center")
    plt.savefig(title + "-exercises.png")
    plt.clf()


# make_graph("Phase 1", count_all()[1])
# make_graph("Software-Theory", count_section("Software-Theory")[1])


def summary(folder=".", name="Phase-1"):
    "Make the slide and exercise graphs for the phase or section"
    # check if used on a single section
    if len(get_sections(folder)) == 1:
        # if folder is not '.' then use it for the name
        if folder != ".":
            name = folder
        # then just make the graphs for this section using the section as name
        print(f"Making slide graph for {name}")
        make_graph(name, count_section(folder)[1])
        print(f"Making exercise graph for {name}")
        make_graph_ex(name, count_section_ex(folder)[1])
        # done
        return
    # else it's for the whole phase
    print(f"Making the slide graph for {name}")
    make_graph(name, count_all(folder)[1])
    print(f"Making the exercise graph for {name}")
    make_graph_ex(name, count_all_ex(folder)[1])
    for section in get_sections(folder):
        print(f"Making slide graph for {section}")
        make_graph(section, count_section(section)[1])
        print(f"Making exercise graph for {section}")
        make_graph_ex(section, count_section_ex(section)[1])
    print("Finished making graphs")


if __name__ == "__main__":
    import sys

    # default args
    folder = "."
    name = "Phase-1"
    try:
        folder = sys.argv[1]
        name = sys.argv[2]
    except:
        pass

    summary(folder, name)
