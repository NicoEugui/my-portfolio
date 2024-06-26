import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Technology
from portafolio.styles.styles import EmSize, Size


def tech_stack(technologies: list[Technology]) -> rx.Component:
    return rx.vstack(
        heading("Technologies"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name=technology.icon,
                        font_size="24px"
                    ),
                    rx.text(technology.name),
                    size="2",
                    _hover={"transform": "scale(1.1)", "transition": "transform 0.2s"}
                )
                for technology in technologies
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value,
    )
