from datetime import datetime
import math
from constants import FeeStructure

class Fee:
    @staticmethod
    def get_total_fee(start_time, end_time) -> float:
        no_of_hours = Fee._calc_number_of_hours(start_time, end_time)
        total_fee = FeeStructure.FIRST_HOUR.value
        if no_of_hours > 1: total_fee += FeeStructure.SECOND_AND_THIRD_HOUR.value
        if no_of_hours > 2: total_fee += FeeStructure.SECOND_AND_THIRD_HOUR.value
        if no_of_hours > 3:
            total_fee += (no_of_hours - 3) * FeeStructure.FOURTH_HOUR_ONWARDS.value
        return total_fee

    @staticmethod
    def _calc_number_of_hours(start_time: datetime, end_time: datetime) -> int:
        delta = end_time-start_time
        no_of_hours = math.ceil((delta.days * 24) + (delta.seconds / 3600))
        return no_of_hours
