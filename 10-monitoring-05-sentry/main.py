import sentry_sdk
sentry_sdk.init(
    dsn="https://5bb0471808b04089b56571edb015a788@o4504965913051136.ingest.sentry.io/4504965916327936",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)