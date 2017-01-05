
import yaml
from nose.tools import assert_equal
from greengraph import Greengraph
import numpy.testing as npt
import os

def test_geolocate():
    with open(os.path.join(os.path.dirname(__file__),
                           'fixtures', 'graph.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            answer = Greengraph(**fixture)
            assert_equal(answer.start, fixture['start'])
            assert_equal(answer.end, fixture['end'])
            assert_equal(answer.geocoder.domain, "maps.google.co.uk")