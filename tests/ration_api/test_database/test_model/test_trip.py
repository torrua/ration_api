from tests.conftest import *
from tests.data import first_trip_data


def test_create_trip():
    trip = Trip(**first_trip_data)
    assert trip.title == first_trip_data.get("title")


@pytest.mark.usefixtures("filled_session")
class TestTrip:

    @staticmethod
    def trip(filled_session):
        return (
            filled_session.query(Trip)
            .filter(Trip.title == first_trip_data.get("title"))
            .first()
        )

    def test_number_of_participants(self, filled_session):
        assert self.trip(filled_session).number_of_participants == 3

    def test_common_coefficient(self, filled_session):
        trip_coefficient = sum(
            [p.coefficient for p in self.trip(filled_session).participants]
        )
        assert self.trip(filled_session).common_coefficient == pytest.approx(
            trip_coefficient, abs=0.01
        )

    def test_carbohydrates(self, filled_session):
        assert self.trip(filled_session).carbohydrates == pytest.approx(247.9, abs=0.01)

    def test_fat(self, filled_session):
        assert self.trip(filled_session).fat == pytest.approx(135.36, abs=0.01)

    def test_protein(self, filled_session):
        assert self.trip(filled_session).protein == pytest.approx(106.01, abs=0.01)

    def test_calories(self, filled_session):
        assert self.trip(filled_session).calories == pytest.approx(2609.88, abs=0.01)

    def test_portions(self, filled_session):
        assert len(self.trip(filled_session).portions) == 7

    def test_weight(self, filled_session):
        assert self.trip(filled_session).weight == 1380.0

    def test_trip_delete_with_mealtimes(self, filled_session):
        user = self.trip(filled_session).user
        mealtimes_before = len(user.mealtimes)
        trip = self.trip(filled_session)
        trip_mealtimes = len(trip.mealtimes)
        filled_session.delete(trip)
        filled_session.refresh(user)
        mealtimes_after = len(user.mealtimes)
        assert mealtimes_after == mealtimes_before - trip_mealtimes
