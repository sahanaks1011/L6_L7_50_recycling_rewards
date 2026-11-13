import math
from hypothesis import given, strategies as st
from recycling_rewards import parse_collection, weight_average, net_points


# ---------- Property 1: no function should ever crash ----------

@given(st.text() | st.none())
def test_parse_collection_no_crash(s):
    try:
        parse_collection(s)
    except Exception as e:
        assert False, f"parse_collection crashed with: {e!r}"


@given(st.text() | st.none())
def test_weight_average_no_crash(s):
    try:
        weight_average(s)
    except Exception as e:
        assert False, f"weight_average crashed with: {e!r}"


@given(st.text() | st.none())
def test_net_points_no_crash(s):
    try:
        net_points(s)
    except Exception as e:
        assert False, f"net_points crashed with: {e!r}"


# ---------- Property 2: targeted inputs built around each separator ----------

@given(st.text(alphabet="abc:.-0123456789 ", max_size=12))
def test_parse_collection_structured(s):
    try:
        result = parse_collection(s)
    except Exception as e:
        assert False, f"parse_collection crashed on {s!r}: {e!r}"
    if result is not None:
        material, kg = result
        assert material != ""
        assert math.isfinite(kg) and kg >= 0


@given(st.text(alphabet="0123456789,.- ", max_size=12))
def test_weight_average_structured(s):
    try:
        result = weight_average(s)
    except Exception as e:
        assert False, f"weight_average crashed on {s!r}: {e!r}"
    if result is not None:
        assert math.isfinite(result) and result >= 0


@given(st.lists(st.floats(min_value=0, max_value=1e6), min_size=1, max_size=10))
def test_weight_average_correct(weights):
    csv = ",".join(str(w) for w in weights)
    result = weight_average(csv)
    assert result is not None
    assert math.isclose(result, sum(weights) / len(weights), rel_tol=1e-9, abs_tol=1e-9)


@given(st.text(alphabet="0123456789|.-naif ", max_size=12))
def test_net_points_structured(s):
    try:
        result = net_points(s)
    except Exception as e:
        assert False, f"net_points crashed on {s!r}: {e!r}"
    if result is not None:
        assert math.isfinite(result) and result >= 0