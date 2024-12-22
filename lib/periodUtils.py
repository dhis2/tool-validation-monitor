import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Dhis2PeriodUtils:
    @staticmethod
    def previous_monthly_periods(period, number_of_periods):
        date = datetime.strptime(period, "%Y%m")
        previous_periods = [date - relativedelta(months=i) for i in range(1, number_of_periods + 1)]
        return {p.strftime("%Y%m") for p in previous_periods}

    @staticmethod
    def previous_weekly_periods(period, number_of_periods):
        year, week = int(period[:4]), int(period[5:])
        date = datetime.strptime(f'{year}-W{week}-1', "%Y-W%W-%w")
        previous_periods = [date - relativedelta(weeks=i) for i in range(1, number_of_periods + 1)]
        return {f"{p.isocalendar()[0]}W{p.isocalendar()[1]:02d}" for p in previous_periods}

    @staticmethod
    def previous_daily_periods(period, number_of_periods):
        date = datetime.strptime(period, "%Y%m%d")
        previous_periods = [date - relativedelta(days=i) for i in range(1, number_of_periods + 1)]
        return {p.strftime("%Y%m%d") for p in previous_periods}

    @staticmethod
    def previous_quarterly_periods(period, number_of_periods):
        year, quarter = int(period[:4]), int(period[5])
        date = datetime(year, (quarter - 1) * 3 + 1, 1)
        previous_periods = [date - relativedelta(months=i*3) for i in range(1, number_of_periods + 1)]
        return {f"{p.year}Q{((p.month - 1) // 3) + 1}" for p in previous_periods}

    @staticmethod
    def current_monthly_period(date=None):
        if date is None:
            date = datetime.now()
        else:
            date = datetime.strptime(date, "%Y-%m-%d")
        return date.strftime("%Y%m")

    @staticmethod
    def current_weekly_period(date=None):
        if date is None:
            date = datetime.now()
        else:
            date = datetime.strptime(date, "%Y-%m-%d")
        return date.strftime("%GW%V")

    @staticmethod
    def current_daily_period(date=None):
        if date is None:
            date = datetime.now()
        return date.strftime("%Y%m%d")

    @staticmethod
    def current_quarterly_period(date=None):
        if date is None:
            date = datetime.now()
        quarter = (date.month - 1) // 3 + 1
        return f"{date.year}Q{quarter}"


    def get_previous_periods(self, period, period_type, number_of_periods):
        if period_type == 'Monthly':
            return self.previous_monthly_periods(period, number_of_periods)
        elif period_type == 'Weekly':
            return self.previous_weekly_periods(period, number_of_periods)
        elif period_type == 'Daily':
            return self.previous_daily_periods(period, number_of_periods)
        elif period_type == 'Quarterly':
            return self.previous_quarterly_periods(period, number_of_periods)
        else:
            raise ValueError("Unsupported period type")