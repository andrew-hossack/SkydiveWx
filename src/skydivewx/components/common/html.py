from dash import html


def mobileDiv(**args) -> html.Div:
    try:
        className = args.pop("className")
    except KeyError:
        className = ""
    return html.Div(className=className + " mobile ", **args)


def webDiv(**args) -> html.Div:
    try:
        className = args.pop("className")
    except KeyError:
        className = ""
    return html.Div(className=className + " web ", **args)
