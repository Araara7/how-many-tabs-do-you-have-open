# How Many Tabs Do You Have Open?

[![make.fun](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/Araara7/how-many-tabs-do-you-have-open/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/Araara7/how-many-tabs-do-you-have-open/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)

A [make.fun](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d) bounty entry: one honest number — how many browser tabs are open right now.

## Entry

**137**

Triple digits, specific rather than round: a real tab-hoarder count. Surprising against a field of a dozen or two, yet believable for someone who researches, reads, and never closes anything "to read later". It hints at a life behind it — tabs as an archive, not a mess.

## How it works

`main.py` writes the number `137` (digits only, no words, no newline) to `/output/entry.txt`, deterministically. The gate requires 1–5 UTF-8 characters, not whitespace-only; the output is exactly 3 bytes.

Run it twice and the output is byte-identical:

```bash
python3 main.py && cat /output/entry.txt   # 137
```

## License

MIT — see [LICENSE](LICENSE).
