# Live job data

The application does not manufacture starter vacancies. Use `POST /jobs/sync/live` or the **Refresh live listings** button in Explore Jobs to fetch current records from the public Arbeitnow job-board API. Listings are persisted locally in SQLite and attributed to their original source URL. A sync replaces the prior Arbeitnow batch and removes legacy starter-demo records while preserving CSV imports.

The upstream API is external and can change, rate-limit, or become unavailable. In those cases the endpoint returns an error; it does not silently fall back to fake jobs. Always validate role availability on the original listing page. This connector is a practical student-project integration, not a comprehensive global job aggregator.


No fabricated sample listings are bundled or automatically seeded. If upgrading an older database, startup removes records from the legacy source label `Clearly labeled demo dataset`.
