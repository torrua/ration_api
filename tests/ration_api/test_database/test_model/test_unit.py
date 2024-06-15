from pytest import raises
from sqlalchemy.exc import IntegrityError

from tests.conftest import *


@pytest.mark.usefixtures("filled_session")
class TestUnit:

    @staticmethod
    def unit(filled_session):
        return (
            filled_session.query(Unit)
            .filter(Unit.title == gr_data.get("title"))
            .first()
        )

    def test_delete_unit(self, filled_session):
        unit = self.unit(filled_session)
        assert unit is not None

        with raises(IntegrityError):
            filled_session.delete(unit)
            filled_session.commit()
