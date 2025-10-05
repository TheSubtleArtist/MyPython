from collections import Counter
from pathlib import Path
import re
import sys

def get_vote_tally(text):
    """Count votes and group by frequency."""
    counts = Counter(re.findall(r"\d+", text))
    tally_groups = {}
    for choice, count in counts.most_common():
        tally_groups.setdefault(count, []).append(int(choice))
    return [
        (count, sorted(choices))
        for count, choices in tally_groups.items()
    ]

def main():
    [votes_filename] = sys.argv[1:]
    contents = Path(votes_filename).read_text()
    for count, choice_group in get_vote_tally(contents):
        if count > 1:
            votes = "votes"
        else:
            votes = "vote"
        choices = ", ".join([str(vote) for vote in choice_group])
        print(f"{count} {votes} for:", choices)

if __name__ == "__main__":
    main()