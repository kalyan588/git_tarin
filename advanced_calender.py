import calendar
import datetime
import sys

class CalendarApp:
    def __init__(self):
        self.current_date = datetime.datetime.now()
        self.selected_date = self.current_date

    def display_calendar(self):
        print(f"\n{self.selected_date.strftime('%B %Y')}")
        print("Su Mo Tu We Th Fr Sa")

        month_calendar = calendar.monthcalendar(self.selected_date.year, self.selected_date.month)

        for week in month_calendar:
            for day in week:
                if day == 0:
                    print("   ", end="")
                else:
                    day_str = f"{day:2d}"
                    if day == self.current_date.day and week.index(day) == 0:
                        day_str = f"\033[1;37;44m{day_str}\033[0m"  # Highlight current day
                    elif day == self.current_date.day:
                        day_str = f"\033[1;37;42m{day_str}\033[0m"  # Highlight today's date
                    print(day_str, end=" ")
            print()

    def compute_relative_month(self, offset):
        self.selected_date = self.selected_date.replace(day=1) + datetime.timedelta(days=32)
        self.selected_date = self.selected_date.replace(day=1) + datetime.timedelta(days=offset)

    def run(self):
        if len(sys.argv) == 2 and sys.argv[1] == "-help":
            print("Help: This application should be run with the following command line parameters:")
            print("A positive integer, a negative integer, or zero.")
            print("The positive integer cannot be more than 12 or less than -12.")
            print("Example: python custom_calendar_app.py +5")
            print("Example: python custom_calendar_app.py -2")
            print("Example: python custom_calendar_app.py 0")
            print("Example: python custom_calendar_app.py -help (for help)")
            print("\nStudent Credentials:")
            print("Your Name")
            print("Your Student ID")
            return

        if len(sys.argv) == 1:
            # Run without command line parameters
            self.display_calendar()
        elif len(sys.argv) == 2 and sys.argv[1].isdigit() and -12 <= int(sys.argv[1]) <= 12:
            # Run with a valid command line parameter
            offset = int(sys.argv[1])
            self.compute_relative_month(offset)
            self.display_calendar()
        else:
            print("Invalid command line parameters. Use -help for assistance.")

if __name__ == "__main__":
    app = CalendarApp()
    app.run()
