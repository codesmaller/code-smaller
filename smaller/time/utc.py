from datetime import datetime, timedelta, timezone

from smaller.default import DEFAULT


class Time:

    # Default value for `naive` parameter in methods
    naive: bool = False

    @classmethod
    def now(cls, *, naive: bool = DEFAULT) -> datetime:
        """
        Get current UTC datetime.
        
        Set `naive` to True to get naive datetime without timezone info.
        """

        time_now = datetime.now(timezone.utc)

        if naive is DEFAULT:
            naive = cls.naive

        if naive:
            time_now = time_now.replace(tzinfo=None)

        return time_now

    @classmethod
    def past(
        cls,
        *,
        seconds: int = 0,
        minutes: int = 0,
        hours: int = 0,
        weeks: int = 0,
        days: int = 0,
        microseconds: int = 0,
        milliseconds: int = 0,
        naive: bool = DEFAULT,
    ) -> datetime:
        """
        Get current UTC datetime minus x seconds, minutes etc.
        
        Set `naive` to True to get naive datetime without timezone info.
        """

        interval = timedelta(
            seconds=seconds,
            minutes=minutes,
            hours=hours,
            weeks=weeks,
            days=days,
            microseconds=microseconds,
            milliseconds=milliseconds,
        )

        return cls.now(naive=naive) - interval

    @classmethod
    def future(
        cls,
        *,
        seconds: int = 0,
        minutes: int = 0,
        hours: int = 0,
        weeks: int = 0,
        days: int = 0,
        microseconds: int = 0,
        milliseconds: int = 0,
        naive: bool = DEFAULT,
    ) -> datetime:
        """
        Get current UTC datetime plus x seconds, minutes etc.
        
        Set `naive` to True to get naive datetime without timezone info.
        """

        interval = timedelta(
            seconds=seconds,
            minutes=minutes,
            hours=hours,
            weeks=weeks,
            days=days,
            microseconds=microseconds,
            milliseconds=milliseconds,
        )

        return cls.now(naive=naive) + interval
