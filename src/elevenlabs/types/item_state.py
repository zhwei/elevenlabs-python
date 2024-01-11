# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ItemState(str, enum.Enum):
    CREATED = "created"
    DELETED = "deleted"
    PROCESSING = "processing"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ItemState.CREATED:
            return created()
        if self is ItemState.DELETED:
            return deleted()
        if self is ItemState.PROCESSING:
            return processing()
