import schedule_generator
import pytest

@pytest.mark.parametrize("num, zon, res", [(2, "Europe/Helsinki", [('Fr', '13/02', 'Closed'), ('Sa', '14/02', '00:05–22:55')]),
                                           (3, "Europe/Helsinki", [('Fr', '13/02', 'Closed'), ('Sa', '14/02', '00:05–22:55'), ('Su', '15/02', '00:05–22:55')]),
                                           (4, "Europe/Helsinki", [('Fr', '13/02', 'Closed'), ('Sa', '14/02', '00:05–22:55'), ('Su', '15/02', '00:05–22:55'), ('Mo', '16/02', '00:05–22:55')]),
                                           (0, "Europe/Helsinki", []),
                                           (-1, "Europe/Helsinki", []),
                                           (2, "Europe/Minsk", [('Fr', '13/02', 'Closed'), ('Sa', '14/02', '00:05–22:55')]),
                                           (2, "America/Los_Angeles", [('Fr', '13/02', 'Closed'), ('Sa', '14/02', '00:05–22:55')]
                                            )])
def test_generate_week_schedule(num, zon, res):
    assert schedule_generator.generate_week_schedule(num, zon) == res
