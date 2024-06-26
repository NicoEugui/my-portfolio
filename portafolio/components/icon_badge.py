import reflex as rx

from portafolio.styles.styles import EmSize


def icon_badge(icon: str) -> rx.Component:
    return rx.badge(
        rx.icon(
            icon,
            size=32
        ),
        aspect_ratio="1",
        variant="soft",
        _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"}
    )
