import json


REQUIRED_FIELDS = [
    "id",
    "category",
    "query",
    "reference_answer",
    "expected_refuses",
    "criteria",
    "source"
]


def validate_sample(sample, line_number):
    """
    Validate one evaluation sample.
    """

    for field in REQUIRED_FIELDS:
        if field not in sample:
            raise ValueError(
                f"Line {line_number}: missing field '{field}'"
            )


def load_evalset(path):
    """
    Load and validate jsonl evaluation dataset.
    """

    samples = []

    with open(path, "r", encoding="utf-8") as f:

        for line_number, line in enumerate(f, 1):

            if not line.strip():
                continue

            try:
                sample = json.loads(line)

            except json.JSONDecodeError as e:
                raise ValueError(
                    f"Line {line_number}: invalid JSON\n{e}"
                )

            validate_sample(sample, line_number)

            samples.append(sample)

    return samples


if __name__ == "__main__":

    data = load_evalset(
        "data/evalset.jsonl"
    )

    print(
        f"Loaded {len(data)} evaluation samples"
    )
