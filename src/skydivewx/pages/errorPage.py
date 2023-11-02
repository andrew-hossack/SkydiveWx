import os
import traceback
from dash import html
import dash_mantine_components as dmc
import smtplib, ssl


def send_error_email(errorMsg: str):
    context = ssl.create_default_context()
    emailUsername = os.environ.get("EMAIL_SENDER_USERNAME")
    emailPassword = os.environ.get("EMAIL_SENDER_PASSWORD")
    receiverEmail = "errors@skydivewx.com"
    if (not emailUsername) or (not emailPassword):
        raise Exception(
            "No email or email password or receiver email given! Not sending error email."
        )
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        print(f"Sending error message from {emailUsername}...")
        server.login(emailUsername, emailPassword)
        message = f"Subject: SkydiveWx Error Notification\n\n{errorMsg}"
        server.sendmail(emailUsername, receiverEmail, message)
        print("Error email sent!")


def render() -> html.Div:
    error = traceback.format_exc()
    emailError = None
    errorModalChildren = []
    try:
        send_error_email(error)
    except Exception as e:
        emailError = str(e)
    if emailError:
        # Error report email failure
        error += f" During handling of the above error, an error occured while sending the error email: {emailError}"
        errorModalChildren = [
            html.A("Sorry! If you are seeing this, an error occurred. Please notify "),
            html.A(
                "admin@skydivewx.com",
                href=f"mailto:admin@skydivewx.com?subject=SkydiveWx - Application Error Report&subject={error}",
                target="_blank",
            ),
            html.A(" to resolve the issue."),
            html.Br(),
            html.Br(),
            html.P(f"Error Information:"),
            html.P(error, style={"font-size": "10px"}),
        ]
    else:
        # Error report email success
        errorModalChildren = [
            html.A(
                "Sorry! If you are seeing this, an error occurred. Our team has been notified and will be addressing it soon."
            ),
        ]

    return html.Div(
        id="error-page-container",
        children=[
            dmc.Modal(
                title="Application Error",
                id="modal-simple",
                opened=True,
                centered=True,
                closeOnClickOutside=False,
                closeOnEscape=False,
                withCloseButton=False,
                zIndex=10000,
                children=errorModalChildren,
            ),
        ],
        style={
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
            "flex-direction": "column",
            "marginTop": "0",
            "backgroundColor": "transparent",
            "marginBottom": "20px",
            "padding": "2rem 1rem",
        },
    )
