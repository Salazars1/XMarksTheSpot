from django import forms

class ReservationForm(forms.Form):
    day = forms.CharField(label='Day', max_length=9)
    timeInt = forms.IntegerField(label='Time', max_value=12)
    timeType = forms.CharField(label = 'am/pm', max_length=2)
    def dayToInt(self, day):
        if day == "Monday":
            return 0
        elif day == "Tuesday":
            return 1
        elif day == "Wednesday":
            return 2
        elif day == "Thursday":
            return 3
        elif day == "Friday":
            return 4
        elif day == "Saturday":
            return 5
        elif day == "Sunday":
            return 6
        return -1

    def timeWithTimeType(self, timeType):
        if timeType == 'pm':
            return 1
        if timeType == 'am':
            return 1
        return -1


