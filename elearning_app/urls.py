from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import UsersView,CourseDetailsViewset,ClassDetailsViewset,EmployeeDetailsView,StudentDetailView,EmployeeTypeView,CourseSectionViewset,CourseSubSectionViewset,mark_attendance
router = DefaultRouter()
router.register(r"user", UsersView, basename="user")
router.register(r"course-details", CourseDetailsViewset , basename="course-details")
router.register(r"employee-details", EmployeeDetailsView, basename="employee-details")
router.register(r"employee-type", EmployeeTypeView, basename="employee-type")
router.register(r"student-details", StudentDetailView, basename="student-details")
router.register(r"class-details", ClassDetailsViewset, basename="class-details")
router.register(r"course-section", CourseSectionViewset, basename="course-sections")
router.register(r'attendance', mark_attendance, basename="attendance")

urlpatterns = router.urls

urlpatterns = [
    *router.urls,
    path('mark-attendance/<int:course_id>/', mark_attendance.as_view, name='mark-attendance'),
]
    