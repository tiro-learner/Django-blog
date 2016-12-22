import markdown


def markdownify(content):
    return markdown.markdown(content, ["codehilite"])


