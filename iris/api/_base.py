from abc import abstractmethod, ABC
from datetime import date, datetime

from iris._http_client import HttpClient
from iris.credentials import ICredential
from iris.model import (
    Account,
    Address,
    Announcement,
    Duty,
    Exam,
    Grade,
    GradeAverage,
    GradeSummary,
    Homework,
    KindergartenHours,
    Lesson,
    LuckyNumber,
    MealMenu,
    Meeting,
    Note,
    Message,
    Schedule,
    SchoolInfo,
    PresenceMonthStats,
    PresenceSubjectStats,
    PushSetting,
    Vacation,
    UserEvent,
    Trip,
    Teacher,
    Timeslot,
)

EPOCH_START_DATETIME = datetime(1970, 1, 1, 1, 0, 0)
INT_MIN = -2_147_483_648
DEFAULT_PAGE_SIZE = 500


class IrisApi(ABC):
    _http: HttpClient
    _credential: ICredential

    @abstractmethod
    def __init__(self, credential: ICredential):
        pass

    async def get_accounts(self, pupil_id: int | None = None):
        envelope = await self._http.request(
            method="GET",
            rest_url=self._credential.rest_url,
            endpoint="mobile/register/hebe",
            query={"mode": 2},
            pupil_id=pupil_id,
        )
        return [Account.model_validate(account) for account in envelope]

    async def make_heartbeat(self, rest_url: str, pupil_id: int | None = None):
        await self._http.request(
            method="GET",
            rest_url=rest_url,
            endpoint="mobile/heartbeat",
            pupil_id=pupil_id,
        )

    async def get_addressbook(
            self, rest_url: str, box: str, pupil_id: int | None = None
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            endpoint="mobile/addressbook",
            query={"box": box},
            pupil_id=pupil_id,
        )
        return [Address.model_validate(address) for address in envelope]

    async def get_announcements(
            self,
            rest_url: str,
            pupil_id: int,
            view: int = 6,
            last_sync_date: datetime = EPOCH_START_DATETIME,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/announcements/byPupil",
            query={
                "pupilId": pupil_id,
                "view": view,
                "lastSyncDate": last_sync_date,
                "lastId": last_id,
                "pageSize": page_size,
            },
        )
        return [Announcement.model_validate(announcement) for announcement in envelope]

    async def get_completed_lessons(
            self,
            rest_url: str,
            pupil_id: int,
            date_from: date,
            date_to: date,
            last_sync_date: datetime = EPOCH_START_DATETIME,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/lesson/byPupil",
            query={
                "pupilId": pupil_id,
                "dateFrom": date_from,
                "dateTo": date_to,
                "lastSyncDate": last_sync_date,
                "lastId": last_id,
                "pageSize": page_size,
            },
        )
        return [Lesson.model_validate(lesson) for lesson in envelope]

    async def get_duty(
            self,
            rest_url: str,
            pupil_id: int,
            last_sync_date: datetime = EPOCH_START_DATETIME,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/school/duty/byPupil",
            query={
                "pupilId": pupil_id,
                "lastSyncDate": last_sync_date,
                "lastId": last_id,
                "pageSize": page_size,
            },
        )
        return [Duty.model_validate(duty) for duty in envelope]

    async def get_exams(
            self,
            rest_url: str,
            pupil_id: int,
            date_from: date,
            date_to: date,
            last_sync_date: datetime = EPOCH_START_DATETIME,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/exam/byPupil",
            query={
                "pupilId": pupil_id,
                "dateFrom": date_from,
                "dateTo": date_to,
                "lastSyncDate": last_sync_date,
                "lastId": last_id,
                "pageSize": page_size,
            },
        )
        return [Exam.model_validate(exam) for exam in envelope]

    async def get_grades(
            self,
            rest_url: str,
            unit_id: int,
            pupil_id: int,
            period_id: int,
            last_sync_date: datetime = EPOCH_START_DATETIME,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/grade/byPupil",
            query={
                "unitId": unit_id,
                "pupilId": pupil_id,
                "periodId": period_id,
                "lastSyncDate": last_sync_date,
                "lastId": last_id,
                "pageSize": page_size,
            },
        )
        return [Grade.model_validate(grade) for grade in envelope]

    async def get_grades_averages(
            self,
            rest_url: str,
            unit_id: int,
            pupil_id: int,
            period_id: int,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/grade/average/byPupil",
            query={
                "unitId": unit_id,
                "pupilId": pupil_id,
                "periodId": period_id,
                "lastId": last_id,
                "pageSize": page_size,
                "scope": "auto",
            },
        )
        return [GradeAverage.model_validate(average) for average in envelope]

    async def get_grades_summary(
            self,
            rest_url: str,
            unit_id: int,
            pupil_id: int,
            period_id: int,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/grade/summary/byPupil",
            query={
                "unitId": unit_id,
                "pupilId": pupil_id,
                "periodId": period_id,
                "lastId": last_id,
                "pageSize": page_size,
            },
        )
        return [GradeSummary.model_validate(summary) for summary in envelope]

    async def get_homework(
            self,
            rest_url: str,
            pupil_id: int,
            date_from: date,
            date_to: date,
            last_sync_date: datetime = EPOCH_START_DATETIME,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/homework/byPupil",
            query={
                "pupilId": pupil_id,
                "dateFrom": date_from,
                "dateTo": date_to,
                "lastSyncDate": last_sync_date,
                "lastId": last_id,
                "pageSize": page_size,
            },
        )
        return [Homework.model_validate(homework) for homework in envelope]

    async def get_kindergarten_hours(
            self, rest_url: str, pupil_id: int, constituent_unit_id: int
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/school/hours",
            query={"pupilId": pupil_id, "constituentId": constituent_unit_id},
        )
        return KindergartenHours.model_validate(envelope)

    async def get_kindergarten_teachers(
            self,
            rest_url: str,
            pupil_id: int,
            last_sync_date: datetime = EPOCH_START_DATETIME,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/teacher/kindergarten/byPupil",
            query={
                "pupilId": pupil_id,
                "lastId": last_id,
                "pageSize": page_size,
                "lastSyncDate": last_sync_date,
            },
        )
        return [Teacher.model_validate(teacher) for teacher in envelope]

    async def get_lucky_number(
            self,
            rest_url: str,
            pupil_id: int,
            constituent_unit_id: int,
            day: date = date.today(),
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/school/lucky",
            query={
                "pupilId": pupil_id,
                "constituentId": constituent_unit_id,
                "day": day,
            },
        )
        return LuckyNumber.model_validate(envelope)

    async def get_meal_menu(
            self,
            rest_url: str,
            pupil_id: int,
            full: bool,
            date_from: date,
            date_to: date,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
            last_sync_date: datetime = EPOCH_START_DATETIME,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/eatery",
            query={
                "pupilId": pupil_id,
                "full": full,
                "dateFrom": date_from,
                "dateTo": date_to,
                "lastId": last_id,
                "pageSize": page_size,
                "lastSyncDate": last_sync_date,
            },
        )
        return [MealMenu.model_validate(meal_menu) for meal_menu in envelope]

    async def get_meetings(
            self,
            rest_url: str,
            pupil_id: int,
            date_from: date,
            last_sync_date: datetime = EPOCH_START_DATETIME,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/meetings/byPupil",
            query={
                "pupilId": pupil_id,
                "from": date_from,
                "lastId": last_id,
                "pageSize": page_size,
                "lastSyncDate": last_sync_date,
            },
        )
        return [Meeting.model_validate(meeting) for meeting in envelope]

    async def get_notes(
            self,
            rest_url: str,
            pupil_id: int,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
            last_sync_date: datetime = EPOCH_START_DATETIME,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/note/byPupil",
            query={
                "pupilId": pupil_id,
                "lastId": last_id,
                "pageSize": page_size,
                "lastSyncDate": last_sync_date,
            },
        )
        return [Note.model_validate(note) for note in envelope]

    async def get_planned_lessons(
            self,
            rest_url: str,
            pupil_id: int,
            date_from: date,
            date_to: date,
            last_sync_date: datetime = EPOCH_START_DATETIME,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/lesson/planned/byPupil",
            query={
                "pupilId": pupil_id,
                "dateFrom": date_from,
                "dateTo": date_to,
                "lastSyncDate": last_sync_date,
                "lastId": last_id,
                "pageSize": page_size,
            },
        )
        return [Lesson.model_validate(lesson) for lesson in envelope]

    async def get_presence_month_stats(
            self, rest_url: str, pupil_id: int, period_id: int
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/presence/stats/perMonth",
            query={
                "pupilId": pupil_id,
                "periodId": period_id,
            },
        )
        return [PresenceMonthStats.model_validate(month) for month in envelope]

    async def get_presence_subject_stats(
            self, rest_url: str, pupil_id: int, period_id: int
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/presence/stats/perSubject",
            query={
                "pupilId": pupil_id,
                "periodId": period_id,
            },
        )
        return [PresenceSubjectStats.model_validate(subject) for subject in envelope]

    async def get_received_messages(
            self,
            rest_url: str,
            box: str,
            pupil_id: int,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
            last_sync_date: datetime = EPOCH_START_DATETIME,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/messages/received/byBox",
            query={
                "box": box,
                "pupilId": pupil_id,
                "lastId": last_id,
                "pageSize": page_size,
                "lastSyncDate": last_sync_date,
            },
        )
        return [Message.model_validate(message) for message in envelope]

    async def get_schedule(
            self,
            rest_url: str,
            pupil_id: int,
            date_from: date,
            date_to: date,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
            last_sync_date: datetime = EPOCH_START_DATETIME,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/schedule/withchanges/byPupil",
            query={
                "pupilId": pupil_id,
                "dateFrom": date_from,
                "dateTo": date_to,
                "lastId": last_id,
                "pageSize": page_size,
                "lastSyncDate": last_sync_date,
            },
        )
        return [Schedule.model_validate(schedule) for schedule in envelope]

    async def get_school_info(
            self,
            rest_url: str,
            pupil_id: int,
            last_sync_date: datetime = EPOCH_START_DATETIME,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/school/info",
            query={
                "pupilId": pupil_id,
                "lastSyncDate": last_sync_date,
            },
        )
        return [SchoolInfo.model_validate(school_info) for school_info in envelope]

    async def get_teachers(
            self,
            rest_url: str,
            period_id: int,
            pupil_id: int,
            last_sync_date: datetime = EPOCH_START_DATETIME,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/teacher/byPeriod",
            query={
                "periodId": period_id,
                "pupilId": pupil_id,
                "lastId": last_id,
                "pageSize": page_size,
                "lastSyncDate": last_sync_date,
            },
        )
        return [Teacher.model_validate(teacher) for teacher in envelope]

    async def get_timeslots(self, pupil_id: int | None = None):
        envelope = await self._http.request(
            method="GET",
            rest_url=self._credential.rest_url,
            endpoint="mobile/dictionary/timeslot",
            query={"pupilId": pupil_id},
            pupil_id=pupil_id,
        )
        return [Timeslot.model_validate(timeslot) for timeslot in envelope]

    async def get_trips(
            self, rest_url: str, pupil_id: int, date_from: date, date_to: date
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/trips/byPupil",
            query={
                "pupilId": pupil_id,
                "dateFrom": date_from,
                "dateTo": date_to,
            },
        )
        return [Trip.model_validate(trip) for trip in envelope]

    async def get_user_events(
            self,
            rest_url: str,
            pupil_id: int,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/userEvents/byPupil",
            query={
                "pupilId": pupil_id,
            },
        )
        return [UserEvent.model_validate(user_event) for user_event in envelope]

    async def get_vacations(
            self,
            rest_url: str,
            pupil_id: int,
            date_from: date,
            date_to: date,
            last_sync_date: datetime = EPOCH_START_DATETIME,
            last_id: int = INT_MIN,
            page_size: int = DEFAULT_PAGE_SIZE,
    ):
        envelope = await self._http.request(
            method="GET",
            rest_url=rest_url,
            pupil_id=pupil_id,
            endpoint="mobile/school/vacation",
            query={
                "pupilId": pupil_id,
                "dateFrom": date_from,
                "dateTo": date_to,
                "lastId": last_id,
                "pageSize": page_size,
                "lastSyncDate": last_sync_date,
            },
        )
        return [Vacation.model_validate(vacation) for vacation in envelope]

    async def change_message_importance(
            self,
            rest_url: str,
            box_key: str,
            message_key: str,
            importance: bool,
            pupil_id: int | None = None
    ):
        await self._http.request(
            method="POST",
            endpoint="mobile/messages/importance",
            rest_url=rest_url,
            pupil_id=pupil_id,
            payload={
                "BoxKey": box_key,
                "MessageKey": message_key,
                "Importance": importance
            }
        )

    async def change_message_status(
            self,
            rest_url: str,
            box_key: str,
            message_key: str,
            status: int,
            pupil_id: int | None = None
    ):
        await self._http.request(
            method="POST",
            endpoint="mobile/messages/status",
            rest_url=rest_url,
            pupil_id=pupil_id,
            payload={
                "BoxKey": box_key,
                "MessageKey": message_key,
                "Status": status
            }
        )

    async def set_push_locale(
            self,
            locale: str,
            pupil_id: int | None = None
    ):
        await self._http.request(
            method="POST",
            endpoint="mobile/push/locale",
            rest_url=self._credential.rest_url,
            pupil_id=pupil_id,
            payload=locale,
            verify_response=False
        )

    async def set_all_push_setting(
            self,
            turn_on: bool,
            pupil_id: int | None = None
    ):
        await self._http.request(
            method="POST",
            endpoint="mobile/push/all",
            rest_url=self._credential.rest_url,
            pupil_id=pupil_id,
            payload="on" if turn_on else "off"
        )

    async def set_push_setting(
            self,
            option: str,
            active: bool,
            pupil_id: int | None = None
    ):
        envelope = await self._http.request(
            method="POST",
            endpoint="mobile/push",
            rest_url=self._credential.rest_url,
            pupil_id=pupil_id,
            payload={
                "Option": option,
                "Active": active
            }
        )
        return PushSetting.model_validate(envelope)

    async def configure_push(
            self,
            options: dict[str, bool],
            locale: str,
            pupil_id: int | None = None
    ):
        envelope_options = []
        for name, active in options.items():
            envelope_options.append({
                "Option": name,
                "Active": active
            })

        envelope = await self._http.request(
            method="POST",
            endpoint="mobile/push/configure",
            rest_url=self._credential.rest_url,
            pupil_id=pupil_id,
            payload={
                "Options": envelope_options,
                "Locale": locale
            }
        )
        return [PushSetting.model_validate(push) for push in envelope]

    async def delete_credential(
            self,
            pupil_id: int | None = None
    ):
        await self._http.request(
            method="DELETE",
            endpoint="mobile/register",
            rest_url=self._credential.rest_url,
            pupil_id=pupil_id
        )
