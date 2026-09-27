from datetime import datetime

from rich.console import Console, JustifyMethod, OverflowMethod
from rich.style import StyleType


class NewConsole(Console):
    def print(
        self,
        *messages: object,
        sep: str = " ",
        end: str = "\n",
        style: StyleType | None = None,
        justify: JustifyMethod | None = None,
        overflow: OverflowMethod | None = None,
        no_wrap: bool | None = None,
        emoji: bool | None = None,
        markup: bool | None = None,
        highlight: bool | None = None,
        width: int | None = None,
        height: int | None = None,
        crop: bool = True,
        soft_wrap: bool | None = None,
        new_line_start: bool = False,
    ) -> None:
        """터미널일 때는 기본 출력"""
        """비터미널일 때는 타임스탬프를 접두사로 붙여 출력합니다."""
        if not self.is_terminal and messages:
            first, *rest = messages
            messages = (f"[{datetime.now():%y-%m-%d|%H:%M:%S}] {first}", *rest)

        super().print(
            *messages,
            sep=sep,
            end=end,
            style=style,
            justify=justify,
            overflow=overflow,
            no_wrap=no_wrap,
            emoji=emoji,
            markup=markup,
            highlight=highlight,
            width=width,
            height=height,
            crop=crop,
            soft_wrap=soft_wrap,
            new_line_start=new_line_start,
        )


console = NewConsole()
