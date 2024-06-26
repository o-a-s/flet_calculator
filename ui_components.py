from flet import (
    Text,
    ElevatedButton,
    ButtonStyle,
    RoundedRectangleBorder,
    transform,
    padding,
    Row,
    MainAxisAlignment,
)
from constants import (
    COLORS,
    BUTTON_LAYOUT,
)
# ------------------------------------------------------------------------------


def create_button(text, data, on_click):
    """
    Creates a button with specified properties
    """
    bgcolor = (
        COLORS["operator_bg"]
        if text in ["÷", "x", "-", "+"]
        else COLORS["border"]
        if text in ["="]
        else COLORS["button_bg"]
    )

    return ElevatedButton(
        text=text,
        color=COLORS["text"],
        bgcolor=bgcolor,
        data=data,
        width=65,
        height=50,
        scale=transform.Scale(scale=1.1),
        on_click=on_click,
        style=ButtonStyle(
            padding=padding.all(10),
            shape=RoundedRectangleBorder(radius=10),
        ),
    )


def create_text():
    """
    Creates a text object with predefined styles
    """
    return Text(
        value="",
        size=20,
        text_align="right",
        color=COLORS["text"],
        selectable=True,
        no_wrap=False,
    )


def create_button_rows(handle_keyboard_input):
    """
    Creates rows of buttons using the create_button function
    """
    rows = [
        Row(
            controls=[
                create_button(text, data, on_click=handle_keyboard_input)
                for text, data in row_buttons
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
        )
        for row_buttons in BUTTON_LAYOUT
    ]

    return rows
