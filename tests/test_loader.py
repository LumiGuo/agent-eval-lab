from src.evals.loader import load_evalset


def test_evalset_load():

    data = load_evalset(
        "data/evalset.jsonl"
    )

    assert len(data) == 20


def test_required_fields():

    data = load_evalset(
        "data/evalset.jsonl"
    )

    sample = data[0]

    required = [
        "id",
        "category",
        "query",
        "reference_answer",
        "expected_refuses",
        "criteria",
        "source"
    ]

    for field in required:
        assert field in sample
