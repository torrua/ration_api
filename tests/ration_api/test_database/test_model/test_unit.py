from tests.conftest import *


@pytest.mark.usefixtures("filled_session")
class TestUnit:

    def test__repr__(self, filled_session):
        pass
