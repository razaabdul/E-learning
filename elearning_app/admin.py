from django.contrib import admin
from .models import *
admin.site.register(User)
admin.site.register(CourseDetails)
admin.site.register(ClassDetails)
admin.site.register(CourseSection)
admin.site.register(CourseSubSection)
admin.site.register(CourseType)
admin.site.register(CourseLevel)
admin.site.register(OTP)
admin.site.register(EmployeePosition)
admin.site.register(BlacklistedToken)
