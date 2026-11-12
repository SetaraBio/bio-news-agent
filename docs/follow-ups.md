# Known limitations

Accepted for now. None of these is scheduled work.

- **Late recovery.** If the local agent run does not publish, the scheduled `digest.yml` fallback publishes an API digest later that day. GitHub has started these scheduled runs hours after the 12:30 PM Eastern target. After the GitHub organization rename, digests were missing Sep 22–27, 2026; publishing resumed Sep 28.
- **Repeated stories after a late digest.** Candidates come from a rolling 24-hour window, so a late digest's window can overlap the next one. Three adjacent digest pairs between Jul 16 and Sep 29, 2026 shared 6 URLs in total, each after a later-than-usual publication.
- **API runs fall back instead of failing.** `digest.yml` and a local `uv run python src/main.py` use the API path. If the API call fails, they render locally categorized results to `news.md` rather than stopping; `digest.yml` then publishes that output in a separate step. On that path, unknown `top_stories` references are dropped silently (top stories are auto-selected if none remain). Agent runs reject invalid top-story references.
- **Unknown categories fall back to keyword matching** in both API and agent runs.
