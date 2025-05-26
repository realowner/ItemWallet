import pytz

from datetime import datetime

from sqlalchemy.orm import Mapper
from sqlalchemy import event

from app.models.mixins import TimestampMixin


#TODO: при импорте лиснера в инит вызывает ошибки, разобраться
@event.listens_for(TimestampMixin, "before_update", propagate=True)
def update_timestamp(mapper: Mapper, connection, target):
    if isinstance(target, TimestampMixin):
        target.updated_at = datetime.now(pytz.UTC)
