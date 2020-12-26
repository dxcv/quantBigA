#  -*- coding: utf-8 -*-

from .daily_k_close_down_break_ma10 import DailyKCloseDownBreakMa10
from .daily_k_close_up_break_ma10 import DailyKCloseUpBreakMa10
from .daily_k_close_break_boll_down import DailyKCloseBreakBollDown
from .daily_k_close_break_boll_up import DailyKCloseBreakBollUp


class SignalFactory:
    @staticmethod
    def get_signal(name, account):
        if name == 'daily_k_close_up_break_ma10':
            return DailyKCloseUpBreakMa10(account)
        elif name == 'daily_k_close_down_break_ma10':
            return DailyKCloseDownBreakMa10(account)
        elif name == 'daily_k_close_break_boll_up':
            return DailyKCloseBreakBollUp(account)
        elif name == 'daily_k_close_break_boll_down':
            return DailyKCloseBreakBollDown(account)

