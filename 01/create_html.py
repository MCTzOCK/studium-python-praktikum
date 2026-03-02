import html


def createHtmlElement(type, classname=None, id=None, style=None, content=None, text=None):

    if content is None and text is None:
        raise ValueError("Either content or text must be specified.")

    _cn = classname if classname else ""
    _id = id if id else ""
    _style = style if style else ""

    shouldEscape = True if text is not None else False
    _c = content if content else text

    if shouldEscape:
        _c = html.escape(_c)

    attr = f'{" class=\"" + _cn + "\"" if _cn else ""}{" id=\"" + _id + "\"" if _id else ""}{" style=\"" + _style + "\"" if _style else ""}'

    return f'<{type}{attr}>{_c}</{type}>'


if __name__ == "__main__":
    span = createHtmlElement("span", text="Werbung <:)")
    div = createHtmlElement("div", classname="ad", id="teaser", style="width: 100%;", content=span)
    print(div)